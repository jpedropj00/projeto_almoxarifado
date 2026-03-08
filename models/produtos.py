from utils import id_generator
from enums import nivel_estoque
class Produto: 
    
    
    def __init__(self, nome, descricao, unidade, estoque_minimo, nome_categoria, quantidade_atual = 0, ativo=True, id = None):
        self.id = id if id else id_generator()
        self.nome = nome
        self.descricao = descricao
        self.unidade = unidade
        self.estoque_minimo = estoque_minimo
        self.nome_categoria = nome_categoria
        self.ativo = ativo
        self.quantidade_atual = quantidade_atual
        
    ALERTA_ESTOQUE = 5
    
    @property
    def nivel_estoque(self):
        """Método utilizado para ver nível do estoque para avisar usuario."""
        if self.quantidade_atual == 0:
            nivel_estoque.NivelEstoque.SEM_ESTOQUE
        if self.quantidade_atual <= self.estoque_minimo:
            return nivel_estoque.NivelEstoque.REPOSICAO
        if self.quantidade_atual <= (self.estoque_minimo + self.ALERTA_ESTOQUE):
            return nivel_estoque.NivelEstoque.BAIXO
        return nivel_estoque.NivelEstoque.NORMAL
    def adicionar_estoque(self, quantidade):
        """Método para fazer uma entrada no estoque"""
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")
        self.quantidade_atual += quantidade

    def remover_estoque(self, quantidade):
        """Método para fazer uma saída no estoque"""
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")

        if quantidade > self.quantidade_atual:
            raise ValueError("Estoque insuficiente")

        self.quantidade_atual -= quantidade
        
    def ativar(self):
        """Método para ativar o produto novamente."""
        self.ativo = True
    
    def desativar(self):
        """Método para desativar o produto"""
        self.ativo = False
    
    def to_dict(self):
        """Método para transformar o objeto em JSON para persistência de dados"""
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "unidade": self.unidade,
            "estoque_minimo": self.estoque_minimo,
            "nome_categoria": self.nome_categoria,
            "ativo": self.ativo,
            "quantidade_atual": self.quantidade_atual
        }
    
    @classmethod
    def from_dict(cls, data):
        """Método de classe para transformar JSON em objeto"""
        return cls (
            id = data["id"],
            nome = data["nome"],
            descricao = data["descricao"],
            unidade = data["unidade"],
            nome_categoria = data["nome_categoria"],
            ativo = data["ativo"],
            quantidade_atual = data["quantidade_atual"],
            estoque_minimo = data["estoque_minimo"]
        )
        
    
        
                
    
    
        
    
        
        
    
        