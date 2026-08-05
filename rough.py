import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel("models/gemini-3.5-flash")

prompt = "Explain how a neural network learns weights."
response = model.generate_content(prompt)

print(response.text)