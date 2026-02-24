usuarios = []


def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu email: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)
    print("\nCadastro completo!\n")


def listar_usuarios():
    if len(usuarios) == 0:
        print("\nNenhum usuário cadastrado!\n")
        return

    print("\nLista de usuários:\n")

    for i, user in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {user['nome']}")
        print(f"   Idade: {user['idade']}")
        print(f"   Email: {user['email']}\n")


def menu():
    while True:
        print("SISTEMA DE CADASTRO")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            print("\nFechando o sistema...")
            break

        else:
            print("\nOpção inválida!\n")


menu()