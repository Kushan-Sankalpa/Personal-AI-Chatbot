import openai
import gradio

openai.api_key = "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"

messages = [{ "role": "system", "content": "You are a helpful assistant." }]

def chatbot(input_text):