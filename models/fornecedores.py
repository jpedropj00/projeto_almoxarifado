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

    def set_email(self , novo_email):
        if not verify_email.validar_email(novo_email):
            raise ValueError('Email Inválido')
        self.email = novo_email.lower()

    @staticmethod
    def cnpj_igual(cnpj1: str , cnpj2: str)-> bool:
        def limpar(cnpj):
            return cnpj.replace(".","").replace("/","").replace("-","")
        
        return limpar(cnpj1) == limpar(cnpj2)

    @staticmethod
    def telefone_igual(tel1: str, tel2: str ) -> bool:
        def limpar(telefone):
            return telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        return limpar(tel1) == limpar(tel2)

        

        