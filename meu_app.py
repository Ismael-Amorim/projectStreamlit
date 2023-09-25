import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu Site Streamlit")

with st.container():
    st.subheader("Meu primeiro site com Streamlit")
    st.title("Dashboard de Contratos")
    st.write("informações sobre os contratos fechados pela Amorim Systems do longo de maio.")

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    st.subheader("Este é um gráfico de área.")
    qtd_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
    num_dias = int(qtd_dias.replace("D",""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")
    
with st.container():
    st.write("---")
    st.subheader("Este é um gráfico de colunas.")
    st.bar_chart(dados,x="Data", y="Contratos")
    
with st.container():
    st.write("---")
    st.subheader("Este é um gráfico de linhas.")
    st.line_chart(dados,x="Data", y="Contratos", height=0)