import bcrypt
from datetime import datetime
class Usuario:
    def __init__(self, id, nome, senha, email, ativo=True, criado_em = None):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.email = email
        self.ativo = ativo
        self.criado_em = datetime.now()
    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            
        }