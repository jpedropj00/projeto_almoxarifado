import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# ---------------- CONFIGURAÇÃO DE ARQUIVOS ----------------
DATA_DIR = "data"

PRODUTOS_FILE = os.path.join(DATA_DIR, "produtos.json")
CATEGORIAS_FILE = os.path.join(DATA_DIR, "categorias.json")
USUARIOS_FILE = os.path.join(DATA_DIR, "usuarios.json")

os.makedirs(DATA_DIR, exist_ok=True)

# ---------------- TEMA VISUAL ----------------
BG = "#1e1e2f"
SIDEBAR = "#151521"
CARD = "#27293d"
BTN = "#4a90e2"
BTN_HOVER = "#357ab8"
TEXT = "#ffffff"

# ---------------- FUNÇÕES JSON ----------------
def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# ---------------- APLICATIVO PRINCIPAL ----------------
class AlmoxarifadoApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Sistema de Almoxarifado")
        self.geometry("1000x600")
        self.configure(bg=BG)

        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Treeview",
            background="#2a2d3e",
            foreground="white",
            rowheight=25,
            fieldbackground="#2a2d3e"
        )

        style.map(
            "Treeview",
            background=[("selected", "#4a90e2")]
        )

        container = tk.Frame(self, bg=BG)
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, RegisterPage, Dashboard, ProdutosPage, CategoriasPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

# ---------------- LOGIN ----------------
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG)

        self.controller = controller

        box = tk.Frame(self, bg=CARD, width=350, height=330)
        box.place(relx=0.5, rely=0.5, anchor="center")
        box.pack_propagate(False)

        tk.Label(
            box,
            text="ALMOXARIFADO MG",
            bg=CARD,
            fg="white",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        tk.Label(box, text="Usuário", bg=CARD, fg="white").pack()
        self.user = tk.Entry(box)
        self.user.pack(pady=5)

        tk.Label(box, text="Senha", bg=CARD, fg="white").pack()
        self.password = tk.Entry(box, show="*")
        self.password.pack(pady=5)

        tk.Button(
            box,
            text="Entrar",
            bg=BTN,
            fg="white",
            width=20,
            height=2,
            bd=0,
            command=self.login
        ).pack(pady=10)

        tk.Button(
            box,
            text="Criar conta",
            bg="#555",
            fg="white",
            width=20,
            command=lambda: controller.show_frame(RegisterPage)
        ).pack()

    def login(self):

        user = self.user.get()
        password = self.password.get()

        usuarios = load_json(USUARIOS_FILE)

        for u in usuarios:
            if u["usuario"] == user and u["senha"] == password:
                self.controller.show_frame(Dashboard)
                return

        messagebox.showerror("Erro", "Usuário ou senha inválidos")

# ---------------- CADASTRO ----------------
class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG)

        self.controller = controller

        box = tk.Frame(self, bg=CARD, width=400, height=420)
        box.place(relx=0.5, rely=0.5, anchor="center")
        box.pack_propagate(False)

        tk.Label(
            box,
            text="Criar Conta",
            font=("Arial", 24, "bold"),
            bg=CARD,
            fg="white"
        ).pack(pady=20)

        tk.Label(box, text="Nome", bg=CARD, fg="white").pack()
        self.nome = tk.Entry(box)
        self.nome.pack(pady=5)

        tk.Label(box, text="Usuário", bg=CARD, fg="white").pack()
        self.usuario = tk.Entry(box)
        self.usuario.pack(pady=5)

        tk.Label(box, text="Senha", bg=CARD, fg="white").pack()
        self.senha = tk.Entry(box, show="*")
        self.senha.pack(pady=5)

        tk.Label(box, text="Confirmar Senha", bg=CARD, fg="white").pack()
        self.confirma = tk.Entry(box, show="*")
        self.confirma.pack(pady=5)

        tk.Button(
            box,
            text="Cadastrar",
            bg=BTN,
            fg="white",
            width=20,
            height=2,
            bd=0,
            command=self.cadastrar
        ).pack(pady=15)

        tk.Button(
            box,
            text="Voltar para Login",
            bg="#555",
            fg="white",
            command=lambda: controller.show_frame(LoginPage)
        ).pack()

    def cadastrar(self):

        nome = self.nome.get()
        usuario = self.usuario.get()
        senha = self.senha.get()
        confirma = self.confirma.get()

        if not nome or not usuario or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos")
            return

        if senha != confirma:
            messagebox.showerror("Erro", "Senhas não coincidem")
            return

        usuarios = load_json(USUARIOS_FILE)

        for u in usuarios:
            if u["usuario"] == usuario:
                messagebox.showerror("Erro", "Usuário já existe")
                return

        usuarios.append({
            "nome": nome,
            "usuario": usuario,
            "senha": senha
        })

        save_json(USUARIOS_FILE, usuarios)

        messagebox.showinfo("Sucesso", "Usuário cadastrado!")

        self.controller.show_frame(LoginPage)

# ---------------- DASHBOARD ----------------
class Dashboard(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG)

        sidebar = tk.Frame(self, bg=SIDEBAR, width=200)
        sidebar.pack(side="left", fill="y")

        content = tk.Frame(self, bg=BG)
        content.pack(side="right", fill="both", expand=True)

        tk.Label(
            sidebar,
            text="ALMOX",
            bg=SIDEBAR,
            fg="white",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        tk.Button(
            sidebar,
            text="Produtos",
            bg=BTN,
            fg="white",
            width=18,
            height=2,
            bd=0,
            command=lambda: controller.show_frame(ProdutosPage)
        ).pack(pady=10)

        tk.Button(
            sidebar,
            text="Categorias",
            bg=BTN,
            fg="white",
            width=18,
            height=2,
            bd=0,
            command=lambda: controller.show_frame(CategoriasPage)
        ).pack(pady=10)

        tk.Button(
            sidebar,
            text="Sair",
            bg="#444",
            fg="white",
            width=18,
            height=2,
            bd=0,
            command=lambda: controller.show_frame(LoginPage)
        ).pack(pady=10)

        tk.Label(
            content,
            text="Dashboard",
            font=("Arial", 28, "bold"),
            bg=BG,
            fg="white"
        ).pack(pady=30)

        self.produtos = tk.Label(
            content,
            text=f"Produtos cadastrados: {len(load_json(PRODUTOS_FILE))}",
            font=("Arial", 16),
            bg=BG,
            fg="white"
        )
        self.produtos.pack(pady=10)

        self.categorias = tk.Label(
            content,
            text=f"Categorias cadastradas: {len(load_json(CATEGORIAS_FILE))}",
            font=("Arial", 16),
            bg=BG,
            fg="white"
        )
        self.categorias.pack(pady=10)

# ---------------- CATEGORIAS ----------------
class CategoriasPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG)

        tk.Label(self, text="Categorias", font=("Arial", 22), bg=BG, fg="white").pack(pady=10)

        form = tk.Frame(self, bg=BG)
        form.pack()

        tk.Label(form, text="Nome", bg=BG, fg="white").grid(row=0, column=0)
        self.nome = tk.Entry(form)
        self.nome.grid(row=0, column=1)

        tk.Label(form, text="Descrição", bg=BG, fg="white").grid(row=1, column=0)
        self.desc = tk.Entry(form)
        self.desc.grid(row=1, column=1)

        tk.Button(
            form,
            text="Cadastrar",
            bg=BTN,
            fg="white",
            bd=0,
            command=self.add_categoria
        ).grid(row=2, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self, columns=("nome", "descricao"), show="headings")

        self.tree.heading("nome", text="Nome")
        self.tree.heading("descricao", text="Descrição")

        self.tree.pack(fill="both", expand=True, pady=10)

        tk.Button(
            self,
            text="Voltar",
            bg=BTN,
            fg="white",
            command=lambda: controller.show_frame(Dashboard)
        ).pack(pady=10)

        self.refresh()

    def add_categoria(self):

        nome = self.nome.get()
        desc = self.desc.get()

        if not nome:
            messagebox.showerror("Erro", "Nome obrigatório")
            return

        categorias = load_json(CATEGORIAS_FILE)

        categorias.append({
            "nome": nome,
            "descricao": desc
        })

        save_json(CATEGORIAS_FILE, categorias)

        self.nome.delete(0, tk.END)
        self.desc.delete(0, tk.END)

        self.refresh()

    def refresh(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        for c in load_json(CATEGORIAS_FILE):
            self.tree.insert("", "end", values=(c["nome"], c["descricao"]))

# ---------------- PRODUTOS ----------------
class ProdutosPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG)

        tk.Label(self, text="Produtos", font=("Arial", 22), bg=BG, fg="white").pack(pady=10)

        form = tk.Frame(self, bg=BG)
        form.pack()

        tk.Label(form, text="Nome", bg=BG, fg="white").grid(row=0, column=0)
        self.nome = tk.Entry(form)
        self.nome.grid(row=0, column=1)

        tk.Label(form, text="Quantidade", bg=BG, fg="white").grid(row=1, column=0)
        self.qtd = tk.Entry(form)
        self.qtd.grid(row=1, column=1)

        tk.Button(
            form,
            text="Cadastrar",
            bg=BTN,
            fg="white",
            bd=0,
            command=self.add_produto
        ).grid(row=2, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self, columns=("nome", "qtd"), show="headings")

        self.tree.heading("nome", text="Nome")
        self.tree.heading("qtd", text="Quantidade")

        self.tree.pack(fill="both", expand=True, pady=10)

        tk.Button(
            self,
            text="Voltar",
            bg=BTN,
            fg="white",
            command=lambda: controller.show_frame(Dashboard)
        ).pack(pady=10)

        self.refresh()

    def add_produto(self):

        nome = self.nome.get()
        qtd = self.qtd.get()

        if not nome or not qtd.isdigit():
            messagebox.showerror("Erro", "Dados inválidos")
            return

        produtos = load_json(PRODUTOS_FILE)

        produtos.append({
            "nome": nome,
            "quantidade": int(qtd)
        })

        save_json(PRODUTOS_FILE, produtos)

        self.nome.delete(0, tk.END)
        self.qtd.delete(0, tk.END)

        self.refresh()

    def refresh(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        for p in load_json(PRODUTOS_FILE):
            self.tree.insert("", "end", values=(p["nome"], p["quantidade"]))

# ---------------- EXECUÇÃO ----------------
if __name__ == "__main__":
    app = AlmoxarifadoApp()
    app.mainloop()