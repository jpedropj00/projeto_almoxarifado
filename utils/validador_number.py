def validar_numero(numero: str) -> bool:
    """Valida telefone brasileiro com DDD"""
    if not numero.isdigit():
        return False
    if len(numero) not in (10, 11):
        return False
    ddd = int(numero[:12])