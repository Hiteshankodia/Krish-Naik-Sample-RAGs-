from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

#Prompt template 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful. Please response to the user queries"),
        ("user", "Question :{question}")
    ]
)

#Streamlit  Framework 

st.title('Langchain Demo with Gemini')
input_text = st.text_input("Search The Topic You Want")

#Gemini LLM 

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",
                             temperature=0.3)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))