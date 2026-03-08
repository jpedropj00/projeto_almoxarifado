from utils import id_generator
from enums import nivel_estoque
class Produto: 
    
    
    def __init__(self, nome, descricao, unidade, estoque_minimo, id_categoria, quantidade_atual = 0, ativo=True, id = None):
        self.id = id if id else id_generator()
        self.nome = nome
        self.descricao = descricao
        self.unidade = unidade
        self.estoque_minimo = estoque_minimo
        self.id_categoria = id_categoria
        self.ativo = ativo
        self.quantidade_atual = quantidade_atual
        
    ALERTA_ESTOQUE = 5
    
    @property
    def nivel_estoque(self):
        if self.quantidade_atual == 0:
            nivel_estoque.NivelEstoque.SEM_ESTOQUE
        if self.quantidade_atual <= self.estoque_minimo:
            return nivel_estoque.NivelEstoque.REPOSICAO
        if self.quantidade_atual <= (self.estoque_minimo + self.ALERTA_ESTOQUE):
            return nivel_estoque.NivelEstoque.BAIXO
        return nivel_estoque.NivelEstoque.NORMAL
    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")
        self.quantidade_atual += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")

        if quantidade > self.quantidade_atual:
            raise ValueError("Estoque insuficiente")

        self.quantidade_atual -= quantidade
        
    def ativar(self):
        self.ativo = True
    
    def desativar(self):
        self.ativo = False
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "unidade": self.unidade,
            "estoque_minimo": self.estoque_minimo,
            "id_categoria": self.id_categoria,
            "ativo": self.ativo,
            "quantidade_atual": self.quantidade_atual
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls (
            id = data["id"],
            nome = data["nome"],
            descricao = data["descricao"],
            unidade = data["unidade"],
            id_categoria = data["id_categoria"],
            ativo = data["ativo"],
            quantidade_atual = data["quantidade_atual"],
            estoque_minimo = data["estoque_minimo"]
        )
        
    
        
                
    
    
        
    
        
        
    
        