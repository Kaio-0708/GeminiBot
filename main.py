from gettext import install
from re import U
import google
import pip
from google import generativeai
from pygments.lexers import q

!pip install -q -U google-generativeai

import google.generativeai as genai
from google.colab import userdata
api_key = userdata.get('SECRET_KEY')
genai.configure(api_key=api_key)

for m in genai.list_models():
    if 'generatContent' in m.supported_generation_methods:
        print(m.name)

generation_config = {
    "candidate_count":1,
    "temperature": 0.5,
}

safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings,)

response = model.generate_content("Que empresa criou o modelo de IA Gemini?")
print(response.text)

chat = model.start_chat(history=[])

prompt = input("Esperando prompt: ")

while prompt != "fim":
    response = chat.send_message(prompt)
    print("Resposta: ", response.text, "\n")
    prompt = input("Esperando prompt: ")

import textwrap
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#Imprimindo o histórico
for message in chat.history:
    display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))
    print('-------------------------------------------')
  
