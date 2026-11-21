
# CYBERGUARD IA - ETAPA 6
# DETECCAO MELHORADA DE GOLPES

import unicodedata

biblioteca_golpes = {
    "Roubo de dados": [
        "senha",
        "codigo de verificacao",
        "confirmar dados",
        "confirme seus dados",
        "envie o codigo",
        "codigo recebido",
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
        "clique aqui",
        "acesse o link",
        "link de confirmacao",
        "link para atualizar",
        "acesse agora"
    ],
    "Falsas urgencias": [
        "urgente",
        "conta bloqueada",
        "conta foi bloqueada",
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


def analisar_mensagem(mensagem):
    mensagem_normalizada = normalizar(mensagem)
    encontrados = {}

    for categoria, palavras in biblioteca_golpes.items():
        for palavra in palavras:
            if palavra in mensagem_normalizada:
                if categoria not in encontrados:
                    encontrados[categoria] = []

                encontrados[categoria].append(palavra)

    return encontrados


def verificar_mensagem(mensagem):
    encontrados = analisar_mensagem(mensagem)
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

        for categoria, palavras in encontrados.items():
            resultado += f"\n{categoria}:\n"

            for palavra in palavras:
                resultado += f"- {palavra}\n"
    else:
        resultado = (
            "Nenhum termo suspeito encontrado.\n"
            "Risco: BAIXO"
        )

    return risco, resultado


def mostrar_historico():
    if not historico:
        print("\nNenhuma analise registrada.")
        return

    print("\nHISTORICO DE ANALISES")

    for numero, registro in enumerate(historico, start=1):
        print(f"\nAnalise {numero}")
        print(f"Mensagem: {registro['mensagem']}")
        print(f"Risco: {registro['risco']}")

    print("-" * 40)


def iniciar_cyberguard():
    print("CYBERGUARD IA - ETAPA 6")
    print("Digite 'historico' para consultar.")
    print("Digite 'limpar' para apagar o historico.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        mensagem = input("Digite ou cole uma mensagem: ")
        comando = mensagem.lower().strip()

        if comando == "sair":
            print("CyberGuard IA encerrado.")
            break

        if comando == "historico":
            mostrar_historico()
            continue

        if comando == "limpar":
            historico.clear()
            print("Historico apagado!")
            continue

        if not mensagem.strip():
            print("Digite uma mensagem para analisar.\n")
            continue

        risco, resultado = verificar_mensagem(mensagem)

        historico.append({
            "mensagem": mensagem,
            "risco": risco
        })

        print("\nResultado da analise:")
        print(resultado)
        print("-" * 40)


if __name__ == "__main__":
    iniciar_cyberguard()
