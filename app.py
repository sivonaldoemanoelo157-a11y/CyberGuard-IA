
# CYBERGUARD IA - ETAPA 5
# HISTORICO DE ANALISES

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

historico = []


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
    else:
        resultado = (
            "Nenhum termo suspeito encontrado.\n"
            "Risco: BAIXO"
        )

    return risco, resultado


def mostrar_historico():
    if not historico:
        print("\nNenhuma análise registrada.")
        return

    print("\nHISTÓRICO DE ANÁLISES")

    for numero, registro in enumerate(historico, start=1):
        print(f"\nAnálise {numero}")
        print(f"Mensagem: {registro['mensagem']}")
        print(f"Risco: {registro['risco']}")

    print("-" * 40)


def iniciar_cyberguard():
    print("CYBERGUARD IA - ETAPA 5")
    print("Digite 'historico' para consultar.")
    print("Digite 'limpar' para apagar o histórico.")
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
            print("Histórico apagado!")
            continue

        if not mensagem.strip():
            print("Digite uma mensagem para analisar.\n")
            continue

        risco, resultado = verificar_mensagem(mensagem)

        historico.append({
            "mensagem": mensagem,
            "risco": risco
        })

        print("\nResultado da análise:")
        print(resultado)
        print("-" * 40)


if __name__ == "__main__":
    iniciar_cyberguard()
