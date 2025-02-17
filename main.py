def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {
        "nome": nome_contato,
        "telefone": telefone_contato,
        "email": email_contato,
        "favorito": False,
    }
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionada com sucesso!")
    return


def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = " ★ " if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(
            f"{indice}. [{status}] {nome_contato} | telefone: {telefone_contato} | email: {email_contato}"
        )
    return


def ver_contatos_favoritos(contatos):
    print("\nLista de contatos favoritos:")
    favoritos = [contato for contato in contatos if contato["favorito"]]
    for indice, contato in enumerate(favoritos, start=1):
        print(
            f'{indice}.[ ★ ] {contato["nome"]} | {contato["telefone"]} | {contato["email"]}'
        )
    return


def editar_contato(
    contatos,
    indice_contato,
    novo_nome_contato,
    novo_telefone_contato,
    novo_email_contato,
):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
        print(
            f"Contato {indice_contato} atualizada para {novo_nome_contato} | {novo_telefone_contato} | {novo_email_contato}"
        )
    else:
        print("Índice de contatos inválido.")
    return


def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} marcado como favorito")
    return


def desmarcar_contato_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = False
    print(f"Contato {indice_contato} marcado como favorito")
    return


def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato = contatos[indice_contato_ajustado]
        contatos.remove(contato)
        print(f"Contato {indice_contato} deletado com sucesso")
    else:
        print("Indice do contato inválido.")
    return


contatos = []
while True:
    print("\nMenu do Gerenciador de Lista de contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Favoritar contato")
    print("5. Desmarcar contato favorito")
    print("6. Ver contatos favoritos")
    print("7. Deletar contato")
    print("8. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input("Digite o telefone do contato que deseja adicionar: ")
        email_contato = input("Digite o email do contato que deseja adicionar: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("\nDigite o número do contato que deseja atualizar: ")
        novo_contato = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        editar_contato(
            contatos, indice_contato, novo_contato, novo_telefone, novo_email
        )

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número da contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = input(
            "Digite o número da contato que deseja desmarcar como favorito: "
        )
        desmarcar_contato_favorito(contatos, indice_contato)

    elif escolha == "6":
        ver_contatos_favoritos(contatos)

    elif escolha == "7":
        ver_contatos(contatos)
        indice_contato = input("Digite o número da contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)

    elif escolha == "8":
        break
