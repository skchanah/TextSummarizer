import streamlit as st
import openai
from langchain.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
import os
from text_summarizer.functions import summarize, search

try:
  # Please update your key in the .secret/secretkey.toml
  openai.api_key = os.getenv('OPENAI_KEY') 
  
  if "summary" not in st.session_state:
      st.session_state["summary"] = ""

  if "summary_ddg" not in st.session_state:
      st.session_state["summary_ddg"] = ""
  
  st.title("Text Summarizer")
  
  input_text = st.text_area(label="Enter full text:", value="", height=250)
  st.button(
      "Submit",
      on_click=summarize,
      kwargs={"prompt": input_text},
  )
  st.button(
      "Search",
      on_click=search,
      kwargs={"prompt": input_text},
  )
  sesh_state = st.session_state["summary"] if st.session_state["summary"] else st.session_state["search"]
  output_text = st.text_area(label="Result", value=sesh_state, height=250)
  #output_text_search = st.text_area(label="Summarized by Duck Duck Go:", value=st.session_state["search"], height=250)
except:
  st.write('There was an error =(')