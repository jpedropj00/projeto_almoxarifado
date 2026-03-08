def validar_cnpj(cnpj: str) -> bool:
    """Validador de cnpj"""
    if len(cnpj) != 14 or not cnpj.isdigit():
        return False
    if cnpj == cnpj[0] * 14:
        return False
    def calc_dv(cnpj_parcial, pesos):
        """Funçao que calcula o cnpj em partes e passa para a função principal"""
        soma = sum(int(d) * p for d, p in zip(cnpj_parcial, pesos))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)
    dv1 = calc_dv(cnpj[:12], [5,4,3,2,9,8,7,6,5,4,3,2])
    dv2 = calc_dv(cnpj[:12] + dv1, [6,5,4,3,2,9,8,7,6,5,4,3,2])

    return cnpj[-2:] == dv1 + dv2