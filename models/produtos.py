class Produto: 
    def __init__(self, id, nome, descricao, unidade, estoque_minimo, id_categoria, quantidade_atual, ativo):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.unidade = unidade
        self.estoque_minimo = estoque_minimo
        self.id_categoria = id_categoria
        self.quantidade_atual = 0
        self.ativo = True
        