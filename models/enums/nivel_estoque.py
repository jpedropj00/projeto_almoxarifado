from enum import Enum

class NivelEstoque(Enum):
    """Classe feita para enumerar os tipos de nível de estoque para auxiliar a função de produtos"""
    SEM_ESTOQUE = "SEM ESTOQUE"
    REPOSICAO = "REPOSICAO"
    BAIXO = "ESTOQUE BAIXO"
    NORMAL = "NORMAL"
    