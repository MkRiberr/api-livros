from flask import Flask, jsonify
import os

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Sophia"},
    {"id": 2, "nome": "Lacerda"},
    {"id": 3, "nome": "Maxwell"},
]

@app.route("/alunos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Alunos - Acesse /alunos"})

@app.route("/", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)