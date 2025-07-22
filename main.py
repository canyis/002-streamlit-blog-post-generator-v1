import streamlit as st
from langchain_openai import OpenAI
from langchain import PromptTemplate

st.set_page_config(
    page_title = "Blog Post Generator"
)

st.title("Blog Post Generator")

openai_api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type = "password"
)

def generate_response(topic, tam, language):
    llm = OpenAI(openai_api_key=openai_api_key)
    template = """
    As experienced startup and venture capital writer, 
    generate a {tam}-word blog post about {topic}
    
    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the result like this: This post has X words.
    Remember to use the {language} language.
    Add the sources used to write the blog post at the end of the response, like this: Sources: [source1, source2, ...]
    Do not include any other text or explanation, just the blog post and the sources.
    Do not use any markdown formatting.
    """
    prompt = PromptTemplate(
        input_variables = ["topic", "tam","language"],
        template = template
    )
    query = prompt.format(topic=topic, tam=tam, language=language)
    response = llm(query, max_tokens=2048)
    return st.write(response)


topic_text = st.text_input("Enter topic: ")
max_length = st.slider("Max length", 100, 50, 400)
text_tone = st.selectbox(
    "Tone",
    ["Professional", "Casual", "Friendly", "Formal", "Informative"]
)
text_language = st.selectbox(
    "Language",
    ["English", "Spanish", "French", "German", "Italian"]
)
if not openai_api_key.startswith("sk-"):
    st.warning("Enter OpenAI API Key")
if openai_api_key.startswith("sk-"):
    generate_response(topic_text, max_length, text_language)
        
