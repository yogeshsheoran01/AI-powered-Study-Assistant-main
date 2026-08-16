# 📘 **SGPA — Study Guide & Personal Assistant**
## *AI-Powered Study Assistant*

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![Gemini API](https://img.shields.io/badge/Backend-Gemini%202.5%20Flash-blue?logo=google)
![Python](https://img.shields.io/badge/Language-Python-yellow?logo=python)
![IBM SkillsBuild](https://img.shields.io/badge/AICTE%20x%20IBM-SkillsBuild%20Internship-orange?logo=ibm)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![Version](https://img.shields.io/badge/version-1.2.0-purple)

---

## 🧠 **Project Overview**

Students often struggle to grasp difficult topics or summarize lengthy notes.

AI-Powered Study Assistant is an AI-powered web application that acts as a personal academic assistant, capable of:

🧩 Explaining complex concepts in simple terms
📄 Summarizing notes or uploaded PDFs
❓ Generating quizzes
📝 Solving exam questions
✅ Evaluating answers and providing feedback

The application combines Streamlit for the user interface and Google Gemini 2.5 Flash API for fast and intelligent AI responses in a clean, chat-based interface.

---

Recent updates (v1.2.0):

- Explainer now suggests simple sketchable diagrams for visual understanding.
- Summarizer handles very short or scanned PDFs more safely with clearer warnings.
- Added lightweight, privacy-friendly usage analytics (anonymous sessions and mode usage).

---

## ⚙️ **System Design**

### 🏗️ **Architecture**
A lightweight **Streamlit frontend** interacts with **Google Gemini 2.5 Flash** backend via secure API calls.  
All secrets managed safely via `.env` and `st.secrets`.

### 🧩 **Core Features**

| Mode        | Function                                                           | Example                       |
|-------------|--------------------------------------------------------------------|-------------------------------|
| 🧠 **Explainer**      | Simplifies academic concepts                                   | “Explain Deadlock in OS”      |
| 📄 **Summarizer**     | Condenses notes or PDFs                                       | Upload 20-page PDF → summary  |
| 🧩 **Quizzer**        | Quiz generator, solver, evaluator (multi-mode workflow)       | MCQs, solve/evaluate Q&As     |

Other Features:
- 📂 PDF upload (PyPDF2 extraction, with guards for very short/empty text)
- 📊 Lightweight usage logging for sessions and mode usage (CSV-based, privacy-friendly)
- 💬 Real-time chat interface
- 🔄 New chat/reset option
- ☁️ Deployed on Streamlit Cloud

---

## 🧙‍♂️ **Quizzer Mode — Three Powerful Sub-modes**

1. **📝 Generate Questions**  
   Enter a topic/chapter/passage. Get a variety of questions (MCQ, T/F, fill-in, descriptive) — answers listed together as an answer key for self-testing.
2. **📖 Solve Questions**  
   Paste your exam questions (optionally add word limits or marks). Get concise, exam-ready answers formatted per input.
3. **✅ Evaluate Answers**  
   Submit questions and your answers (with '---' separator, or sequential prompts). Get detailed feedback, correction, and scoring.

---

## 🧱 **Project Structure**

```
SGPA/
├── main.py
├── requirements.txt
├── assets/
│ └── PROBLEM STATEMENTS.pdf
├── components/
│ ├── chat_ui.py
│ ├── pdf_handler.py
│ └── sidebar.py
├── core/
│ ├── ai_utils.py
│ ├── explainer.py
│ ├── pdf_handler.py
│ ├── quizzer.py
│ └── summarizer.py
└── utils/
└── gemini_helper.py
```

---

## 🪜 **Workflow**
![SGPA Workflow](https://github.com/user-attachments/assets/2cdac27e-2ae1-4dcf-b339-3a63efcebbb3)
![SGPA System Architecture](https://github.com/user-attachments/assets/ae8f9a61-c84b-4ebf-9081-f139b98cf441)

---

## 📚 In-Repo User Guide (Quick Start)

You can keep the PDF as the detailed reference and mirror a concise, in-README guide here.

### 1️⃣ Getting Started

- Open the deployed app: `https://ai-powered-study-assistant-main.onrender.com/`
- Select a mode from the sidebar: **Explainer**, **Summarizer**, or **Quizzer**
- Provide input (topic, notes, PDF, or questions) in the main chat area

### 2️⃣ Mode Usage

- **Explainer**:  
  Type your concept or question (e.g., “Explain paging in OS for exams”).  
  SGPA returns a simple, exam-oriented explanation, plus an idea for a quick diagram you can sketch.

- **Summarizer**:  
  Upload a PDF or paste notes.  
  SGPA returns an exam-ready summary with headings, bullets, and practice questions.

- **Quizzer**:  
  - Use “Generate Questions” for practice questions with an answer key.  
  - Use “Solve Questions” to get answers to your questions.  
  - Use “Evaluate Answers” to paste both question and your answer to receive feedback and scoring.

### 3️⃣ Tips for Best Results

- Mention exam context (e.g., “for B.Tech 3rd sem OS viva”) for sharper responses.  
- Use follow-up prompts in the same chat to refine or extend answers.  
- Reset the chat using the “New Chat” / reset option before switching topics heavily.

---

## 💡 **Tech Stack**

| Category            | Technologies                             |
|---------------------|------------------------------------------|
| **Frontend**        | Streamlit                                |
| **Backend / AI**    | Google Gemini 2.5 Flash API              |
| **Language**        | Python                                   |
| **Libraries**       | PyPDF2, google-generativeai, streamlit, dotenv |
| **Deployment**      | Streamlit Community Cloud                |
| **Security**        | `.env` + `st.secrets` key handling       |

---

## 🧾 **Results**

- 🎯 Simple, modern, and interactive chat-based UI  
- 📑 Smart summarization, quiz generation, and answer evaluation  
- ⚡ Fast, context-aware AI with Gemini 2.5 Flash  
- 🧩 Smooth multi-mode workflow for study and revision

---

## 🚀 **Future Scope**

- 🗣️ Speech-to-text / text-to-speech interaction  
- 🌐 Multi-language explanations  
- 🧠 Flashcard & spaced-repetition support  
- 👤 Memory-based user personalization  
- ☁️ Drive/Notion integration for notes & sessions  

---

> 🧩 *“Integrating AI with Education — Making Learning Simpler, Smarter, and Accessible for All.”*

---

## 📜 Usage & Attribution

- You are welcome to **fork** this repository to learn from it or build your own version of SGPA.  
- If you deploy this project publicly or create a derivative version:
  - Keep the existing license file.  
  - Credit **“Yogesh Sheoran”**.  
  - Include a link back to the original repo:
    - https://github.com/yogeshsheoran01/AI-powered-Study-Assistant-main

For contributions, please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on forking, branching, and opening pull requests.

---

## 👨‍💻 Author

**Yogesh Sheoran**  
-- GitHub: [@yogeshsheoran01](https://github.com/yogeshsheoran01)

🌟 If you find this repository useful, please give it a star! 🌟

---
