# Dentist Appointment Booking Assistant

A simple appointment scheduling ai conversational agent that helps users book dental appointments using the Cohere LLM API and LangChain framework.

## Features

- Interactive chat interface for appointment booking
- Conversation memory to maintain context
- Natural language processing using Cohere's command-xlarge-nightly model
- Simple and intuitive user interface built with Streamlit

## Prerequisites

- Python 3.8 or higher
- Cohere API key
- Required Python packages (see Installation section)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/JJoshi468/dentist-appointment-assistant.git
cd dentist-appointment-assistant
```

2. Install required packages:
```bash
pip install langchain langchain-cohere python-dotenv
```

3. Create a `config.py` file in the project root and add your Cohere API key:
```python
key = "your-cohere-api-key-here"
```

## Project Structure

```
dentist-appointment-assistant/
├── app.py             # Main application file
├── config.py          # Configuration file with API key
└── README.md          # This file
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Start chatting with the assistant to book your appointment

Example conversation:
```
User: Hi, I would like to book an appointment.
Assistant: Sure, can you provide the date and time for the appointment?
User: Book on 13 Dec at 2 PM
Assistant: Booking your appointment for 13th December at 2 PM... Done! Your appointment is confirmed.
```

## Features Explanation

### Conversation Memory
The application uses `ConversationBufferMemory` to maintain context throughout the conversation, allowing for more natural interactions.

### Prompt Template
The assistant uses a predefined template that includes:
- Role definition (dentist appointment booking assistant)
- Example conversation flow
- Conversation history


## Configuration

The application requires a Cohere API key. You can obtain one by:
1. Creating an account at [Cohere](https://cohere.ai/)
2. Generating an API key in your dashboard
3. Adding the key to your `config.py` file


## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web interface framework
- [LangChain](https://python.langchain.com/) for the conversation chain implementation
- [Cohere](https://cohere.ai/) for the LLM API

