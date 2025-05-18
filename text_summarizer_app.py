import streamlit as st
from app.summarizer import summarize_text
from app.file_handler import read_pdf, read_docx

st.set_page_config(page_title="CodTech Text Summarizer", page_icon="📝", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📝Text Summarization Tool📝")
st.subheader("Summarize text, PDFs, and Word documents with smart modes")

# Input Type Selection
input_type = st.radio("📄 Choose your input type:", ("Manual Text", "Upload PDF", "Upload DOCX"), horizontal=True)

text = ""

if input_type == "Manual Text":
    text = st.text_area("✏️ Enter or paste your text here:", height=300)

elif input_type == "Upload PDF":
    uploaded_pdf = st.file_uploader("📥 Upload a PDF file", type=["pdf"])
    if uploaded_pdf:
        text = read_pdf(uploaded_pdf)

elif input_type == "Upload DOCX":
    uploaded_docx = st.file_uploader("📥 Upload a DOCX file", type=["docx"])
    if uploaded_docx:
        text = read_docx(uploaded_docx)

if text:
    st.info(f"✅ Input Text Length: {len(text.split())} words")

    # Summary length controls
    default_summary_length = max(100, len(text.split()) // 2)
    max_len = st.slider("📝 Select summary length (words)", 100, 2000, default_summary_length, 50)

    # Summarization mode
    mode = st.selectbox("🎨 Choose summarization style:",
                        ["Paragraph Summary", "Bullet Points", "Key Points", "With Subheadings"])

    if st.button("🧠 Summarize Now"):
        with st.spinner("Generating summary..."):
            summary = summarize_text(text, max_length=max_len)

            if mode == "Bullet Points":
                summary = "• " + summary.replace(". ", ".\n• ")
            elif mode == "Key Points":
                summary = summary.replace(". ", ".\n- ")
            elif mode == "With Subheadings":
                summary = "### Summary\n" + summary

            st.success("✅ Summary Generated")
            st.text_area("📑 Summary:", value=summary, height=300)

else:
    st.warning("⚠️ Please enter or upload some content to summarize.")

st.caption("Built with ❤️ by CodTech Intern")
