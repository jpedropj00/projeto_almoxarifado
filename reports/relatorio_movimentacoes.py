from repositories.movimentacao_repository import MovimentacaoRepository
from enums.tipo import TipoTransacao
from datetime import datetime


class MovimentacaoReport:

    def __init__(self):
        self.repository = MovimentacaoRepository()


    def movimentacoes_por_periodo(self, data_inicio, data_fim):

        movimentacoes = self.repository.listar()

        return [
            m for m in movimentacoes
            if data_inicio <= m.data <= data_fim
        ]


    def movimentacoes_produto(self, id_produto):

        movimentacoes = self.repository.listar()

        return [
            m for m in movimentacoes
            if m.id_produto == id_produto
        ]


    def entradas_periodo(self, data_inicio, data_fim):

        movimentacoes = self.repository.listar()

        return [
            m for m in movimentacoes
            if m.tipo == TipoTransacao.ENTRADA
            and data_inicio <= m.data <= data_fim
        ]


    def saidas_periodo(self, data_inicio, data_fim):

        movimentacoes = self.repository.listar()

        return [
            m for m in movimentacoes
            if m.tipo == TipoTransacao.SAIDA
            and data_inicio <= m.data <= data_fim
        ]