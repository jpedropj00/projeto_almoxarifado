from utils.json_manager import carregar_dados, salvar_dados
from models.fornecedores import Fornecedor

class FornecedorRepository:
    CAMINHO_FORNECEDORES = "../database/fornecedores.json"

    @staticmethod
    def listar():
        """Lista todos os fornecedores cadastrados"""
        dados = carregar_dados(FornecedorRepository.CAMINHO_FORNECEDORES)
        return [Fornecedor.from_dict(fornecedor) for fornecedor in dados]

    @staticmethod
    def buscar_por_id(id: str):
        """Busca um fornecedor pelo seu ID"""
        fornecedores = FornecedorRepository.listar()
        for fornecedor in fornecedores:
            if fornecedor.id == id:
                return fornecedor
        return None
    @staticmethod
    def buscar_por_cnpj(cnpj: str):
        """Busca um fornecedor pelo seu CNPJ"""
        fornecedores = FornecedorRepository.listar()
        for fornecedor in fornecedores:
            if fornecedor.cnpj == cnpj:
                return fornecedor
        return None
    
    @staticmethod
    def adicionar(fornecedor: Fornecedor):
        """Adiciona um novo fornecedor ao repositório"""
        fornecedores = FornecedorRepository.listar()
        fornecedores.append(fornecedor)
        salvar_dados(FornecedorRepository.CAMINHO_FORNECEDORES, [f.to_dict() for f in fornecedores])

    @staticmethod
    def atualizar(fornecedor: Fornecedor):
        """Atualiza um fornecedor existente no repositório"""
        fornecedores = FornecedorRepository.listar()
        for idx, f in enumerate(fornecedores):
            if f.id == fornecedor.id:
                fornecedores[idx] = fornecedor
                salvar_dados(FornecedorRepository.CAMINHO_FORNECEDORES, [f.to_dict() for f in fornecedores])
                return
        raise ValueError("Fornecedor não encontrado")

    @staticmethod
    def remover(id: str):
        """Remove um fornecedor do repositório pelo seu ID"""
        fornecedores = FornecedorRepository.listar()
        fornecedores = [fornecedor for fornecedor in fornecedores if fornecedor.id != id]
        salvar_dados(FornecedorRepository.CAMINHO_FORNECEDORES, [f.to_dict() for f in fornecedores])

    @staticmethod
    def salvar(fornecedor: Fornecedor):
        """Salva um fornecedor, seja adicionando ou atualizando"""
        if FornecedorRepository.buscar_por_id(fornecedor.id):
            FornecedorRepository.atualizar(fornecedor)
        else:
            FornecedorRepository.adicionar(fornecedor)
