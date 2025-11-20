# A classe é um conjunto de objetos
class Mercado:
    mercados = []
    # Métodos especiais (dunder methods)
    # __init__ é o construtor da classe
    # Costruir um objeto na mémoria
    # Stack e Heap
    # Stack é a pilha de chamadas
    # Heap é a memória dinâmica
    # Self serve para definir os atributos do objeto
    def __init__(self, nome, midia, ativo):
        self.nome = nome
        self.midia = midia
        self.ativo = ativo

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False      

    # Método especial para representar o objeto como string
    def __str__(self):
        return f"O mercado {self.nome} está {'ativo' if self.ativo else 'inativo'}."
    
    
    
    def listar_mercados():
        for mercado in Mercado.mercados:
            status = "Ativo" if mercado.ativo else "Inativo"
            print(f"{mercado.nome}, Site: {mercado.midia}, Status: {status}")