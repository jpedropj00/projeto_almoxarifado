from enum import Enum

class NivelEstoque(Enum):
    SEM_ESTOQUE = "SEM ESTOQUE"
    REPOSICAO = "REPOSICAO"
    BAIXO = "ESTOQUE BAIXO"
    NORMAL = "NORMAL"
    