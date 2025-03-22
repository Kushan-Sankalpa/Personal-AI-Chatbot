import openai
import gradio as gr

# Set your OpenAI API key (keep it secure and do not expose it publicly)
openai.api_key = "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"
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
