import customtkinter as ctk
from tkinter import messagebox

from services.produto_service import ProdutoService


class ProdutoCadastro:

    def __init__(self, parent):

        self.service = ProdutoService()

        self.window = ctk.CTkToplevel(parent)
        self.window.title("Cadastrar Produto")
        self.window.geometry("400x400")

        self.criar_formulario()

    def criar_formulario(self):

        ctk.CTkLabel(self.window, text="Nome").pack(pady=5)
        self.nome = ctk.CTkEntry(self.window)
        self.nome.pack()

        ctk.CTkLabel(self.window, text="Descrição").pack(pady=5)
        self.descricao = ctk.CTkEntry(self.window)
        self.descricao.pack()

        ctk.CTkLabel(self.window, text="Categoria").pack(pady=5)
        self.categoria = ctk.CTkEntry(self.window)
        self.categoria.pack()

        ctk.CTkLabel(self.window, text="Unidade").pack(pady=5)
        self.unidade = ctk.CTkEntry(self.window)
        self.unidade.pack()

        ctk.CTkLabel(self.window, text="Estoque mínimo").pack(pady=5)
        self.estoque_min = ctk.CTkEntry(self.window)
        self.estoque_min.pack()

        botao = ctk.CTkButton(
            self.window,
            text="Cadastrar",
            command=self.cadastrar
        )

        botao.pack(pady=20)

    def cadastrar(self):

        try:

            self.service.cadastrar_produto(
                self.nome.get(),
                self.descricao.get(),
                self.unidade.get(),
                int(self.estoque_min.get()),
                self.categoria.get()
            )

            messagebox.showinfo("Sucesso", "Produto cadastrado")

            self.window.destroy()

        except Exception as e:

            messagebox.showerror("Erro", str(e))