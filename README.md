# Feynman.AI


## Table of Contents
* [About the project](#about-the-project)
* [Setting Up](#setting-up)
* [Diagrams](#diagrams)
* [Result and Analysis](#result-and-analysis)
* [Technology Used](#technology-used)
* [Authors](#authors)
* [Credits](#credits)


## About the project
Feynman.AI makes online learning through educational videos more effective for individuals with learning disabilities. Around 20% of the world's population suffers from Dyslexia, and 4% from ADHD. This impedes their ability to learn since they are unable to absorb the important information from dense content as well as retain it while maintaining their concentration for extended periods of time. Most educational materials present in videos online are large in duration and contain complex information. This raises the difficulty of learning new content for learners with disabilities. Our product addresses their issue by generating short and intuitive explanations of large videos from YouTube. Our goal is to reduce the time taken to comprehend long videos while enhancing retention of information. We enhance their ability to focus by providing an audio explanation of the simplified content, which the learner can listen to while reading. The notes generated also include explanations of the jargon used, formulae presented, and mnemonics to help retain important facts contained in the video. At Feynman.AI, we leverage the power of artificial intelligence to make learning more inclusive. Our product pipeline initially extracts audio from a YouTube link that the user provides. The audio file is run through the WhisperAI model to extract text. We have a competitive edge since the model supports over 90 languages, increasing accessibility for learners from different geographical locations. This text is then supplied to the GPT 3.5 Turbo model, which is designed to generate notes from the text. To assist learners, the notes are also converted into an audio file. Finally, the output is deployed as a Streamlit web application. The user interface is simple, intuitive, and aesthetically pleasing to reduce any potential distractions.

## Setting Up
- Step 1: run the command "pip install -r requirements"
- Step 2: Paste your [OpenAI API key](https://platform.openai.com/account/api-keys) in a new file with the name "secrets.toml"
- Step 3: run the command "streamlit run app.py"

## Diagrams
- ### **FlowChart**
![Flowchart](https://user-images.githubusercontent.com/59303406/228313163-cbc65662-4600-43b2-b817-7026e11a749a.png)


## Result and Analysis
![intro_page](https://user-images.githubusercontent.com/59303406/228673401-fab1e61e-d711-45b3-b60a-b1baf5ceaece.png)
![start](https://user-images.githubusercontent.com/59303406/228673409-9534d165-7b80-4d51-b82e-e7874dddb33f.png)
![audio_page](https://user-images.githubusercontent.com/59303406/228673410-dd8b4430-40f1-4c26-98ca-462f4084004b.png)
![end](https://user-images.githubusercontent.com/59303406/228673413-900e0023-325f-45ef-a962-86e46c96f3cd.png)
## Technology Used
- [Whisper API](https://openai.com/research/whisper)
- [ChatGPT](https://openai.com/product/gpt-4)
- [Streamlit](https://streamlit.io/)

## Authors
- [Ryan Nayak](https://github.com/ryannayak28)
- [Ryan Varghese](https://github.com/ryanvarghese)
- [Shlok Pikle](https://github.com/KarMeno)
- [Karthik Menon](https://github.com/ShlokP07)


## Credits
- [Whisper API](https://openai.com/research/whisper)
- [ChatGPT](https://openai.com/product/gpt-4)
