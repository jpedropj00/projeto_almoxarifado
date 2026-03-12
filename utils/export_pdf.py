from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


class PDFExporter:

    @staticmethod
    def exportar(dados, caminho_arquivo, titulo="Relatório"):

        if not dados:
            raise ValueError("Nenhum dado para exportar")

        # converter objetos para dicionário
        if hasattr(dados[0], "to_dict"):
            dados = [obj.to_dict() for obj in dados]

        colunas = list(dados[0].keys())

        tabela_dados = [colunas]

        for item in dados:
            tabela_dados.append(list(item.values()))

        pdf = SimpleDocTemplate(caminho_arquivo, pagesize=A4)

        tabela = Table(tabela_dados)

        estilo = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("GRID", (0, 0), (-1, -1), 1, colors.black)
        ])

        tabela.setStyle(estilo)

        elementos = [tabela]

        pdf.build(elementos)