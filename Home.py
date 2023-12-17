import streamlit as st
from langchain.prompts import PromptTemplate

st.title("Hello World")

st.subheader("Welcome to Streamlit!")

st.write([1, 2, 3, 4])
st.write(PromptTemplate) # class 출력

p = PromptTemplate.from_template("xxxx")
st.write(p)