import os
from dotenv import load_dotenv

# Load local .env for development (won't affect deployed env vars)
load_dotenv()
MODEL = "models/gemini-3.5-flash"
api_configured = False
_config_error = ""


def _get_api_key() -> str | None:
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        return api_key

    try:
        import streamlit as st
        return st.secrets.get("GEMINI_API_KEY")
    except Exception:
        return None


def _configure_api() -> None:
    global api_configured, _config_error
    try:
        import google.genai as genai
    except ImportError:
        try:
            import google.generativeai as genai
        except ImportError as e:
            api_configured = False
            _config_error = (
                "Gemini client package is not installed. "
                "Install `google-genai` or `google-generativeai` in your environment."
            )
            return

    api_key = _get_api_key()
    if not api_key:
        api_configured = False
        _config_error = "GEMINI_API_KEY not set in environment or Streamlit secrets."
        return

    try:
        genai.configure(api_key=api_key)
        api_configured = True
        _config_error = ""
    except Exception as e:
        api_configured = False
        _config_error = str(e)


_configure_api()


def generate_response(prompt: str) -> str:
    """Generate response from Gemini model or return a helpful error if not configured."""
    if not api_configured:
        return (
            "❌ Gemini API not configured. Set GEMINI_API_KEY in a local `.env` file "
            "or in Streamlit secrets (`st.secrets['GEMINI_API_KEY']`).\n\n"
            f"Details: {_config_error}"
        )
    try:
        try:
            import google.genai as genai
        except ImportError:
            import google.generativeai as genai
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text.strip() if response and getattr(response, "text", None) else "⚠️ No response generated."
    except Exception as e:
        return f"❌ Error generating response: {e}"
