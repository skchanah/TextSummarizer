import openai
import streamlit as st
from langchain.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

wrapper = DuckDuckGoSearchAPIWrapper(max_results=2)

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    st.session_state["search"] = ""
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=2000,
        )["choices"][0].message.content # deprecated ["text"]
    except:
        st.write('There was an error =(')

def search(prompt):
    st.session_state["summary"] = ""
    try:
        st.session_state["search"] = DuckDuckGoSearchRun(api_wrapper=wrapper, source="news").run(f"{prompt}")
    except:
        st.write('There was an error =(')