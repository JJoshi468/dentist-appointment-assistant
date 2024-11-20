import os
import re
from langchain.prompts import PromptTemplate
from langchain_cohere import ChatCohere
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from config import *

# Set Cohere API key
os.environ["COHERE_API_KEY"] = key

# Defining the template
template = """
You are an excellent dentist appointment booking assistant who gives short and precise answers. Communicate in a natural way. Ask the user for the appointment details like name, date and time.
You can refer the given example conversation scenario and conversation history as context. Return only the response as a string.
Use the last confimation line format given in the example, everytime.

User: {input}
Assistant:

**Conversation history**:
{history}

**Example Conversation**:

User: Hi, I would like to book an appointment.
Assistant: Sure can I get your name and when would you like to book the appointment?
User: yes, its {{name}}.
Assistant: ok {{name}}, can i get the date and time ?
User: can you schedule on {{date}} at {{time}}?
Assistant: Alright, booking your appointment for {{name2}} on {{date}} at {{time}} is... Done! Your appointment is confirmed.
User: Thank you.
"""

prompt = PromptTemplate(input_variables=["input", "history"], template=template)

# Initialize Cohere LLM
cohere_llm = ChatCohere(model="command-r-plus", temperature=0)

# Add memory to chain
memory = ConversationBufferMemory(memory_key="history", input_key="input")

# Create the conversation chain
conversation = ConversationChain(
    llm=cohere_llm,
    prompt=prompt,
    memory=memory
)

# Dictionary to store appointment details
appointment_details = {}

def booking_assistant():
    print("Hi, this is your Appointment Booking Assistant!")

    while True:
        user_input = input("User: ")
        if 'thank' in user_input.lower():
            print("Assistant: Goodbye! Have a great day.")
            break
        resp = conversation.invoke(user_input)
        
        print("Assistant: "+resp['response'])
    extract_details(resp['response'], appointment_details)

# function to get date and time details to feed into dictionary
def extract_details(response, appointment_details):
    """
    Extracting details from the assistant's response and updating the appointment dictionary.
    """
    
    # Define patterns for extracting details
    # Regex patterns
    date_pattern = r"\b\d{1,2}(?:st|nd|rd|th)?\s+(?:of\s+)?(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\b|\b\d{1,2}\s+(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
    time_pattern = r"\b(?:1[0-2]|[1-9])\s?(?:a\.?m\.?|p\.?m\.?)\b"  # Capture time
    # Extract details
    date_match = re.search(date_pattern, response)
    time_match = re.search(time_pattern, response)

    if date_match:
        appointment_details['date'] = date_match.group(0)  # Group 0 returns the full match
    if time_match:
        appointment_details['time'] = time_match.group(0)
        
    print(appointment_details)
    return appointment_details


if __name__ == "__main__":
    booking_assistant()
