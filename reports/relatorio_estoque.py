from repositories.produto_repository import ProdutoRepository
from enums.nivel_estoque import NivelEstoque


class EstoqueReport:

    def __init__(self):
        self.repository = ProdutoRepository()


    def inventario_completo(self):

        return self.repository.listar()


    def produtos_sem_estoque(self):

        produtos = self.repository.listar()

        return [
            p for p in produtos
            if p.quantidade_atual == 0
        ]


    def produtos_estoque_baixo(self):

        produtos = self.repository.listar()

        return [
            p for p in produtos
            if p.quantidade_atual <= p.estoque_minimo
        ]


    def produtos_para_reposicao(self):

        produtos = self.repository.listar()

        return [
            p for p in produtos
            if p.nivel_estoque == NivelEstoque.REPOSICAO
        ]
    def produtos_ativos(self):
        produtos = self.repository.listar()

        return [
            p for p in produtos
            if p.ativo
        ]