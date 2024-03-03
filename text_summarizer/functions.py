import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=2000,
        )["choices"][0].message.content # deprecated ["text"]
    except:
        st.write('There was an error =(')