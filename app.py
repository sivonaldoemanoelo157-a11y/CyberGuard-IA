

# 🛡️ BIBLIOTECA DE DETECÇÃO DO CYBERGUARD IA

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
    encontrados = []

    for categoria, palavras in biblioteca_golpes.items():
        for palavra in palavras:
            if palavra in mensagem:
                encontrados.append((categoria, palavra))

    return encontrados


def verificar_mensagem(mensagem):
    encontrados = analisar_mensagem(mensagem)

    categorias = set(
        categoria for categoria, palavra in encontrados
    )

    quantidade = len(categorias)

    if quantidade >= 3:
        risco = "ALTO"
    elif quantidade >= 1:
        risco = "MEDIO"
    else:
        risco = "BAIXO"

    if encontrados:
        motivos = [
            f"{categoria}: {palavra}"
            for categoria, palavra in encontrados
        ]

        return (
            "Mensagem suspeita!\n"
            f"Risco: {risco}\n"
            "Motivos encontrados:\n"
            + "\n".join(motivos)
        )

    return (
        "Nenhum termo suspeito encontrado.\n"
        "Risco: BAIXO"
    )


def testar_cyberguard():
    mensagens = [
        "Clique aqui para ganhar um prêmio falso!",
        "Sua conta foi bloqueada, confirme seus dados.",
        "Olá, tudo bem? Como foi seu dia?",
        "Acesse o link, envie o código e faça uma transferência urgente."
    ]

    print("CyberGuard IA iniciada!\n")

    for mensagem in mensagens:
        print("Mensagem:", mensagem)
        print("Resultado:", verificar_mensagem(mensagem))
        print("-" * 40)


if __name__ == "__main__":
    testar_cyberguard()
