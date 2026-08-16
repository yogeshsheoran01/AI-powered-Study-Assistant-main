# 📘 **AI-Powered Study Assistant**

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

**AI-Powered Study Assistant** is an AI-powered web application that acts as a personal academic assistant, capable of:

* 🧩 Explaining complex concepts in simple terms
* 📄 Summarizing notes or uploaded PDFs
* ❓ Generating quizzes
* 📝 Solving exam questions
* ✅ Evaluating answers and providing feedback

The application combines **Streamlit** for the user interface and **Google Gemini 2.5 Flash API** for fast and intelligent AI responses in a clean, chat-based interface.

---

## 🆕 **Recent Updates — v1.2.0**

* Explainer now suggests simple sketchable diagrams for visual understanding.
* Summarizer handles very short or scanned PDFs more safely with clearer warnings.
* Added lightweight, privacy-friendly usage analytics for anonymous sessions and mode usage.

---

## ⚙️ **System Design**

### 🏗️ **Architecture**

A lightweight **Streamlit frontend** interacts with the **Google Gemini 2.5 Flash API** through secure API calls.

All secrets are managed safely via `.env` and `st.secrets`.

### 🧩 **Core Features**

| Mode              | Function                          | Example                      |
| ----------------- | --------------------------------- | ---------------------------- |
| 🧠 **Explainer**  | Simplifies academic concepts      | "Explain Deadlock in OS"     |
| 📄 **Summarizer** | Condenses notes or PDFs           | Upload 20-page PDF → Summary |
| 🧩 **Quizzer**    | Quiz generator, solver, evaluator | MCQs, solve/evaluate Q&As    |

### Other Features

* 📂 PDF upload using PyPDF2
* 📊 Lightweight usage logging for anonymous sessions
* 💬 Real-time chat interface
* 🔄 New chat/reset option
* ☁️ Deployed on Render

---

## 🧙‍♂️ **Quizzer Mode — Three Powerful Sub-Modes**

### 1. 📝 Generate Questions

Enter a topic, chapter, or passage and get a variety of questions:

* MCQ
* True/False
* Fill-in-the-blanks
* Descriptive questions

Answers are provided together as an answer key for self-testing.

### 2. 📖 Solve Questions

Paste your exam questions and optionally add word limits or marks.

Get concise, exam-ready answers formatted according to the input.

### 3. ✅ Evaluate Answers

Submit questions and your answers.

Get:

* Detailed feedback
* Corrections
* Scoring
* Suggestions for improvement

---

## 🧱 **Project Structure**

```text
AI-powered-Study-Assistant/
├── main.py
├── requirements.txt
├── assets/
│   └── PROBLEM STATEMENTS.pdf
├── components/
│   ├── chat_ui.py
│   ├── pdf_handler.py
│   └── sidebar.py
├── core/
│   ├── ai_utils.py
│   ├── explainer.py
│   ├── pdf_handler.py
│   ├── quizzer.py
│   └── summarizer.py
└── utils/
    └── gemini_helper.py
```

---

## 🪜 **Workflow**

![AI Study Assistant Workflow](https://github.com/user-attachments/assets/2cdac27e-2ae1-4dcf-b339-3a63efcebbb3)

![AI Study Assistant System Architecture](https://github.com/user-attachments/assets/ae8f9a61-c84b-4ebf-9081-f139b98cf441)

### 🔄 Workflow

```text
User
  │
  ▼
Streamlit Web Interface
  │
  ├──────────────┬──────────────┐
  ▼              ▼              ▼
Explainer    Summarizer      Quizzer
  │              │              │
  └──────────────┴──────────────┘
                 │
                 ▼
       Google Gemini 2.5 Flash
                 │
                 ▼
          AI Generated Result
                 │
                 ▼
              User
```

---

## 📚 **User Guide**

### 1️⃣ Getting Started

Open the deployed application:

**https://ai-powered-study-assistant-main.onrender.com/**

Then:

1. Open the application.
2. Select a mode from the sidebar.
3. Choose **Explainer**, **Summarizer**, or **Quizzer**.
4. Enter your topic, notes, PDF, or questions.
5. Get your AI-generated response.

### 2️⃣ Mode Usage

#### 🧠 Explainer

Type your concept or question.

Example:

> Explain paging in OS for exams.

The AI provides a simple, exam-oriented explanation and can suggest a quick diagram you can sketch.

#### 📄 Summarizer

Upload a PDF or paste notes.

The AI generates an exam-ready summary with:

* Headings
* Key points
* Important concepts
* Practice questions

#### 🧩 Quizzer

* **Generate Questions** → Generate practice questions with an answer key.
* **Solve Questions** → Get answers to your questions.
* **Evaluate Answers** → Submit questions and answers to receive feedback and scoring.

### 3️⃣ Tips for Best Results

* Mention the subject and topic.
* Mention your exam level.
* Specify marks or word limits.
* Use follow-up prompts to refine the response.
* Reset the chat before switching to a completely different topic.

Example:

> Explain Deadlock in Operating Systems for a B.Tech 10-mark exam answer.

---

## 💡 **Tech Stack**

| Category            | Technologies                                          |
| ------------------- | ----------------------------------------------------- |
| **Frontend**        | Streamlit                                             |
| **Backend / AI**    | Google Gemini 2.5 Flash API                           |
| **Language**        | Python                                                |
| **Libraries**       | PyPDF2, google-generativeai, streamlit, python-dotenv |
| **Deployment**      | Render                                                |
| **Security**        | `.env` + `st.secrets`                                 |
| **Version Control** | Git & GitHub                                          |

---

## 🧾 **Results**

* 🎯 Simple, modern, and interactive chat-based UI
* 📑 Smart summarization, quiz generation, and answer evaluation
* ⚡ Fast, context-aware AI with Gemini 2.5 Flash
* 🧩 Smooth multi-mode workflow for study and revision

---

## 🚀 **Future Scope**

* 🗣️ Speech-to-text / text-to-speech interaction
* 🌐 Multi-language explanations
* 🧠 Flashcard & spaced-repetition support
* 👤 Memory-based user personalization
* 📊 Student performance analytics
* ☁️ Drive/Notion integration for notes and sessions
* 📱 Improved mobile experience
* 🔔 Study reminders

---

## 🌐 **Live Application**

🚀 **Try the AI-Powered Study Assistant:**

https://ai-powered-study-assistant-main.onrender.com/

---

## 📂 **GitHub Repository**

💻 **Source Code:**

https://github.com/yogeshsheoran01/AI-powered-Study-Assistant-main

---

## 📜 **License**

This project is licensed under the **MIT License**.

See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 **Author**

**Yogesh Sheoran**

* GitHub: [@yogeshsheoran01](https://github.com/yogeshsheoran01)

---

> 🧩 *"Integrating AI with Education — Making Learning Simpler, Smarter, and Accessible for All."*

---

⭐ **If you find this project useful, please give it a star!** ⭐
