from flask import Flask,render_template, request, Response
from openai import OpenAI
from dotenv import load_dotenv
import os

from components.bot import bot
from helpers import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

app = Flask(__name__)
app.secret_key = 'alura'

contexto = carrega("dados/ecomart.txt")

@app.route('/chat', methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt, cliente, modelo, contexto)
    texto_resposta = resposta.choices[0].message.content
    return texto_resposta

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
