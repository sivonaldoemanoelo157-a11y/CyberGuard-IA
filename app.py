

def analisar_mensagem(mensagem):
    palavras_suspeitas = [
        "senha",
        "pix",
        "urgente",
        "clique aqui",
        "prêmio",
        "premio",
        "código de verificação",
        "conta bloqueada",
        "conta foi bloqueada",
        "foi bloqueada",
        "confirmar dados",
        "confirme seus dados",
        "confirme seus dados imediatamente"
    ]

    mensagem = mensagem.lower()

    encontrados = [
        palavra for palavra in palavras_suspeitas
        if palavra in mensagem
    ]

    return encontrados


def verificar_mensagem(mensagem):
    encontrados = analisar_mensagem(mensagem)

    if encontrados:
        return (
            "⚠️ Mensagem suspeita! Termos encontrados: "
            + ", ".join(encontrados)
        )

    return "✅ Nenhum termo suspeito encontrado."


def testar_cyberguard():
    mensagens = [
        "Clique aqui para ganhar um prêmio!",
        "Sua conta foi bloqueada, confirme seus dados.",
        "Olá, tudo bem? Como foi seu dia?"
    ]

    print("🛡️ CyberGuard IA iniciada!\n")

    for mensagem in mensagens:
        print("Mensagem:", mensagem)
        print("Resultado:", verificar_mensagem(mensagem))
        print("-" * 40)


if __name__ == "__main__":
    testar_cyberguard()
