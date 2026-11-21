from collections import deque
leitores = []
fila_reservas = deque()
pilha_devolucoes = []
arvore_livros = {}
def cadastrar_leitor():
    id_novo = input("Digite o ID do leitor: ")

    for leitor in leitores:
        if leitor["id"] == id_novo:
            print("Já existe um leitor com esse ID!")
            return

    leitor = {
        "id": id_novo,
        "nome": input("Digite o nome do leitor: "),
        "cpf": input("Digite o CPF do leitor: "),
        "telefone": input("Digite o telefone do leitor: "),
        "endereço": input("Digite o endereço do leitor: "),
        "atividade": True
    }

    leitores.append(leitor)
    print("Leitor cadastrado com sucesso!")


def listar_leitores():
    if len(leitores) == 0:
        print("Nenhum leitor cadastrado.")
    else:
        print("\nLEITORES CADASTRADOS")

        for leitor in leitores:
            if leitor["atividade"]:
                status = "Ativo"
            else:
                status = "Inativo"

            print("\nID:", leitor["id"],"\nNome:", leitor["nome"],"\nCPF:", leitor["cpf"],"\nTelefone:", leitor["telefone"],"Endereço:", leitor["endereço"],"Situação:", status)

def pesquisar_leitor():
    pesquisa_op = input("Deseja pesquisar por ID ou Nome?\n1 - ID\n2 - Nome\nEscolha:")
    encontrado = False
    if pesquisa_op == "1":
        busca = input("Digite o ID do leitor: ")
        campo = "id"

    elif pesquisa_op == "2":
        busca = input("Digite o nome do leitor: ")
        campo = "nome"

    else:
        print("Opção inválida!")
        return

    for leitor in leitores:
        if leitor[campo].lower() == busca.lower():

            if leitor["atividade"]:
                status = "Ativo"
            else:
                status = "Inativo"

            print("\nLEITOR ENCONTRADO!")
            print("ID:", leitor["id"])
            print("Nome:", leitor["nome"])
            print("CPF:", leitor["cpf"])
            print("Telefone:", leitor["telefone"])
            print("Endereço:", leitor["endereço"])
            print("Situação:", status)

            encontrado = True

    if encontrado == False:
        print("Leitor não encontrado.")


def atualizar_leitor():
    atualizar_id = input("Digite o ID do leitor que deseja atualizar: ")
    encontrado = False
    for leitor in leitores:
        if leitor["id"] == atualizar_id:
            encontrado = True
            atualizar_op = input("Leitor encontrado. O que deseja atualizar?\n1 - Nome\n2 - CPF\n3 - Telefone\n4 - Endereço\n5 - Atividade\nDigite a opção desejada: ")

            if atualizar_op == "1":
                leitor["nome"] = input("Digite o novo nome: ")

            elif atualizar_op == "2":
                leitor["cpf"] = input("Digite o novo CPF: ")

            elif atualizar_op == "3":
                leitor["telefone"] = input(
                    "Digite o novo telefone: "
                )

            elif atualizar_op == "4":
                leitor["endereço"] = input(
                    "Digite o novo endereço: "
                )

            elif atualizar_op == "5":
                atividade = input(
                    "O leitor ainda é ativo? (s/n): "
                ).lower()

                if atividade == "s":
                    leitor["atividade"] = True

                elif atividade == "n":
                    leitor["atividade"] = False

                else:
                    print("Opção inválida!")
                    return

            else:
                print("Opção inválida!")
                return

            print("Dados atualizados com sucesso!")
            break

    if encontrado == False:
        print("Leitor não encontrado.")


def excluir_leitor():
    excluir_id = input("Digite o ID do leitor que deseja excluir: ")
    encontrado = False
    for leitor in leitores:
        if leitor["id"] == excluir_id:
            leitores.remove(leitor)
            print("Leitor excluído com sucesso!")
            encontrado = True
            break

    if encontrado == False:
        print("Leitor não encontrado.")

def cadastrar_reserva():
    id_reserva = input("Digite o ID da reserva: ")

    for reserva in fila_reservas:
        if reserva["id"] == id_reserva:
            print("Já existe uma reserva com esse ID!")
            return

    id_leitor = input("Digite o ID do leitor: ")

    leitor_encontrado = False

    for leitor in leitores:
        if leitor["id"] == id_leitor:

            leitor_encontrado = True

            if leitor["atividade"] == False:
                print("Este leitor está inativo e não pode reservar.")
                return

            break

    if leitor_encontrado == False:
        print("Leitor não encontrado!")
        return

    reserva = {
        "id": id_reserva,
        "id_leitor": id_leitor,
        "livro": input("Digite o nome do livro: "),
        "data": input("Digite a data da reserva: ")
    }

    fila_reservas.append(reserva)

    print("Reserva cadastrada com sucesso!")


def listar_reservas():
    if len(fila_reservas) == 0:
        print("Não existem reservas na fila.")
    else:
        print("\nFILA DE RESERVAS")

        for reserva in fila_reservas:
            print("\nID da reserva:", reserva["id"],"\nID do leitor:", reserva["id_leitor"],"\nLivro:", reserva["livro"],"\nData:", reserva["data"])

def atender_reserva():
    if len(fila_reservas) == 0:
        print("Não existem reservas para atender.")
    else:
        reserva = fila_reservas.popleft()

        print("\nReserva atendida!")
        print("ID da reserva:", reserva["id"])
        print("Leitor:", reserva["id_leitor"])
        print("Livro:", reserva["livro"])


def cancelar_reserva():
    id_cancelar = input("Digite o ID da reserva que deseja cancelar: ")
    encontrado = False
    for reserva in fila_reservas:
        if reserva["id"] == id_cancelar:
            fila_reservas.remove(reserva)
            print("Reserva cancelada com sucesso!")
            encontrado = True
            break
    if encontrado == False:
        print("Reserva não encontrada.")

def registrar_devolucao():
    id_devolucao = input("Digite o ID da devolução: ")

    for devolucao in pilha_devolucoes:
        if devolucao["id"] == id_devolucao:
            print("Já existe uma devolução com esse ID!")
            return

    devolucao = {
        "id": id_devolucao,
        "livro": input("Digite o nome do livro: "),
        "id_leitor": input("Digite o ID do leitor: "),
        "data": input("Digite a data da devolução: ")
    }

    pilha_devolucoes.append(devolucao)

    print("Devolução registrada com sucesso!")


def listar_devolucoes():
    if len(pilha_devolucoes) == 0:
        print("Não existem devoluções registradas.")
    else:
        print("\nDEVOLUÇÕES REGISTRADAS")

        for devolucao in reversed(pilha_devolucoes):
            print("\nID:", devolucao["id"],"\nLivro:", devolucao["livro"],"\nID do leitor:", devolucao["id_leitor"],"\nData:", devolucao["data"])

def retirar_devolucao():
    if len(pilha_devolucoes) == 0:
        print("Não existem devoluções para retirar.")
    else:
        devolucao = pilha_devolucoes.pop()

        print("\nÚltima devolução retirada da pilha!")
        print("ID:", devolucao["id"])
        print("Livro:", devolucao["livro"])


def pesquisar_devolucao():
    id_busca = input("Digite o ID da devolução: ")

    encontrado = False

    for devolucao in pilha_devolucoes:
        if devolucao["id"] == id_busca:

            print("\nDEVOLUÇÃO ENCONTRADA!")
            print("ID:", devolucao["id"])
            print("Livro:", devolucao["livro"])
            print("ID do leitor:", devolucao["id_leitor"])
            print("Data:", devolucao["data"])

            encontrado = True
            break

    if encontrado == False:
        print("Devolução não encontrada.")

def cadastrar_categoria():
    print("\nCADASTRAR CATEGORIA\n1 - Cadastrar área principal\n2 - Cadastrar subcategoria\n")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        categoria = input("Digite o nome da categoria: ")

        if categoria in arvore_livros:
            print("Essa categoria já existe!")
            return

        arvore_livros[categoria] = {}

        print("Categoria cadastrada com sucesso!")

    elif opcao == "2":
        categoria = input("Digite a área principal: ")

        if categoria not in arvore_livros:
            print("Categoria principal não encontrada!")
            return

        subcategoria = input("Digite o nome da subcategoria: ")

        if subcategoria in arvore_livros[categoria]:
            print("Essa subcategoria já existe!")
            return

        arvore_livros[categoria][subcategoria] = {}

        print("Subcategoria cadastrada com sucesso!")

    else:
        print("Opção inválida!")


def listar_categorias():
    if len(arvore_livros) == 0:
        print("Nenhuma categoria cadastrada.")
    else:
        print("\nCATEGORIAS DOS LIVROS")

        for categoria, subcategorias in arvore_livros.items():

            print("\n", categoria)

            if len(subcategorias) == 0:
                print("  Nenhuma subcategoria cadastrada.")

            else:
                for subcategoria in subcategorias:
                    print("  -", subcategoria)


def pesquisar_categoria():
    busca = input("Digite o nome da categoria ou subcategoria: ").lower()

    encontrado = False

    for categoria, subcategorias in arvore_livros.items():

        if categoria.lower() == busca:
            print("Categoria encontrada:", categoria)
            encontrado = True
            break

        for subcategoria in subcategorias:

            if subcategoria.lower() == busca:
                print("Subcategoria encontrada:", subcategoria)
                print("Área principal:", categoria)
                encontrado = True
                break

        if encontrado:
            break

    if encontrado == False:
        print("Categoria não encontrada.")


def renomear_categoria():
    print("\nRENOMEAR CATEGORIA")
    print("1 - Renomear área principal")
    print("2 - Renomear subcategoria")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_antigo = input("Digite o nome da categoria atual: ")

        if nome_antigo not in arvore_livros:
            print("Categoria não encontrada!")
            return

        nome_novo = input("Digite o novo nome: ")

        if nome_novo in arvore_livros:
            print("Já existe uma categoria com esse nome!")
            return

        arvore_livros[nome_novo] = arvore_livros.pop(nome_antigo)

        print("Categoria renomeada com sucesso!")

    elif opcao == "2":
        categoria = input("Digite a área principal: ")

        if categoria not in arvore_livros:
            print("Categoria principal não encontrada!")
            return

        nome_antigo = input("Digite o nome da subcategoria atual: ")

        if nome_antigo not in arvore_livros[categoria]:
            print("Subcategoria não encontrada!")
            return

        nome_novo = input("Digite o novo nome: ")

        if nome_novo in arvore_livros[categoria]:
            print("Já existe uma subcategoria com esse nome!")
            return

        arvore_livros[categoria][nome_novo] = (arvore_livros[categoria].pop(nome_antigo))

        print("Subcategoria renomeada com sucesso!")

    else:
        print("Opção inválida!")


def excluir_categoria():
    print("\nEXCLUIR CATEGORIA\n1 - Excluir área principal\n2 - Excluir subcategoria")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        categoria = input("Digite a categoria que deseja excluir: ")

        if categoria in arvore_livros:
            del arvore_livros[categoria]
            print("Categoria excluída com sucesso!")
        else:
            print("Categoria não encontrada!")

    elif opcao == "2":
        categoria = input("Digite a área principal: ")

        if categoria not in arvore_livros:
            print("Categoria principal não encontrada!")
            return

        subcategoria = input("Digite a subcategoria que deseja excluir: ")
        if subcategoria in arvore_livros[categoria]:
            del arvore_livros[categoria][subcategoria]
            print("Subcategoria excluída com sucesso!")
        else:
            print("Subcategoria não encontrada!")

    else:
        print("Opção inválida!")



def salvar_dados():

    with open("dados_sistema.txt","w",encoding="utf-8") as arquivo:

        for leitor in leitores:
            atividade = "1" if leitor["atividade"] else "0"
            arquivo.write(f"LISTA|{leitor['id']}|{leitor['nome']}|"f"{leitor['cpf']}|{leitor['telefone']}|"f"{leitor['endereço']}|{atividade}\n")

        for reserva in fila_reservas:
            arquivo.write(f"FILA|{reserva['id']}|{reserva['id_leitor']}|"f"{reserva['livro']}|{reserva['data']}\n")

        for devolucao in pilha_devolucoes:
            arquivo.write(f"PILHA|{devolucao['id']}|{devolucao['livro']}|"f"{devolucao['data']}\n")

        for categoria, subcategorias in arvore_livros.items():
            if len(subcategorias) == 0:
                arquivo.write(f"ARVORE|{categoria}|\n")

            else:
                for subcategoria in subcategorias:
                    arquivo.write(f"ARVORE|{categoria}|{subcategoria}\n")

    print("Todos os dados foram salvos com sucesso!")

def carregar_dados():
    try:
        with open("dados_sistema.txt","r",encoding="utf-8") as arquivo:
            leitores.clear()
            fila_reservas.clear()
            pilha_devolucoes.clear()
            arvore_livros.clear()
            for linha in arquivo:
                dados = linha.rstrip("\r\n").split("|")
                if dados[0] == "LISTA" and len(dados) == 7:
                    leitor = {
                        "id": dados[1],
                        "nome": dados[2],
                        "cpf": dados[3],
                        "telefone": dados[4],
                        "endereço": dados[5],
                        "atividade": dados[6] == "1"
                    }

                    leitores.append(leitor)

                elif dados[0] == "FILA" and len(dados) == 5:

                    reserva = {
                        "id": dados[1],
                        "id_leitor": dados[2],
                        "livro": dados[3],
                        "data": dados[4]
                    }

                    fila_reservas.append(reserva)
                elif dados[0] == "PILHA" and len(dados) == 5:
                    devolucao = {
                        "id": dados[1],
                        "livro": dados[2],
                        "id_leitor": dados[3],
                        "data": dados[4]
                          }
                    pilha_devolucoes.append(devolucao)

                elif dados[0] == "ARVORE" and len(dados) == 3:

                    categoria = dados[1]
                    subcategoria = dados[2]

                    if categoria not in arvore_livros:
                        arvore_livros[categoria] = {}

                    if subcategoria != "":
                        arvore_livros[categoria][subcategoria] = {}

        print("Todos os dados foram carregados com sucesso!")

    except FileNotFoundError:
        print("Arquivo de dados não encontrado. As estruturas continuam como estavam.")

def menu():
    while True:
        print(" ------- Biblioteca Digital --------\n Bem-vindo(a)!")

        print("\n--- LISTA: LEITORES ---")
        print("1 - Cadastrar leitor")
        print("2 - Listar leitores")
        print("3 - Pesquisar leitor")
        print("4 - Atualizar leitor")
        print("5 - Excluir leitor")

        print("\n--- FILA: RESERVAS ---")
        print("6 - Cadastrar reserva")
        print("7 - Listar reservas")
        print("8 - Atender reserva")
        print("9 - Cancelar reserva")

        print("\n--- PILHA: DEVOLUÇÕES ---")
        print("10 - Registrar devolução")
        print("11 - Listar devoluções")
        print("12 - Pesquisar devolução")
        print("13 - Retirar devolução")

        print("\n--- ÁRVORE: CATEGORIAS ---")
        print("14 - Cadastrar categoria")
        print("15 - Listar categorias")
        print("16 - Pesquisar categoria")
        print("17 - Renomear categoria")
        print("18 - Excluir categoria")

        print("\n--- ARQUIVO TXT ---")
        print("19 - Salvar dados")
        print("20 - Carregar dados")

        print("\n0 - Sair")

        opcao = input("\nDigite a opção desejada: ")

        if opcao == "1":
            cadastrar_leitor()

        elif opcao == "2":
            listar_leitores()

        elif opcao == "3":
            pesquisar_leitor()

        elif opcao == "4":
            atualizar_leitor()

        elif opcao == "5":
            excluir_leitor()

        elif opcao == "6":
            cadastrar_reserva()

        elif opcao == "7":
            listar_reservas()

        elif opcao == "8":
            atender_reserva()

        elif opcao == "9":
            cancelar_reserva()

        elif opcao == "10":
            registrar_devolucao()

        elif opcao == "11":
            listar_devolucoes()

        elif opcao == "12":
            pesquisar_devolucao()

        elif opcao == "13":
            retirar_devolucao()

        elif opcao == "14":
            cadastrar_categoria()

        elif opcao == "15":
            listar_categorias()

        elif opcao == "16":
            pesquisar_categoria()

        elif opcao == "17":
            renomear_categoria()

        elif opcao == "18":
            excluir_categoria()

        elif opcao == "19":
            salvar_dados()

        elif opcao == "20":
            carregar_dados()

        elif opcao == "0":
            print("\nEncerrando o sistema...")
            print("Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")

menu()
