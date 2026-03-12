import customtkinter as ctk
from tkinter import ttk

from services.produto_service import ProdutoService


class ProdutoLista:

    def __init__(self, parent):

        self.service = ProdutoService()

        self.window = ctk.CTkToplevel(parent)
        self.window.title("Produtos")
        self.window.geometry("850x500")

        self.produtos = self.service.listar_produtos()

        self.criar_interface()

    # -------------------------------------

    def criar_interface(self):

        titulo = ctk.CTkLabel(
            self.window,
            text="📦 Produtos Cadastrados",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        titulo.pack(pady=10)

        # Campo de pesquisa
        self.campo_pesquisa = ctk.CTkEntry(
            self.window,
            placeholder_text="Pesquisar produto..."
        )
        self.campo_pesquisa.pack(pady=10)

        self.campo_pesquisa.bind("<KeyRelease>", self.filtrar_produtos)

        # FRAME DA TABELA
        frame_tabela = ctk.CTkFrame(self.window)
        frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

        # SCROLLBAR
        scrollbar = ttk.Scrollbar(frame_tabela)
        scrollbar.pack(side="right", fill="y")

        # TABELA
        self.tabela = ttk.Treeview(
            frame_tabela,
            columns=("id", "nome", "categoria", "unidade", "estoque"),
            show="headings",
            yscrollcommand=scrollbar.set
        )

        scrollbar.config(command=self.tabela.yview)

        # COLUNAS
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Produto")
        self.tabela.heading("categoria", text="Categoria")
        self.tabela.heading("unidade", text="Unidade")
        self.tabela.heading("estoque", text="Estoque")

        self.tabela.column("id", width=80)
        self.tabela.column("nome", width=200)
        self.tabela.column("categoria", width=150)
        self.tabela.column("unidade", width=100)
        self.tabela.column("estoque", width=100)

        self.tabela.pack(fill="both", expand=True)

        self.carregar_produtos(self.produtos)

    # -------------------------------------

    def carregar_produtos(self, produtos):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for p in produtos:

            self.tabela.insert(
                "",
                "end",
                values=(
                    p.id,
                    p.nome,
                    p.nome_categoria,
                    p.unidade,
                    p.quantidade_atual
                )
            )

    # -------------------------------------

    def filtrar_produtos(self, event):

        termo = self.campo_pesquisa.get().lower()

        filtrados = [
            p for p in self.produtos
            if termo in p.nome.lower()
        ]

        self.carregar_produtos(filtrados)