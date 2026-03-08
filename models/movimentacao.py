from datetime import datetime
from utils import id_generator
from enums import tipo
from produtos import Produto
class Movimentacao:
    def __init__(self,id_produto, id_usuario, quantidade,tipo, data=None, id = None, observacao = ""):
        self.id = id if id else id_generator.gerar_id()
        self.id_produto = id_produto
        self.id_usuario = id_usuario
        self.quantidade = quantidade
        self.data = data if data else datetime.now()
        self.tipo = tipo
        self.observacao = observacao
        
    def aplicar_movimentacao(self, quantidade):
        if self.tipo == tipo.TipoTransacao.ENTRADA:
            Produto.adicionar_estoque(quantidade)
        
        if self.tipo == tipo.TipoTransacao.SAIDA:
            Produto.remover_estoque(quantidade)
            
    
    def to_dict(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_produto" : self.id_produto,
            "quantidade": self.quantidade,
            "tipo": self.tipo,
            "data": datetime.fromisoformat(self.data),
            "observacoes": self.observacao
        }
    @classmethod    
    def from_dict(cls, data):
        return cls(
            id = data["id"],
            id_produto = data["id_produto"],
            id_usuario = data["id_usuario"],
            quantidade = data["quantidade"],
            data = datetime.isoformat()
        )

            
    
    
        