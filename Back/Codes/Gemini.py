import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
#from google.colab import userdata

from IPython.display import display
from IPython.display import Markdown

import PIL.Image

img = PIL.Image.open('E:\\Projetos\\GitHub\\Pythonando\\Back\\Codes\\x-ray.jpg')
img

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key='AIzaSyC0zUAhggPNjPnx3QMVD7-MpGfgIwBDAwI')

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro-vision')
texto=""
while(texto!='s'):
  print("Digite uma pergunta:")
  texto = input()
  response = model.generate_content([texto, img], stream=True)
  response.resolve()
  print("------")
  print(response.text)
  print("------")
