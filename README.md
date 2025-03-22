
# Personal AI Chatbot

A real-time conversational AI built with Python, OpenAI's gpt-3.5-turbo model, and Gradio. This project demonstrates how to build a context-aware chatbot with an interactive web interface while securely managing sensitive data via environment variables.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview
**Personal AI Chatbot** uses OpenAI’s ChatCompletion API to generate responses and Gradio to provide a user-friendly interface. By storing the conversation history, it offers context-aware replies that feel more natural and coherent.

## Features
- **Real-Time Interaction:** Chat with the bot through a web interface powered by Gradio.  
- **Context-Aware Responses:** Maintains conversation history to deliver coherent, context-rich answers.  
- **Secure API Key Management:** Uses environment variables to protect sensitive data like API keys.  
- **Lightweight & Easy to Deploy:** Minimal dependencies for quick setup and usage.

## Prerequisites
- **Python** 3.7 or higher  
- An active **OpenAI API key**  
- Internet connection (to access the OpenAI API)

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YourUsername/Personal-AI-Chatbot.git
   cd Personal-AI-Chatbot
   ```


2. **Install Dependencies:**
   ```bash
   pip install openai gradio python-dotenv
   ```

## Setup
1. **Create a `.env` File:**

   In the project’s root folder, create a file named `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. **Ignore the `.env` File in Git:**

   Make sure `.env` is listed in your `.gitignore` to prevent accidental commits:
   ```
   .env
   ```

## Usage
1. **Run the Chatbot Script:**
   ```bash
   python <script_name>.py
   ```
   Replace `<script_name>.py` with the actual name of your script (e.g., `app.py`).

2. **Open the Gradio Interface:**
   - After running the script, Gradio will display a local URL (e.g., `http://127.0.0.1:7860`).
   - Open this URL in your browser to start chatting with the AI.

## Project Structure
```
Personal-AI-Chatbot/
├── README.md              # This file
├── <script_name>.py       # Main chatbot script
├── .env                   # (Optional) File for storing your API key
├── .gitignore             # File to ignore .env and other sensitive files
└── requirements.txt       # (Optional) List of project dependencies

