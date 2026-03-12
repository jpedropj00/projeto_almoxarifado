import customtkinter as ctk
from tkinter import ttk, messagebox

from services.produto_service import ProdutoService
from services.movimentacao_service import MovimentacaoService


class MovimentacaoWindow:

    def __init__(self, parent, usuario):

        self.usuario = usuario

        self.produto_service = ProdutoService()
        self.mov_service = MovimentacaoService()

        self.window = ctk.CTkToplevel(parent)
        self.window.title("Movimentação de Estoque")
        self.window.geometry("900x600")

        self.produtos = self.produto_service.listar_produtos()

        self.criar_interface()
        self.carregar_movimentacoes()

    # -----------------------------------

    def criar_interface(self):

        titulo = ctk.CTkLabel(
            self.window,
            text="🔄 Movimentação de Estoque",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        titulo.pack(pady=10)

        frame_form = ctk.CTkFrame(self.window)
        frame_form.pack(pady=10)

        # Produto
        ctk.CTkLabel(frame_form, text="Produto").grid(row=0, column=0, padx=10)

        nomes_produtos = [p.nome for p in self.produtos]

        self.combo_produto = ctk.CTkComboBox(
            frame_form,
            values=nomes_produtos
        )

        self.combo_produto.grid(row=0, column=1, padx=10)

        # Quantidade
        ctk.CTkLabel(frame_form, text="Quantidade").grid(row=0, column=2)

        self.entry_qtd = ctk.CTkEntry(frame_form, width=100)
        self.entry_qtd.grid(row=0, column=3, padx=10)

        # Tipo
        ctk.CTkLabel(frame_form, text="Tipo").grid(row=0, column=4)

        self.tipo = ctk.CTkOptionMenu(
            frame_form,
            values=["ENTRADA", "SAIDA"]
        )

        self.tipo.grid(row=0, column=5, padx=10)

        # Observação
        ctk.CTkLabel(frame_form, text="Observação").grid(row=1, column=0)

        self.obs = ctk.CTkEntry(frame_form, width=300)
        self.obs.grid(row=1, column=1, columnspan=3, pady=10)

        # Botão movimentar
        btn = ctk.CTkButton(
            frame_form,
            text="Registrar Movimentação",
            command=self.registrar_movimentacao
        )

        btn.grid(row=1, column=4, columnspan=2, padx=10)

        # ---------------------------

        # TABELA
        frame_tabela = ctk.CTkFrame(self.window)
        frame_tabela.pack(fill="both", expand=True, pady=20)

        self.tabela = ttk.Treeview(
            frame_tabela,
            columns=("produto", "tipo", "quantidade", "data"),
            show="headings"
        )

        self.tabela.heading("produto", text="Produto")
        self.tabela.heading("tipo", text="Tipo")
        self.tabela.heading("quantidade", text="Quantidade")
        self.tabela.heading("data", text="Data")

        self.tabela.pack(fill="both", expand=True)
        # TAGS DE CORES
        self.tabela.tag_configure("entrada", foreground="green")
        self.tabela.tag_configure("saida", foreground="red")

    # -----------------------------------

    def registrar_movimentacao(self):

        try:

            nome_produto = self.combo_produto.get()
            quantidade = int(self.entry_qtd.get())
            tipo = self.tipo.get()
            observacao = self.obs.get()

            produto = next(p for p in self.produtos if p.nome == nome_produto)

            self.mov_service.registrar_movimentacao(
                produto.id,
                self.usuario.id,
                quantidade,
                tipo,
                observacao
            )

            messagebox.showinfo("Sucesso", "Movimentação registrada")

            self.carregar_movimentacoes()

        except Exception as e:

            messagebox.showerror("Erro", str(e))

    # -----------------------------------

    def carregar_movimentacoes(self):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        movimentacoes = self.mov_service.listar_movimentacoes()

        for mov in movimentacoes:

            produto = next(
                p.nome for p in self.produtos if p.id == mov.id_produto
            )

            tag = "entrada" if mov.tipo == "ENTRADA" else "saida"

            self.tabela.insert(
                "",
                "end",
                values=(
                    produto,
                    mov.tipo,
                    mov.quantidade,
                    mov.data.strftime("%d/%m/%Y")
                ),
                tags=(tag,)
            )