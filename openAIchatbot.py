import os
from dotenv import load_dotenv
import openai
import gradio as gr


openai.api_key = os.getenv("OPENAI_API_KEY")
# Initialize the conversation with a system message
messages = [{"role": "system", "content": "You are a helpful assistant."}]

def chatbot(input_text):
    # Add the user input to the conversation history
    messages.append({"role": "user", "content": input_text})
    
    try:
        # Call the ChatCompletion API using gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        # Retrieve the assistant's response
        chatbot_response = response["choices"][0]["message"]["content"]
        # Add the assistant's response to the conversation history
        messages.append({"role": "assistant", "content": chatbot_response})
        return chatbot_response
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Create and launch the Gradio interface
demo = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="OpenAI Chatbot",
    description="Chat with the OpenAI Chatbot!"
)
demo.launch()
