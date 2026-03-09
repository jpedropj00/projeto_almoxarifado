from utils import id_generator, hash_generator, verify_email
import bcrypt
from datetime import datetime

class Usuario:
    def __init__(self, id, nome, senha, email, ativo=True, criado_em = None, senha_criptografada = False):
        self.id = id if id else id_generator.gerar_id()
        if not nome:
            raise ValueError ("Nome inválido")
        self.nome = nome
        if senha_criptografada:
            self.senha = senha
        else:
            self.senha = hash_generator._gerar_hash()
        if not verify_email(email):
            raise ValueError("Email Inválido")
        self.email = email
        self.ativo = ativo
        self.criado_em = criado_em if criado_em else datetime.now()
    
    def validar_senha(self, senha_digitada):
        """Validando senha para login"""
        return bcrypt.checkpw(
            senha_digitada.encode("utf-8"),
            self.senha.encode("utf-8")
        )
    def desativar_user(self):
        """Desativar user"""
        self.ativo = False
    
    def toDict(self):
        """Transformando dados em objetos
        para JSON(utilizado para persistência de dados)"""
        return {
            "id": self.id,
            "nome": self.nome,
            "senha": self.senha,
            "email": self.email,
            "ativo": self.ativo,
            "criado_em": self.criado_em.isoformat()
        }
    @classmethod
    def from_dict(cls, data):
        """Retirada das informações de JSON para objeto novamente"""
        return cls(
            id = data["id"],
            nome = data["nome"],
            email = data["email"],
            senha = data["senha"],
            ativo = data["ativo"],
            criado_em = datetime.fromisoformat(data["criado_em"]),
            senha_criptografada = True
        )