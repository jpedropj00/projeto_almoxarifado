import sys
import os

# Caminho da raiz do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Adiciona a raiz ao PYTHONPATH
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


def main():
    try:
        from gui.telas.app2 import main as start_app
        start_app()

    except ModuleNotFoundError as e:
        print("\nErro de importação de módulo.")
        print("Verifique se todas as pastas possuem __init__.py")
        print("Detalhes:", e)

    except Exception as e:
        print("\nErro ao iniciar o sistema:")
        print(e)


if __name__ == "__main__":
    main()