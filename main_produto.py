# Ultimo desafio 
# Criar uma classe Produto com os atributos nome, preco, estoque, data_validade.
# Criar métodos para adicionar estoque, remover estoque e verificar validade.
# Criar uma lista de produtos e listar todos os produtos com seus detalhes.

# Menu de interação com o usuário para gerenciar mercados e produtos.

from produto import Produto

lista_produtos = [
    Produto("Arroz", 20.0, 50, "2024-12-31"),
    Produto("Feijão", 8.0, 30, "2024-11-30"),
    Produto("Macarrão", 5.0, 20, "2025-01-15")
]
def menu():
    while True:
        print("\nMenu de Produtos:")
        print("1. Listar Produtos")
        print("2. Adicionar Estoque")
        print("3. Remover Estoque")
        print("4. Verificar Validade")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            for produto in lista_produtos:
                print(f"Nome: {produto.nome}, Preço: {produto.preco}, Estoque: {produto.estoque}, Validade: {produto.data_validade}")
        elif escolha == "2":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a adicionar: "))
            for produto in lista_produtos:
                if produto.nome == nome:
                    produto.adicionar_estoque(quantidade)
                    print(f"Estoque atualizado: {produto.estoque}")
                    break
            else:
                print("Produto não encontrado, escreva o nome conforme o produto em estoque, com a primeira letra maiúscula .")
        elif escolha == "3":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a remover: "))
            for produto in lista_produtos:
                if produto.nome == nome:
                    produto.remov   er_estoque(quantidade)
                    print(f"Estoque atualizado: {produto.estoque}")
                    break
            else:
                print("Produto não encontrado, escreva o nome conforme o produto em estoque, com a primeira letra maiúscula.")
        elif escolha == "4":
            nome = input("Nome do produto: ")
            data_atual = input("Escreva data atual apenas com números sem espaço (YYYYMMDD): ")
            for produto in lista_produtos:
                if produto.nome == nome:
                    if produto.verificar_validade(data_atual):
                        print(f"O produto {produto.nome} está vencido.")
                    else:
                        print(f"O produto {produto.nome} está dentro da validade.")
                    break
            else:
                print("Produto não encontrado, escreva o nome conforme o produto em estoque, com a primeira letra maiúscula..")
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

    
print("Bem-vindo ao sistema de gerenciamento de produtos!")
menu()
