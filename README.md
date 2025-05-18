<<<<<<< HEAD
# TEXT-SUMMARIZATION-TOOL
A versatile text summarization tool that supports multiple input formats (text, PDF, DOC) and generates concise summaries in various styles like bullet points, key points, and subheadings. Built with an interactive, user-friendly UI.
=======
# 📝 Text Summarization Tool 

A Streamlit-based application that summarizes lengthy text, PDFs, and Word documents using state-of-the-art abstractive summarization models from Hugging Face like **BART-large-cnn**. Designed with an interactive, modern UI for seamless summarization and exploration of long-form content. Developed as part of an internship project at **CODTECH IT SOLUTIONS PVT. LTD.**

---

## 🏢 Internship Details

- **Company**: CODTECH IT SOLUTIONS PVT. LTD.  
- **Name**: Gajangi Malavika  
- **Intern ID**: C0DF141  
- **Domain**: Artificial Intelligence Markup Language  

---

## 📌 Project Overview

This project centers on building a user-friendly UI for summarizing large articles, research papers, reports, and documents using abstractive summarization techniques via Hugging Face Transformers. The app allows users to input text manually or upload PDF/DOCX files, select summarization modes, adjust summary length, and visualize results in a clean, interactive layout.

---

## 🚀 Features

- 📑 Summarize lengthy text articles, PDFs, and DOCX files  
- 🧠 Abstractive summarization with BART-large-cnn model  
- 📃 Multiple input formats: manual text, PDF, DOCX  
- ⚙ Adjustable summary length (default: half of input length)  
- 📝 Choose summarization type: Paragraph, Bullet Points, Key Points, or With Subheadings  
- 📊 Word count display for input and summaries  
- 💾 Clean, responsive, and officially-themed Streamlit UI  
- 🎨 Custom theming with branded colors and logo  
- 📥 Download summaries easily (future upgrade scope)

---

## 🛠 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **Model**:  
  - Hugging Face Transformers (`facebook/bart-large-cnn`)  
- **Libraries**:  
  - `transformers`  
  - `torch`  
  - `PyPDF2`  
  - `python-docx`  
  - `streamlit`

---

## 🔧 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/text-summarization-tool-app.git
cd text-summarization-tool-app