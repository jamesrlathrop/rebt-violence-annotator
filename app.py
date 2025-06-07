
import streamlit as st
from utils import load_docx, annotate_text, generate_bibliography

st.set_page_config(page_title="REBT Violence Annotator", layout="wide")

st.title("📘 REBT Language of Violence Annotator")
st.write("Upload a `.docx` chapter to receive annotated REBT-based suggestions and inline citations.")

uploaded_file = st.file_uploader("Upload a .docx file", type=["docx"])

if uploaded_file:
    raw_text = load_docx(uploaded_file)
    clean_text, annotations = annotate_text(raw_text)
    biblio = generate_bibliography()

    st.subheader("✏️ Clean Academic Version")
    st.text_area("Edited Text", clean_text, height=300)

    st.subheader("📝 Annotated Version")
    st.text_area("Annotated Text", annotations, height=300)

    st.subheader("📚 APA-Style Bibliography")
    st.text_area("Bibliography", biblio, height=200)
