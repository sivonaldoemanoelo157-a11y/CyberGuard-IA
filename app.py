
# CYBERGUARD IA - ETAPA 4

biblioteca_golpes = {
    "Roubo de dados": [
        "senha",
        "código de verificação",
        "confirmar dados",
        "confirme seus dados",
        "envie o código",
        "código recebido"
    ],

    "Golpes financeiros": [
        "prêmio falso",
        "ganhe dinheiro fácil",
        "transferência urgente",
        "pix premiado"
    ],

    "Links suspeitos": [
        "clique aqui",
        "acesse o link",
        "link de confirmação",
        "link para atualizar"
    ],

    "Falsas urgências": [
        "urgente",
        "conta bloqueada",
        "conta foi bloqueada",
        "ação imediata",
        "última oportunidade"
    ]
}


def analisar_mensagem(mensagem):
    mensagem = mensagem.lower()
    encontrados = {}

    for categoria, palavras in biblioteca_golpes.items():
        for palavra in palavras:
            if palavra in mensagem:
                if categoria not in encontrados:
                    encontrados[categoria] = []

                if palavra not in encontrados[categoria]:
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

        return resultado

    return (
        "Nenhum termo suspeito encontrado.\n"
        "Risco: BAIXO"
    )


def iniciar_cyberguard():
    print("CYBERGUARD IA")
    print("Analisador de mensagens iniciado!")
    print("Digite 'sair' para encerrar.\n")

    while True:
        mensagem = input("Digite ou cole uma mensagem: ")

        if mensagem.lower().strip() == "sair":
            print("CyberGuard IA encerrado.")
            break

        if not mensagem.strip():
            print("Digite uma mensagem para analisar.\n")
            continue

        resultado = verificar_mensagem(mensagem)

        print("\nResultado da análise:")
        print(resultado)
        print("-" * 40)


if __name__ == "__main__":
    iniciar_cyberguard()
