from utils.json_manager import carregar_dados, salvar_dados
from models.usuario import Usuario
CAMINHO_USUARIOS = "../database/usuarios.json"

class UsuarioRepository:
    @staticmethod
    def listar():
        """Lista todos os usuários cadastrados"""
        dados = carregar_dados(CAMINHO_USUARIOS)
        return [Usuario.from_dict(usuario) for usuario in dados]
    @staticmethod
    def buscar_por_id(id: str):
        """Busca um usuário pelo seu ID"""
        usuarios = UsuarioRepository.listar()
        for usuario in usuarios:
            if usuario.id == id:
                return usuario
        return None
    @staticmethod
    def adicionar(usuario: Usuario):
        """Adiciona um novo usuário ao repositório"""
        usuarios = UsuarioRepository.listar()
        usuarios.append(usuario)
        salvar_dados(CAMINHO_USUARIOS, [usuario.to_dict() for usuario in usuarios])
    @staticmethod
    def atualizar(usuario: Usuario):
        """Atualiza um usuário existente no repositório"""
        usuarios = UsuarioRepository.listar()
        for idx, u in enumerate(usuarios):
            if u.id == usuario.id:
                usuarios[idx] = usuario
                salvar_dados(CAMINHO_USUARIOS, [usuario.to_dict() for usuario in usuarios])
                return
        raise ValueError("Usuário não encontrado")
    def remover(id: str):
        """Remove um usuário do repositório pelo seu ID"""
        usuarios = UsuarioRepository.listar()
        usuarios = [usuario for usuario in usuarios if usuario.id != id]
        salvar_dados(CAMINHO_USUARIOS, [usuario.to_dict() for usuario in usuarios])
    def salvar(usuario: Usuario):
        """Salva um usuário, seja adicionando ou atualizando"""
        if UsuarioRepository.buscar_por_id(usuario.id):
            UsuarioRepository.atualizar(usuario)
        else:
            UsuarioRepository.adicionar(usuario)