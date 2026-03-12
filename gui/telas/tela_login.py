import customtkinter as ctk
from tkinter import messagebox

from services.usuario_service import UsuarioService
from gui.tela_dashboard import Dashboard

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class LoginWindow:

    def __init__(self):

        self.usuario_service = UsuarioService()

        self.root = ctk.CTk()
        self.root.title("ALMOXARIFADO MG")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

        self.criar_interface()

        self.root.mainloop()

    def criar_interface(self):

        # ===== Frame esquerdo =====
        frame_left = ctk.CTkFrame(self.root, width=450, corner_radius=0)
        frame_left.pack(side="left", fill="both")

        titulo = ctk.CTkLabel(
            frame_left,
            text="📦 ALMOXARIFADO MG",
            font=ctk.CTkFont(size=34, weight="bold")
        )
        titulo.pack(pady=150)

        subtitulo = ctk.CTkLabel(
            frame_left,
            text="Sistema de Gestão de Estoque",
            font=ctk.CTkFont(size=16)
        )
        subtitulo.pack()

        # ===== Frame direito =====
        frame_right = ctk.CTkFrame(self.root)
        frame_right.pack(side="right", fill="both", expand=True)

        titulo_login = ctk.CTkLabel(
            frame_right,
            text="Acessar Sistema",
            font=ctk.CTkFont(size=26, weight="bold")
        )
        titulo_login.pack(pady=50)

        # Campo Email
        self.entry_email = ctk.CTkEntry(
            frame_right,
            placeholder_text="Email",
            width=260
        )
        self.entry_email.pack(pady=10)

        # Campo Senha
        self.entry_senha = ctk.CTkEntry(
            frame_right,
            placeholder_text="Senha",
            show="*",
            width=260
        )
        self.entry_senha.pack(pady=10)

        # Botão Login
        botao_login = ctk.CTkButton(
            frame_right,
            text="Entrar",
            width=220,
            height=40,
            command=self.fazer_login
        )
        botao_login.pack(pady=30)

        # Login com Enter
        self.root.bind("<Return>", lambda e: self.fazer_login())

    def fazer_login(self):

        email = self.entry_email.get()
        senha = self.entry_senha.get()

        try:

            usuario = self.usuario_service.autenticar_usuario(email, senha)

            messagebox.showinfo("Sucesso", f"Bem-vindo {usuario.nome}")

            self.root.destroy()

            Dashboard(usuario)

        except Exception as e:

            messagebox.showerror("Erro", str(e))