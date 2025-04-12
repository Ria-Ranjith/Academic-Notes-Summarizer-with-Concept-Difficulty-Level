import openai
from dotenv import load_dotenv
import os
import streamlit as st
from utils import extract_pdf_text, extract_docx_text, generate_summary_and_flashcards

# Load environment variables from the .env file
load_dotenv()

# Load the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Academic Notes Summarizer")

# File upload section
uploaded_file = st.file_uploader("Upload your academic notes", type=["pdf", "docx"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary file path
    with open(f"temp_{uploaded_file.name}", "wb") as temp_file:
        temp_file.write(uploaded_file.getbuffer())

    # Extract text based on file type
    if uploaded_file.type == "application/pdf":
        text = extract_pdf_text(f"temp_{uploaded_file.name}")
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = extract_docx_text(f"temp_{uploaded_file.name}")

    # Display extracted text in a text area
    st.text_area("Extracted Notes", text, height=300)

    # Process the extracted text using Langflow chain to generate summary and flashcards
    if text:
        result = generate_summary_and_flashcards(text)
        st.text_area("Summary and Flashcards", result, height=300)

