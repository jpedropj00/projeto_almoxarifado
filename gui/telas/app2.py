import customtkinter as ctk

from gui.login_window import LoginWindow


def main():

    # Configuração visual global
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Iniciar tela de login
    LoginWindow()


if __name__ == "__main__":
    main()