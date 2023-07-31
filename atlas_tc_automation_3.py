# --------------------------------------------------------------
# PROJECT BILLABLE HOURS DAYS
# --------------------------------------------------------------

import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv
import openai

# Load API key
load_dotenv(find_dotenv())

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# assign model id
model_id = 'gpt-4'

def chatgpt_conversation(conversation_Log):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation_Log
    )
    print(response)  # print the response object

    # extract the role and content from the response message
    role = response.choices[0].message['role']
    content = response.choices[0].message['content']
    
    conversation_Log.append({
        'role': role.strip(),
        'content': content.strip(),
    })
    return conversation_Log  # get the convo log

conversations = []
# roles = system, user, assistant
conversations.append({
    'role': 'system', 
    'content': 'Hey sudz, I am a ServiceNow Certified Master Architect Assistant.'
})
conversations = chatgpt_conversation(conversations)

while True:
    prompt = input('User:')
    conversations.append({'role': 'user', 'content': prompt})
    conversations = chatgpt_conversation(conversations)
    print(conversations)
    print()
    print('{0}: {1}\n'.format(conversations[-1]['role'].strip(), conversations[-1]['content'].strip()))
    if conversations[-1]['content'].strip() == 'Bye':
        break
    