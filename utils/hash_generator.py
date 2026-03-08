import bcrypt
def _gerar_hash(self, senha):
        """Gerando criptografia da senha"""
        senha_bytes = senha.encode("utf-8")
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha_bytes, salt).decode("utf-8")