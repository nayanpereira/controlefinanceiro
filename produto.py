# DESAFIO 
# Criar uma classe Produto com os atributos nome, preco, estoque, data_validade.
# Criar métodos para adicionar estoque, remover estoque e verificar validade.
# Criar uma lista de produtos e listar todos os produtos com seus detalhes.

# Menu de interação com o usuário para gerenciar mercados e produtos.

class Produto:
    def __init__ (self, nome, preco, estoque, data_validade):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque  
        self.data_validade = data_validade

    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade   

    def remover_estoque(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
        else:
            print("Estoque insuficiente!")

    def verificar_validade(self, data_atual):
        return data_atual > self.data_validade