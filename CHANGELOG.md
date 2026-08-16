# 🧾 CHANGELOG

**Project:** AI-Powered Study Assistant  
**Repository:** https://github.com/yogeshsheoran01/AI-powered-Study-Assistant-main

**Last Updated:** 16th August 2026

---

## 🆕 Version 1.2.0 — Visual + Analytics + UI Refresh (January 2026)

### ✨ New Features & Improvements

- **Visual Explanations in Explainer**
  - Explainer responses now include a simple, sketchable diagram idea at the end of each explanation.
  - Diagrams are described in text so students can quickly draw them in notebooks during revision or exams.

- **Summarizer PDF Handling Fixes**
  - Added a stronger short-text guard for PDF summarization.
  - Clear warning message when extracted text is too short or likely from scanned/image-based PDFs.
  - Improved handling of real-world PDFs and scanned documents.

- **Lightweight Usage Analytics**
  - Implemented privacy-friendly interaction logging to a local CSV file.
  - Each interaction records:
    - Timestamp
    - Anonymous session ID
    - Mode
    - Sub-mode
    - PDF usage flag
    - Prompt length
    - Response length
  - Enables analysis of:
    - Total interactions
    - Approximate study sessions
    - Mode usage distribution
    - PDF-based study patterns

- **Branding & UI Updates**
  - Updated the application branding to **AI-Powered Study Assistant**.
  - Improved the application header and overall UI.
  - Added a custom Streamlit theme for a more polished and student-friendly experience.

### 🛠️ Internal & Maintenance

- Ensured analytics logging is fail-safe so logging errors do not break the application.
- Normalized asset paths and filenames for reliable deployment.
- Cleaned up `.gitignore` and configuration files.
- Improved configuration consistency between local development and deployment environments.

---

## 🆕 Version 1.1.0 — Major Feature Update (November 2025)

### ✨ New Features & Improvements

- **Quizzer Mode Expanded**
  - Added three sub-modes:
    - 📝 **Generate Questions** — MCQ, T/F, Fill in the Blanks, and Descriptive questions with an answer key.
    - 📖 **Solve Questions** — Exam-style answers adapted to marks and word limits.
    - ✅ **Evaluate Answers** — Automated feedback, scoring, corrections, and improvement tips.
  - Answer keys are displayed at the end of generated quizzes.

- **Context-Aware Chat**
  - Improved support for follow-up questions using previous chat history across all modes.

- **Dynamic Sidebar**
  - Added nested options for Quizzer actions.
  - Improved navigation and mode selection.
  - Added links for the GitHub repository and user documentation.

- **User Help Documentation**
  - Added a quick-start guide covering:
    - Sample inputs
    - Usage tips
    - Input formats
    - Troubleshooting
    - Application walkthrough

- **Refined Prompts & Outputs**
  - Improved exam-oriented summaries.
  - Improved answer formatting.
  - Added Markdown-friendly responses.
  - Improved adaptive answer length based on marks and word limits.

- **UI/UX Enhancements**
  - Improved code block outputs.
  - Added one-click copy functionality where applicable.
  - Added information banners for mode guidance.
  - Added response feedback functionality.

- **Performance & Stability**
  - Improved API error and timeout handling.
  - Added input limits for large notes and PDFs.
  - Improved new-chat behavior and notifications.

### 🛠️ Other Updates

- Streamlined project structure and modularized components.
- Improved AI prompt logic for clearer and more exam-ready responses.
- Improved handling of user options and input formats.
- Added foundations for future features including speech support, flashcards, login, notes, and multilingual support.

---

## 🏁 Version 1.0.0 — Initial Release (October 2025)

### ✅ Initial Features

- 🧠 **AI Chat Modes**
  - Explainer
  - Summarizer
  - Quizzer

- 📄 **PDF Upload & Summarization**
  - PyPDF2-based PDF text extraction
  - PDF summarization using Google Gemini

- 💬 **Streamlit Chat Interface**
  - Interactive chat UI
  - Sidebar navigation
  - New chat/reset functionality

- 🤖 **Google Gemini 2.5 Flash API**
  - AI-powered responses
  - Secure API integration

- 🔐 **Secure API Key Handling**
  - `.env`
  - Streamlit secrets

- 🚀 **Deployment**
  - Deployed on Render

- 🧱 **Modular Project Structure**
  - Core modules
  - Components
  - Utilities
  - Assets

---

## 🚀 Future Development

Planned improvements include:

- 🗣️ Speech-to-text and text-to-speech
- 🌐 Multilingual explanations
- 🧠 Flashcard generation
- 🔁 Spaced repetition
- 💾 Persistent chat memory
- 👤 User authentication
- 📝 Personal notes and study storage
- 📊 Student performance analytics
- 🎨 Further UI/UX improvements
- ☁️ Cloud-based study data storage

---

## 🌐 Live Application

https://ai-powered-study-assistant-main.onrender.com/

---

## 📂 Repository

https://github.com/yogeshsheoran01/AI-powered-Study-Assistant-main

---

> 🚀 **AI-Powered Study Assistant — Making Learning Simpler, Smarter, and More Accessible.**
