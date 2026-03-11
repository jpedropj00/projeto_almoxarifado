from enums.unidademedidaEnum import UnidadeMedida
from enums.categoriaRegistry import Categoria
class ProdutoService:
        @staticmethod
        def cadastrar_produto(nome: str, categoria_id: str, descricao: str, unidade:UnidadeMedida, estoque_minimo: Integer, categoria: str):
                """Cadastra um novo produto"""
                if not nome or not nome.strip():
                        raise ValueError("Nome do produto é obrigatório")
                if not categoria_id or not categoria_id.strip():
                        raise ValueError("Categoria do produto é obrigatória")
                if not descricao or not descricao.strip():
                        raise ValueError("Descrição do produto é obrigatória")
                if not isinstance(unidade, UnidadeMedida):
                        raise ValueError("Unidade de medida inválida")
                if estoque_minimo < 0:
                        raise ValueError("Estoque mínimo não pode ser negativo")
                
                categoria_obj = Categoria.buscar_por_id(categoria_id)
                if not categoria_obj:
                        raise ValueError("Categoria não encontrada")
                
                return Produto(nome=nome.strip(), categoria_id=categoria_id, descricao=descricao.strip(), unidade=unidade, estoque_minimo=estoque_minimo)
        @staticmethod
        def buscar_produto_por_id(id: str):
                                