# Text-summarizer

## Introduction and Model information
A mini summarizer app using streamlit and OpenAI's gpt-3.5-turbo-instruct (previously the deprecated text-davinci-003) model.

Below are key facts from openai.com about the model:
> Context window: 4,096 tokens
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
To run the app, run the below command in the root of the repo

```
streamlit run app.py
```

This shall open a browser page alike to below.
![Screenshot of the app](/assets/images/app_preview.png)

## Acknowledgement
Shout out to Jay Peterman@medium for the tutorial
https://towardsdatascience.com/make-a-text-summarizer-with-gpt-3-f0917a07189e
