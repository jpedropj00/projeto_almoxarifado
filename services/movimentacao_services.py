from models.movimentacao import Movimentacao
from repositories.movimentacao_repository import MovimentacaoRepository
from enums.tipo import TipoMovimentacao
from repositories.produto_repository import ProdutoRepository
class MovimentacaoService:
    @staticmethod
    def registrar_entrada(id_produto, id_usuario, quantidade,observacao = ""):
        """Registra uma nova movimentação de entrada ou saída de estoque"""
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        usuario = UsuarioRepository.buscar_por_id(id_usuario)
        if not usuario:
            raise ValueError("Usuário não encontrado")
        produto = ProdutoRepository.buscar_por_id(id_produto)
        if not produto:
            raise ValueError("Produto não encontrado")
        movimentacao = Movimentacao(id_produto=id_produto, id_usuario=id_usuario, quantidade=quantidade, tipo=TipoTransacao.ENTRADA, observacao=observacao)
        MovimentacaoRepository.adicionar(movimentacao)
        produto.adicionar_estoque(quantidade)
        
        ProdutoRepository.atualizar(produto)
        return movimentacao

    @staticmethod
    def registrar_saida(id_produto, id_usuario, quantidade, observacao = ""):
        """Registra uma nova movimentação de saída de estoque"""
        produto = ProdutoRepository.buscar_por_id(id_produto)
        usuario = UsuarioRepository.buscar_por_id(id_usuario)
        if not usuario:
            raise ValueError("Usuário não encontrado")
        if not produto:
            raise ValueError("Produto não encontrado")

        produto.remover_estoque(quantidade)

        movimentacao = Movimentacao(
            id_produto=id_produto,
            id_usuario=id_usuario,
            quantidade=quantidade,
            tipo=TipoTransacao.SAIDA,
            observacao=observacao
        )

        self.prod_repo.atualizar(produto)
        self.mov_repo.adicionar(movimentacao)

        return movimentacao
    @staticmethod
    def listar_movimentacoes():
        """Lista todas as movimentações registradas"""
        return MovimentacaoRepository.listar()
    @staticmethod
    def lista_por_produto(id_produto):
        """Lista movimentações relacionadas a um produto específico"""
        movimentacoes = MovimentacaoRepository.listar()
        if not movimentacoes:
            raise ValueError("Nenhuma movimentação encontrada para este produto")
        lista_movimentacoes = []
        for m in movimentacoes:
            if m.id_produto == id_produto:
                lista_movimentacoes.append(m)
        return lista_movimentacoes
    @staticmethod
    def listar_movimentacoes_por_usuario(self, id_usuario):
        movimentacoes = self.mov_repo.listar()

        return [
            m for m in movimentacoes
            if m.id_usuario == id_usuario
        ]

    @staticmethod
    def buscar_por_id(self, id_movimentacao):

        movimentacoes = self.mov_repo.listar()

        for m in movimentacoes:

            if m.id == id_movimentacao:
                return m

        raise ValueError("Movimentação não encontrada")


