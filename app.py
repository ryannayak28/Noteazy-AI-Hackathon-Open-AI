import openai
import os
import toml
from pytube import YouTube
import streamlit as st
from PIL import Image
import re
from gtts import gTTS


#------------Set up OpenAI API credentials------------
# with open("/secrets/secrets.toml", "r") as f:
#     config = toml.load(f)

openai.api_key = st.secrets["OPENAI_KEY"]

#------------Model------------
def video_to_audio(video_URL:str, destination:str)-> None:
  '''
  Downloads the audio of the input URL and saves it into a .mp3 audio file
    Args:
            video_URL(str): URL of a youtube video
            
            destination(str): path to temporarily store the extracted audio file
    Returns:
            None
  '''   
  video = YouTube(video_URL)
  
  # Convert video to Audio
  audio = video.streams.filter(only_audio=True).first()
  output = audio.download(output_path = destination)  
  _, ext = os.path.splitext(output)
  new_file = "Target_audio" + '.mp3'
  # Change the name of the file
  os.rename(output, new_file)

def audio_to_text()-> None:
  '''
  Converts Target_audio.mp3 into text using whisper-1 model
    Args:
            None
            
    Returns:
            None
  '''  
  audio_file= open("Target_audio.mp3", "rb")
  transcript = openai.Audio.translate("whisper-1", audio_file)
  return transcript['text']

def markdown_to_voice(text:str)-> str: 
  '''
  Converts markdown into plain text format and saves it in voice_file.mp3
  Args:
          text(str): text in the format of markdown
          
  Returns:
          None
  '''
  output_file = "'assets/audio/notes_voice.mp3'"
  
  #Convert markdown to plain text
  cleaned_text = text.replace('#', ' ').replace('-', ' ').replace('.', ' ')

  speech = gTTS(text = text)
  speech.save(output_file)
  


def generate_notes(text:str)-> str:
  '''
    Generates notes from input text
    Args:
            text(str): Generated text from audio file
            
    Returns:
            reply(str): Notes formatted in Markdown format
  '''
  prompt = """You are a teacher helping teach students with learning disabilities such as Dyslexia and ADHD. 
              
              The answer provided should always include these 5 sections listed below and should also contain any of the OPTIONAL SECTIONS listed above if applicable: 
                    1) Title: containing an apt title for the text,
                    2) Summary: a brief summary containing a creative, meaningful and intuitive explanation of the text, 
                    3) Key Takeaways: containing important points to remember from the text,
                    4) Mnemonics: use mnemonic devices (acronyms, acrostics, association, chunking, method of loci, songs or rhymes) to remember any important facts in the text,
                    5) Quiz Yourself!: a short quiz with questions on the key takeaways from the text along with the answers.
              The answer provided must also include any of these optional sections below if conditions are true:
              OPTIONAL SECTIONS:
                    - Formulae: containing any important formulae mentioned in the text, 
                    - Code: containing any snippets of code mentioned in the text,
                    - Trivia: include an any important dates or information about important entities such persons, organizations, etc mentioned in text,
                    - Jargons: provide short explanations for any jargons present in the text,

              The answer generated must always be appropiately formatted using the Markdown with each section being a subheading.              
              The language used to answer should be simple, compassionate and easily visualizable.
            """

  messages = [
              {"role": "system", "content": prompt}, 
              {"role": "user", "content": text}
              ]

  chat = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", 
      messages=messages, 
      temperature=1.2,
      top_p=0,
      n=1,
      stream=False,
      presence_penalty=0,
      frequency_penalty=0)
  
  reply = chat.choices[0].message.content
  return(reply)

def display_sidebar(text:str)-> None:
  '''
  Display the Markdown notes in the streamlit app
    Args:
            text(str): text in Markdown format 
            
    Returns:
            None
  '''
  # Use regular expressions to find level 2 headers
  pattern = r'^##\s+.+$'
  headers = re.findall(pattern, text, re.MULTILINE)

  # Add the headers to the sidebar
  st.sidebar.markdown('## Table of Contents')
  for header in headers:
      text_without_hashes = header.replace('##', '').strip()
      st.sidebar.markdown(f'- [{text_without_hashes}](#{text_without_hashes.lower().replace(" ", "-")})')

  # Display the full text with headers
  st.markdown(text, unsafe_allow_html=True)


#------------Streamlit app------------
def app():
  
  st.set_page_config(page_title="Feynman.AI")  
  st.title("Feynman.AI 📑")
 
  with st.sidebar:   
    # Add the logo image to the sidebar
    image = Image.open("assets/images/feynmanai-no-bg.png")
    st.image(image)
    
    # Add the header to the sidebar
    st.header("Understanding complex topics made simple!")
    st.write("_For students with special needs._")
    
  # Get user input
  video_URL = st.text_input("Paste the video URL here.")

  # Generate Notes
  if st.button("Generate Notes"):
      if video_URL:
          with st.spinner('Simplifying the content 📖....'):
            destination = "."
            video_to_audio(video_URL, destination)
            text = audio_to_text()
            os.remove('Target_audio.mp3')
            output = generate_notes(text)
          st.video(video_URL)
          st.write("Listen to the notes in voice")
          markdown_to_voice(output)
          st.audio('assets/audio/notes_voice.mp3')
          display_sidebar(output)
      else:
          st.warning("Please enter some text to summarize.")

# Run the Streamlit app
if __name__ == '__main__':
    app()
