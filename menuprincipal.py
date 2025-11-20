from mercado import Mercado

# Se eu programo sem OO, eu sou um programador procedural.
# Funções soltas, estruturas sequenciais e dicionarios.

# Criar um dicionario mercado nome,site,ativo
mercado = {
    "nome": "Tudo Bom",
    "midia": "www.tudobom.com.br",
    "ativo": False
}

# Paradigma procedural
# Paradigma Orientado a Objetos
# Paradigma Funcional (lambda)
m1 = Mercado("Tudo Bom", "www.tudobom.com.br", False)
m2 = Mercado("Compra Fácil", "www.comprafacil.com.br", True)
m3 = Mercado("Mercado Legal", "www.mercadolegal.com.br", False)
m4 = Mercado("Supermercado Show", "www.supermercado.com.br", True)

print(m1.ativo)
m1.ativar()
print(m1.ativo)
m1.desativar()
print(m1.ativo)

print(m2.nome)

mercados = [m1, m2, m3, m4]
print("Lista de Mercados:")
for mercado in mercados:
    status = "Ativo" if mercado.ativo else "Inativo"
    print(f"{mercado.nome}, Site: {mercado.midia}, Status: {status}")

print(vars(m1))
print(dir(m1))
print(m1) # Chama o método __str__ implicitamente
m5 = Mercado("Mercado Novo", "www.mercadonovo.com.br", True)
m6 = Mercado("Mercado Antigo", "www.mercadoantigo.com.br", False)
m7 = Mercado("Dia a Dia", "www.diaadia.com.br", True)
m8 = Mercado("Ratico", "www.ratico.com.br", False)

m8.ativar()

Mercado.mercados.append(m5)
Mercado.mercados.append(m6)     
Mercado.mercados.append(m7)
Mercado.mercados.append(m8)
Mercado.listar_mercados()

## Ultimo desafio 
## Criar uma classe Produto com os atributos nome, preco, estoque, data_validade.
## Criar métodos para adicionar estoque, remover estoque e verificar validade.
## Criar uma lista de produtos e listar todos os produtos com seus detalhes.

## Menu de interação com o usuário para gerenciar mercados e produtos.