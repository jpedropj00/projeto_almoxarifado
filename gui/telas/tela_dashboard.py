import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from services.produto_service import ProdutoService
from services.movimentacao_service import MovimentacaoService


class Dashboard:

    def __init__(self, usuario):

        self.usuario = usuario

        self.produto_service = ProdutoService()
        self.mov_service = MovimentacaoService()

        self.root = ctk.CTk()
        self.root.title("ALMOXARIFADO MG - Dashboard")
        self.root.geometry("1200x700")

        self.criar_layout()

        self.root.mainloop()

    # ----------------------------------

    def criar_layout(self):

        menu = ctk.CTkFrame(self.root, width=220)
        menu.pack(side="left", fill="y")

        titulo = ctk.CTkLabel(
            menu,
            text="📦 ALMOXARIFADO MG",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        titulo.pack(pady=20)

        usuario_label = ctk.CTkLabel(
            menu,
            text=f"Usuário: {self.usuario.nome}"
        )
        usuario_label.pack(pady=10)

        # Área principal
        self.frame_main = ctk.CTkFrame(self.root)
        self.frame_main.pack(expand=True, fill="both")

        self.criar_graficos()
        self.alerta_estoque()
        self.ultimas_movimentacoes()

    # ----------------------------------

    def criar_graficos(self):

        produtos = self.produto_service.listar_produtos()

        nomes = [p.nome for p in produtos]
        quantidades = [p.quantidade_atual for p in produtos]

        categorias = {}
        for p in produtos:
            categorias[p.nome_categoria] = categorias.get(p.nome_categoria, 0) + 1

        fig, axs = plt.subplots(1, 3, figsize=(12,4))

        # 📊 Gráfico 1 - Estoque por produto
        axs[0].bar(nomes, quantidades)
        axs[0].set_title("Estoque por Produto")
        axs[0].tick_params(axis='x', rotation=45)

        # 📊 Gráfico 2 - Produtos por categoria
        axs[1].pie(
            categorias.values(),
            labels=categorias.keys(),
            autopct="%1.0f%%"
        )
        axs[1].set_title("Produtos por Categoria")

        # 📊 Gráfico 3 - Produtos com menos estoque
        produtos_baixos = [
            p for p in produtos
            if p.quantidade_atual <= p.estoque_minimo
        ]

        nomes_baixos = [p.nome for p in produtos_baixos]
        qtd_baixos = [p.quantidade_atual for p in produtos_baixos]

        axs[2].bar(nomes_baixos, qtd_baixos)
        axs[2].set_title("Estoque Baixo")
        axs[2].tick_params(axis='x', rotation=45)

        canvas = FigureCanvasTkAgg(fig, master=self.frame_main)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)

    # ----------------------------------

    def alerta_estoque(self):

        produtos = self.produto_service.listar_produtos()

        produtos_baixos = [
            p for p in produtos
            if p.quantidade_atual <= p.estoque_minimo
        ]

        if produtos_baixos:

            alerta_frame = ctk.CTkFrame(self.frame_main)
            alerta_frame.pack(pady=10)

            titulo = ctk.CTkLabel(
                alerta_frame,
                text="⚠ ALERTA DE ESTOQUE BAIXO",
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color="red"
            )

            titulo.pack(pady=5)

            for p in produtos_baixos:

                texto = f"{p.nome} - Estoque atual: {p.quantidade_atual}"

                label = ctk.CTkLabel(alerta_frame, text=texto)

                label.pack()

    # ----------------------------------

    def ultimas_movimentacoes(self):

        movimentacoes = self.mov_service.listar_movimentacoes()

        titulo = ctk.CTkLabel(
            self.frame_main,
            text="🔄 Últimas Movimentações",
            font=ctk.CTkFont(size=16, weight="bold")
        )

        titulo.pack(pady=10)

        for mov in movimentacoes[-5:]:

            texto = f"{mov.data.strftime('%d/%m')} | Produto {mov.id_produto} | Qtd {mov.quantidade}"

            label = ctk.CTkLabel(
                self.frame_main,
                text=texto
            )

            label.pack()