import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px
import io

st.set_page_config(page_title="Almoxarifado Miguel Gurgel", layout="wide")

# ---------------- CONFIGURAÇÃO ----------------
DATA_DIR = "data"
PRODUTOS_FILE = os.path.join(DATA_DIR, "produtos.json")
CATEGORIAS_FILE = os.path.join(DATA_DIR, "categorias.json")
USUARIOS_FILE = os.path.join(DATA_DIR, "usuarios.json")
os.makedirs(DATA_DIR, exist_ok=True)

# ---------------- FUNÇÕES JSON ----------------
def load_json(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# ---------------- LOGIN ----------------
def login_page():
    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        st.image("imgs/logoinicio.png", width=700)

    st.markdown("<h1 style='text-align: center;'>Almoxarifado Miguel Gurgel</h1>", unsafe_allow_html=True)
    st.write("")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        usuarios = load_json(USUARIOS_FILE)
        for u in usuarios:
            if u["usuario"] == usuario and u["senha"] == senha:
                st.session_state.logged = True
                st.session_state.usuario = usuario
                st.rerun()
        st.error("Usuário ou senha inválidos")

    if st.button("Criar conta"):
        st.session_state.page = "register"
        st.rerun()

# ---------------- REGISTRO ----------------
def register_page():
    st.title("Criar conta")
    nome = st.text_input("Nome")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    confirma = st.text_input("Confirmar senha", type="password")

    if st.button("Cadastrar"):
        if senha != confirma:
            st.error("Senhas não coincidem")
            return
        usuarios = load_json(USUARIOS_FILE)
        if any(u["usuario"] == usuario for u in usuarios):
            st.error("Usuário já existe")
            return
        usuarios.append({"nome": nome,"usuario": usuario,"senha": senha})
        save_json(USUARIOS_FILE, usuarios)
        st.success("Conta criada!")

    if st.button("Voltar"):
        st.session_state.page = "login"
        st.rerun()

# ---------------- DASHBOARD ----------------
def dashboard_home():
    st.title("📊 Dashboard")

    produtos = load_json(PRODUTOS_FILE)
    if not produtos:
        st.warning("Nenhum produto cadastrado")
        return

    df = pd.DataFrame(produtos)
    # Adiciona coluna de estoque mínimo caso não exista
    if "estoque_minimo" not in df.columns:
        df["estoque_minimo"] = 0

    total_produtos = len(df)
    total_estoque = df["quantidade"].sum()
    media = df["quantidade"].mean()
    estoque_baixo = df[df["quantidade"] <= df["estoque_minimo"]]

    col1, col2, col3 = st.columns(3)
    col1.metric("Produtos cadastrados", total_produtos)
    col2.metric("Itens em estoque", int(total_estoque))
    col3.metric("Média por produto", round(media,2))

    if not estoque_baixo.empty:
        st.error("⚠ Produtos com estoque baixo")
        st.dataframe(estoque_baixo, width="stretch")

    st.divider()

    col1, col2 = st.columns(2)
    fig1 = px.bar(df, x="nome", y="quantidade", title="Estoque por Produto")
    col1.plotly_chart(fig1, width="stretch")
    fig2 = px.pie(df, names="nome", values="quantidade", title="Distribuição do Estoque")
    col2.plotly_chart(fig2, width="stretch")

    st.divider()
    st.subheader("Tabela de Produtos")
    st.dataframe(df, width="stretch")

    # Exportação CSV
    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button("Exportar para CSV", data=csv_data, file_name="produtos.csv", mime="text/csv")

    # Exportação Excel
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Produtos")
    output.seek(0)
    st.download_button(
        "Exportar para Excel",
        data=output,
        file_name="produtos.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# ---------------- PRODUTOS ----------------
def produtos_page():
    st.title("📦 Produtos")

    produtos = load_json(PRODUTOS_FILE)
    categorias = load_json(CATEGORIAS_FILE)
    categorias_lista = [c["nome"] for c in categorias]

    busca = st.text_input("🔎 Buscar produto")

    with st.expander("Adicionar Produto"):
        nome = st.text_input("Nome do Produto")
        qtd = st.number_input("Quantidade", min_value=0)
        estoque_minimo = st.number_input("Estoque mínimo", min_value=0)
        categoria = st.selectbox("Categoria", categorias_lista if categorias_lista else ["Sem categoria"])

        if st.button("Salvar Produto"):
            if nome.strip() == "":
                st.error("Informe o nome do produto")
            else:
                produtos.append({
                    "nome": nome,
                    "quantidade": qtd,
                    "estoque_minimo": estoque_minimo,
                    "categoria": categoria
                })
                save_json(PRODUTOS_FILE, produtos)
                st.success("Produto salvo!")
                st.rerun()

    st.divider()
    for idx, p in enumerate(produtos):
        if busca and busca.lower() not in p["nome"].lower():
            continue
        col1, col2, col3, col4, col5 = st.columns([4,2,1,1,1])
        col1.write(p["nome"])
        col2.write(f"{p['quantidade']} (mín: {p.get('estoque_minimo', 0)})")

        if col3.button("➕", key=f"add_{idx}"):
            produtos[idx]["quantidade"] += 1
            save_json(PRODUTOS_FILE, produtos)
            st.rerun()
        if col4.button("➖", key=f"remove_{idx}"):
            if produtos[idx]["quantidade"] > 0:
                produtos[idx]["quantidade"] -= 1
                save_json(PRODUTOS_FILE, produtos)
            else:
                st.warning("Estoque zerado")
            st.rerun()
        if col5.button("Excluir", key=f"del_{idx}"):
            produtos.pop(idx)
            save_json(PRODUTOS_FILE, produtos)
            st.rerun()

# ---------------- CATEGORIAS ----------------
def categorias_page():
    st.title("📂 Categorias")
    categorias = load_json(CATEGORIAS_FILE)

    nome = st.text_input("Nome da categoria")
    desc = st.text_input("Descrição")

    if st.button("Salvar categoria"):
        if nome.strip() == "":
            st.error("Informe o nome da categoria")
        else:
            categorias.append({"nome": nome,"descricao": desc})
            save_json(CATEGORIAS_FILE, categorias)
            st.success("Categoria salva")
            st.rerun()

    st.divider()
    if categorias:
        df = pd.DataFrame(categorias)
        st.dataframe(df, width="stretch")
        for idx, c in enumerate(categorias):
            if st.button(f"Excluir {c['nome']}", key=f"del_cat_{idx}"):
                categorias.pop(idx)
                save_json(CATEGORIAS_FILE, categorias)
                st.success(f"Categoria '{c['nome']}' removida")
                st.rerun()

# ---------------- MENU ----------------
def dashboard():
    st.sidebar.title(f"Olá, {st.session_state.usuario}!")
    menu = st.sidebar.radio("Menu", ["Dashboard","Produtos","Categorias","Logout"])
    if menu == "Dashboard":
        dashboard_home()
    elif menu == "Produtos":
        produtos_page()
    elif menu == "Categorias":
        categorias_page()
    elif menu == "Logout":
        st.session_state.logged = False
        st.rerun()

# ---------------- INICIO ----------------
if "logged" not in st.session_state:
    st.session_state.logged = False
if "page" not in st.session_state:
    st.session_state.page = "login"

if not st.session_state.logged:
    if st.session_state.page == "login":
        login_page()
    else:
        register_page()
else:
    dashboard()