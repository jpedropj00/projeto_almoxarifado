class CategoriaRegistry:
    """Classe feita para poder registrar as categorias, porém sendo mútavel e podendo adicionar categorias"""
    tipos = set()
    
    @classmethod
    def adicionar_tipo(cls, nome: str):
        cls.tipos.add(nome.upper())