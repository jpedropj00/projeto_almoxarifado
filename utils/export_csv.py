import csv


class CSVExporter:

    @staticmethod
    def exportar(dados, caminho_arquivo):

        if not dados:
            raise ValueError("Nenhum dado para exportar")

        # Se os objetos forem classes (Produto, Usuario etc)
        if hasattr(dados[0], "to_dict"):
            dados = [obj.to_dict() for obj in dados]

        campos = dados[0].keys()

        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:

            writer = csv.DictWriter(arquivo, fieldnames=campos)

            writer.writeheader()

            for linha in dados:
                writer.writerow(linha)