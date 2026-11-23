
from flask import Flask, request, jsonify
from flask_cors import CORS
import unicodedata

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": [
            "https://sivonaldoemanoelo157-a11y.github.io"
        ]
    }
})

biblioteca_golpes = {
    "Roubo de dados": [
        "informe sua senha",
        "envie sua senha",
        "confirme seus dados",
        "codigo de verificacao",
        "envie o codigo",
        "dados bancarios",
        "informacoes pessoais"
    ],
    "Golpes financeiros": [
        "premio falso",
        "ganhe dinheiro facil",
        "transferencia urgente",
        "pix premiado",
        "dinheiro gratis",
        "emprestimo aprovado"
    ],
    "Links suspeitos": [
        "clique aqui para confirmar",
        "acesse o link de confirmacao",
        "link para atualizar seus dados",
        "acesse agora para receber"
    ],
    "Falsas urgencias": [
        "sua conta foi bloqueada",
        "conta sera bloqueada",
        "acao imediata",
        "ultima oportunidade",
        "sua conta sera encerrada"
    ]
}

historico = []


def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)

    return "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )


def verificar_mensagem(mensagem):
    texto = normalizar(mensagem)
    encontrados = {}

    for categoria, frases in biblioteca_golpes.items():
        for frase in frases:
            if frase in texto:
                encontrados[categoria] = [frase]

    quantidade = len(encontrados)

    if quantidade >= 3:
        risco = "ALTO"
    elif quantidade == 2:
        risco = "MEDIO"
    elif quantidade == 1:
        risco = "ATENCAO"
    else:
        risco = "BAIXO"

    if encontrados:
        resultado = "Sinais suspeitos encontrados!\n"
        resultado += f"Risco: {risco}\n"
        resultado += "Motivos encontrados:\n"

        for categoria, frases in encontrados.items():
            resultado += f"\n{categoria}:\n"
            for frase in frases:
                resultado += f"- {frase}\n"
    else:
        resultado = (
            "Nenhum sinal conhecido foi encontrado.\n"
            "Risco: BAIXO\n"
            "Isso nao garante que a mensagem seja segura."
        )

    return risco, resultado, encontrados


@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "status": "online",
        "projeto": "CyberGuard IA"
    })


@app.route("/analisar", methods=["POST"])
def analisar():
    dados = request.get_json(silent=True) or {}
    mensagem = dados.get("mensagem", "")

    if not isinstance(mensagem, str) or not mensagem.strip():
        return jsonify({
            "erro": "Envie uma mensagem valida para analisar."
        }), 400

    risco, resultado, encontrados = verificar_mensagem(mensagem)

    registro = {
        "mensagem": mensagem,
        "risco": risco
    }

    historico.insert(0, registro)

    return jsonify({
        "risco": risco,
        "resultado": resultado,
        "categorias": encontrados,
        "historico": historico[:20]
    })


@app.route("/historico", methods=["GET"])
def consultar_historico():
    return jsonify(historico[:20])


@app.route("/historico", methods=["DELETE"])
def limpar_historico():
    historico.clear()
    return jsonify({
        "mensagem": "Historico apagado com sucesso."
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
