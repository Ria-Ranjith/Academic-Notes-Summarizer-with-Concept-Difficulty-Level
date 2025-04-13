import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    # Test API connection
    available_models = [m.name for m in genai.list_models()]
    st.sidebar.success(f"✅ API Connected | Available models: {', '.join(available_models)}")
    
    # Verify desired model is available
    desired_model = 'models/gemini-1.5-pro-latest'
    if desired_model not in available_models:
        st.sidebar.warning(f"⚠️ {desired_model} not available. Falling back to gemini-pro")
        desired_model = 'gemini-pro'
except Exception as e:
    st.sidebar.error(f"❌ API Connection Failed: {str(e)}")
    st.stop()  # Stop the app if API connection fails

# Initialize the model with automatic fallback
model = genai.GenerativeModel(desired_model)

def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""  # Handle None returns
        return text.strip()
    except Exception as e:
        st.error(f"PDF extraction error: {str(e)}")
        return ""

def extract_text_from_docx(docx_file):
    try:
        doc = Document(docx_file)
        return '\n'.join(paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip())
    except Exception as e:
        st.error(f"DOCX extraction error: {str(e)}")
        return ""

def generate_summary_and_flashcards(notes_content):
    if not notes_content.strip():
        st.error("No text content found in the document")
        return None

    prompt = f"""
    Given the following academic notes:
    {notes_content}
    
    Please perform the following tasks:
    1. Summarize the content into clear, concise key points (3-5 bullet points).
    2. Generate 5-10 flashcards with questions and answers based on the notes.
    3. Rate the overall difficulty level of the concepts (Easy/Medium/Hard).
    
    Format your response exactly as follows:
    
    SUMMARY:
    [Your summary here]
    
    FLASHCARDS:
    1. Q: [Question 1]
       A: [Answer 1]
    2. Q: [Question 2]
       A: [Answer 2]
    ...
    
    DIFFICULTY LEVEL: [Easy/Medium/Hard]
    """
    
    try:
        response = model.generate_content(prompt)
        if not response.text:
            st.error("Empty response from Gemini API")
            return None
        return response.text
    except Exception as e:
        st.error(f"Generation error: {str(e)}")
        return None

def main():
    st.title("📚 Academic Notes Summarizer with Concept Difficulty Assessment")
    
    uploaded_file = st.file_uploader(
        "Upload your notes", 
        type=["pdf", "docx"],
        help="Supported formats: PDF or DOCX",
        label_visibility="visible"
    )
    
    if uploaded_file is not None:
        with st.spinner("Extracting text..."):
            if uploaded_file.type == "application/pdf":
                text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = extract_text_from_docx(uploaded_file)
            else:
                st.error("Unsupported file type")
                return
        
        if text:
            st.subheader("📄 Extracted Text Preview")
            st.text_area(
                "Extracted content", 
                value=text, 
                height=200,
                label_visibility="collapsed"
            )
            
            if st.button("✨ Generate Summary and Flashcards", type="primary"):
                with st.spinner("Generating content..."):
                    output = generate_summary_and_flashcards(text)
                    
                    if output:
                        # Display results in expandable sections
                        with st.expander("📝 Summary", expanded=True):
                            if "SUMMARY:" in output:
                                summary = output.split("SUMMARY:")[1].split("FLASHCARDS:")[0].strip()
                                st.markdown(summary)
                        
                        with st.expander("📚 Flashcards (Q&A)"):
                            if "FLASHCARDS:" in output:
                                flashcards = output.split("FLASHCARDS:")[1].split("DIFFICULTY LEVEL:")[0].strip()
                                st.markdown(flashcards)
                        
                        with st.expander("📊 Difficulty Assessment"):
                            if "DIFFICULTY LEVEL:" in output:
                                difficulty = output.split("DIFFICULTY LEVEL:")[1].strip()
                                st.metric("Difficulty", difficulty)

if __name__ == "__main__":
    main()
                   