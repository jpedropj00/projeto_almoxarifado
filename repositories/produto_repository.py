from utils.json_manager import carregar_dados, salvar_dados
from models.produto import Produto

CAMINHO_PRODUTOS = "../database/produtos.json"

class ProdutoRepository:
    @staticmethod
    def listar():
        """Lista todos os produtos cadastrados"""
        dados = carregar_dados(CAMINHO_PRODUTOS)
        return [Produto.from_dict(produto) for produto in dados]
    @staticmethod
    def buscar_por_id(id: str):
        """Busca um produto pelo seu ID"""
        produtos = ProdutoRepository.listar()
        for produto in produtos:
            if produto.id == id:
                return produto
        return None
    @staticmethod
    def adicionar(produto: Produto):
        """Adiciona um novo produto ao repositório"""
        produtos = ProdutoRepository.listar()
        produtos.append(produto)
        salvar_dados(CAMINHO_PRODUTOS, [produto.to_dict() for produto in produtos])
    @staticmethod
    def atualizar(produto: Produto):
        """Atualiza um produto existente no repositório"""
        produtos = ProdutoRepository.listar()
        for idx, p in enumerate(produtos):
            if p.id == produto.id:
                produtos[idx] = produto
                salvar_dados(CAMINHO_PRODUTOS, [produto.to_dict() for produto in produtos])
                return
        raise ValueError("Produto não encontrado")
    def remover(id: str):
        """Remove um produto do repositório pelo seu ID"""
        produtos = ProdutoRepository.listar()
        produtos = [produto for produto in produtos if produto.id != id]
        salvar_dados(CAMINHO_PRODUTOS, [produto.to_dict() for produto in produtos])
    def salvar(produto: Produto):
        """Salva um produto, seja adicionando ou atualizando"""
        if ProdutoRepository.buscar_por_id(produto.id):
            ProdutoRepository.atualizar(produto)
        else:
            ProdutoRepository.adicionar(produto)