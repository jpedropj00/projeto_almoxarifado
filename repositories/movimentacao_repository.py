from utils.json_manager import carregar_dados, salvar_dados
from models.movimentacao import Movimentacao

class MovimentacaoRepository:
    CAMINHO_MOVIMENTACOES = "../database/movimentacoes.json"

    @staticmethod
    def listar():
        """Lista todas as movimentações cadastradas"""
        dados = carregar_dados(MovimentacaoRepository.CAMINHO_MOVIMENTACOES)
        return [Movimentacao.from_dict(movimentacao) for movimentacao in dados]

    @staticmethod
    def buscar_por_id(id: str):
        """Busca uma movimentação pelo seu ID"""
        movimentacoes = MovimentacaoRepository.listar()
        for movimentacao in movimentacoes:
            if movimentacao.id == id:
                return movimentacao
        return None
    @staticmethod
    def buscar_por_produto_id(produto_id: str):
        """Busca movimentações relacionadas a um produto específico"""
        movimentacoes = MovimentacaoRepository.listar()
        return [mov for mov in movimentacoes if mov.produto_id == produto_id]
    @staticmethod
    def buscar_por_fornecedor_id(fornecedor_id: str):
        """Busca movimentações relacionadas a um fornecedor específico"""
        movimentacoes = MovimentacaoRepository.listar()
        return [mov for mov in movimentacoes if mov.fornecedor_id == fornecedor_id]
    @staticmethod
    def adicionar(movimentacao: Movimentacao):
        """Adiciona uma nova movimentação ao repositório"""
        movimentacoes = MovimentacaoRepository.listar()
        movimentacoes.append(movimentacao)
        salvar_dados(MovimentacaoRepository.CAMINHO_MOVIMENTACOES, [mov.to_dict() for mov in movimentacoes])
    
    