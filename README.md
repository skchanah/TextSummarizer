# Text-summarizer

## Introduction and Model information
A mini summarizer app using streamlit and OpenAI's gpt-3.5-turbo-instruct (previously the deprecated text-davinci-003) model. Max input token is limited to 2000.

Below are key facts from openai.com about the model:
> Context window: 4,096 tokens (Input + Output)
> 
> Last trained data: up to Sep 2021

## API Keys
Before you use the app, please create a .streamlit hidden file to store your OpenAI API key, and also, to make it accessible to streamlit. Go to the root of this repo, enter below command:

```
mkdir .streamlit
cd .streamlit
touch secrets.toml
```

In the secrets.toml, paste your key as below:
> OPENAI_KEY = "your_key_here"

## Run
Run below in root of the repo for the environment

```
source venv/bin/activate
```

To run the app, run the below command in the root of the repo

```
streamlit run app.py
```

This shall open a browser page alike to below.
![Screenshot of the app](/assets/images/app_preview.png)

## Pending Updates
1. Duckduckgo algorithm to replace gpt 3.5
2. Langchain to further optimize the summarization

## Acknowledgement
Shout out to Jay Peterman @ medium for the motivations and inspirations
https://towardsdatascience.com/make-a-text-summarizer-with-gpt-3-f0917a07189e
