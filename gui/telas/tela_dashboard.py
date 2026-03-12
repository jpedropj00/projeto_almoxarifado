import customtkinter as ctk

from gui.produto_lista import ProdutoLista
from gui.produto_cadastro import ProdutoCadastro
from gui.movimentacao_window import MovimentacaoWindow


class Dashboard:

    def __init__(self, usuario):

        self.usuario = usuario

        self.root = ctk.CTk()
        self.root.title("ALMOXARIFADO MG")
        self.root.geometry("1200x700")

        self.criar_layout()

        self.root.mainloop()

    # --------------------------------

    def criar_layout(self):

        # MENU LATERAL
        self.menu = ctk.CTkFrame(self.root, width=220)
        self.menu.pack(side="left", fill="y")

        titulo = ctk.CTkLabel(
            self.menu,
            text="📦 ALMOXARIFADO MG",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        titulo.pack(pady=20)

        usuario = ctk.CTkLabel(
            self.menu,
            text=f"Usuário:\n{self.usuario.nome}"
        )
        usuario.pack(pady=10)

        # BOTÕES DO MENU

        btn_dashboard = ctk.CTkButton(
            self.menu,
            text="📊 Dashboard",
            command=self.mostrar_dashboard
        )
        btn_dashboard.pack(fill="x", pady=5, padx=10)

        btn_produtos = ctk.CTkButton(
            self.menu,
            text="📦 Listar Produtos",
            command=self.abrir_lista_produtos
        )
        btn_produtos.pack(fill="x", pady=5, padx=10)

        btn_cadastrar = ctk.CTkButton(
            self.menu,
            text="➕ Cadastrar Produto",
            command=self.abrir_cadastro_produto
        )
        btn_cadastrar.pack(fill="x", pady=5, padx=10)

        btn_mov = ctk.CTkButton(
            self.menu,
            text="🔄 Movimentações",
            command=self.abrir_movimentacao
        )
        btn_mov.pack(fill="x", pady=5, padx=10)

        btn_relatorios = ctk.CTkButton(
            self.menu,
            text="📑 Relatórios",
            command=self.relatorio
        )
        btn_relatorios.pack(fill="x", pady=5, padx=10)

        btn_sair = ctk.CTkButton(
            self.menu,
            text="🚪 Sair",
            fg_color="red",
            command=self.root.destroy
        )
        btn_sair.pack(side="bottom", pady=20, padx=10, fill="x")

        # AREA PRINCIPAL
        self.frame_principal = ctk.CTkFrame(self.root)
        self.frame_principal.pack(side="right", expand=True, fill="both")

        self.mostrar_dashboard()

    # --------------------------------

    def limpar_frame(self):

        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    # --------------------------------

    def mostrar_dashboard(self):

        self.limpar_frame()

        label = ctk.CTkLabel(
            self.frame_principal,
            text="📊 Dashboard do Sistema",
            font=ctk.CTkFont(size=24, weight="bold")
        )

        label.pack(pady=40)

    # --------------------------------

    def abrir_lista_produtos(self):

        ProdutoLista(self.root)

    # --------------------------------

    def abrir_cadastro_produto(self):

        ProdutoCadastro(self.root)

    # --------------------------------

    def abrir_movimentacao(self):

        MovimentacaoWindow(self.root, self.usuario)

    # --------------------------------

    def relatorio(self):

        self.limpar_frame()

        label = ctk.CTkLabel(
            self.frame_principal,
            text="📑 Área de Relatórios",
            font=ctk.CTkFont(size=20)
        )

        label.pack(pady=40)