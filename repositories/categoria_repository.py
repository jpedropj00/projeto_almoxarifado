from utils.json_manager import carregar_dados, salvar_dados
from enums.categoria import Categoria

CAMINHO_CATEGORIA = "../database/categorias.json"
class CategoriaRepository:
    @staticmethod
    def listar():
        """Lista todas as categorias cadastradas"""
        dados = carregar_dados(CAMINHO_CATEGORIA)
        return [Categoria.from_dict(categoria) for categoria in dados]
    @staticmethod
    def buscar_por_id(id: str):
        """Busca uma categoria pelo seu ID"""
        categorias = CategoriaRepository.listar()
        for categoria in categorias:
            if categoria.id == id:
                return categoria
        return None
    @staticmethod
    def buscar_por_nome(nome: str):
        """Busca uma categoria pelo seu nome"""
        categorias = CategoriaRepository.listar()
        for categoria in categorias:
            if categoria.nome == nome:
                return categoria
        return None
    @staticmethod
    def adicionar(categoria: Categoria):
        """Adiciona uma nova categoria ao repositório"""
        categorias = CategoriaRepository.listar()
        categorias.append(categoria)
        salvar_dados(CAMINHO_CATEGORIA, [categoria.to_dict() for categoria in categorias])
    @staticmethod
    def atualizar(categoria: Categoria):
        """Atualiza uma categoria existente no repositório"""
        categorias = CategoriaRepository.listar()
        for idx, c in enumerate(categorias):
            if c.id == categoria.id:
                categorias[idx] = categoria
                salvar_dados(CAMINHO_CATEGORIA, [categoria.to_dict() for categoria in categorias])
                return
        raise ValueError("Categoria não encontrada")
    @staticmethod
    def remover(id: str):
        """Remove uma categoria do repositório pelo seu ID"""
        categorias = CategoriaRepository.listar()
        categorias = [categoria for categoria in categorias if categoria.id != id]
        salvar_dados(CAMINHO_CATEGORIA, [categoria.to_dict() for categoria in categorias])
    @staticmethod
    def salvar(categoria: Categoria):
        """Salva uma categoria, seja adicionando ou atualizando"""
        if CategoriaRepository.buscar_por_id(categoria.id):
            CategoriaRepository.atualizar(categoria)
        else:
            CategoriaRepository.adicionar(categoria)
 