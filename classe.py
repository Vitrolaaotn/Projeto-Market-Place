class Carrinho_Compras:
    lista_compra = []
    def add_produto(self, produto):
        self.produto = produto
        self.lista_compra.append(produto)

    def listar_produtos(self):
        self.cont = 0
        for produto in self.lista_compra:
            self.cont += 1
            print(f"Nome: {produto.getNome()} - Valor: {produto.getValor()}")

    def getLista(self, vetor):
        return self.lista_compra(vetor)

    def remover_Produto(self, vetor):
        self.vetor = vetor - 1
        self.lista_compra.pop(vetor)

class Produtos:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def getNome(self):
        return self.nome
    
    def getValor(self):
        return self.valor
    
class Cliente(Produtos, Carrinho_Compras):
    clientes = []
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def add_Cliente(self, cliente):
        self.cliente = cliente
        self.clientes.append(cliente)

    def getNome(self):
        return self.nome
    
    def getSenha(self):
        return self.senha

    def listar_Clientes(self):
        self.cont = 0
        for cliente in self.clientes:
            self.cont += 1
            print(f"Nome: {cliente.getNome()} - Senha: {cliente.getSenha()}")
