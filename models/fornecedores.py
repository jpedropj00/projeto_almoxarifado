from utils import hash_generator, verify_email, validador_cnpj
class Fornecedor:
    def __init__(self, nome: str, cnpj: str, telefone: str, email: str, ativo: bool = True):
        if not nome:
            raise ValueError ("Nome inválido")
        self.nome = nome
        if not verify_email.validar_email(email):
            raise ValueError ("Email inválido")
        self.email = email
        if not validador_cnpj.validar_cnpj(cnpj):
            raise ValueError ("Cnpj Inválido")
        self.cnpj = cnpj
        
        
        
        
        