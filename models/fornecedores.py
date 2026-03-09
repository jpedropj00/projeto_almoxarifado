from utils import hash_generator, verify_email, validador_cnpj
class Fornecedor:
    def __init__(self, nome: str, cnpj: str, telefone: str, email: str, ativo: bool = True):
        if not nome:
            raise ValueError ("Nome inválido")
        self.nome = nome.strip().title()
        
        if not verify_email.validar_email(email):
            raise ValueError ("Email inválido")
        self.email = email.lower()

        if not validador_cnpj.validar_cnpj(cnpj):
            raise ValueError ("Cnpj Inválido")
        self.cnpj = cnpj.replace(".", "").replace("/" , "").replace("-" ,"")

        if not telefone or not telefone.strip():
            raise ValueError ("Telefone Inválido")
        self.telefone = telefone.strip()

        self.ativo = ativo 

        
        