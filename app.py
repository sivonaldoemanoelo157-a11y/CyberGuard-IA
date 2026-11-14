

def analisar_mensagem(mensagem):
    suspeitas = [
        "senha",
        "pix",
        "clique aqui",
        "prêmio",
        "urgente",
        "código de verificação"
    ]

    mensagem = mensagem.lower()

    encontrados = [
        palavra for palavra in suspeitas
        if palavra in mensagem
    ]

    if encontrados:
        print("ATENÇÃO: mensagem suspeita!")
        print("Termos encontrados:", encontrados)
    else:
        print("Nenhum termo suspeito encontrado.")

print("CyberGuard IA iniciada!")

mensagem = input("Digite uma mensagem para analisar: ")
analisar_mensagem(mensagem)
    mensagem = mensagem.lower()
    palavras_suspeitas = ["senha", "pix", "urgente", "clique aqui", "prêmio"]
    

            if palavra in mensagem:
                        return True    
            return False
            def verificar_mensagem(mensagem):
                    if analisar_mensagem(mensagem):
                            return "⚠️ Mensagem suspeita!"
                                return "✅ Mensagem aparentemente segura."
                                
