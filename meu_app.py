import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Ismael Amorim Data Analyst"
)

st.title('Ismael Amorim - Analista de Dados')
 
# Guias / Abas de navegação
titulos_guias = ['Apresentação', 'Dashboards', 'KPIs', 'Projetos pessoais']
guias = st.tabs(titulos_guias)

with guias[0]:
    st.title('Sobre')
    st.write("Atualmente aprofundo meus conhecimentos em Análise de Dados, tenho mais de 4 anos de experiência na área.")
    st.write("Conhecimento intermediário em inglês.")
    st.write("Como linguagem de programação tenho conhecimento em PHP, JavaScript, CSS, Bootstap, banco de dados SQL.")
    st.write("Comecei na área com Excel, atualmente tenho fortes conhecimentos na ferramenta. Os principais projetos profissionais em análise de dados que desenvolvi são:")
    st.write("Indicadores de atendimento,")
    st.write("Indicadores de entregas,")
    st.write("Indicadores de armazenamento.")
    st.write("Até o momento, o Excel é meu ponto forte para análise de dados. Estou aprofundando meus conhecimentos em Machine Learning e Python com suas bibliotecas para análise de dados como Pandas, Plotly, Streamlit, Dash e também SQL para ter um melhor desempenho em análises.")
    st.write("---")
    st.title("Ferramentas para análise de dados")
    st.write("Excel")
    st.write("Looker Studio")
    st.write("Python")
    st.write("Pandas")
    st.write("SQL")
    st.write("---")
    st.title("Experiências")
    st.subheader("Autopeças OK Distribuidora Automotiva")
    st.write("Assistente de controladoria")
    st.write("Responsável por auditoria de processos, auditoria de caixa, controles financeiros, elaboração de indicadores.")
    st.write("Líder de logística")
    st.write("Líder da equipe de separação e expedição de pedidos, recebimento de mercadorias, armazenamento.")
    st.write("Assistente de logística")
    st.write("Faturamento de notas fiscais, elaboração de indicadores.")
    st.write("---")

    
with guias[1]:
    st.title('Dashboards')
    
    with st.container():
        st.header("Dashboards com Python:")
        st.subheader("Dashboard de Contratos")
        st.write("informações sobre os contratos fechados pela Amorim Systems do longo de maio.")

    @st.cache_data
    def carregar_dados():
        tabela = pd.read_csv("resultados.csv")
        return tabela

    with st.container():
        st.write("---")
        st.subheader("Gráfico de área.")
        qtd_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
        num_dias = int(qtd_dias.replace("D",""))
        dados = carregar_dados()
        dados = dados[-num_dias:]
        st.area_chart(dados, x="Data", y="Contratos")
        
    with st.container():
        st.write("---")
        st.subheader("Gráfico de colunas.")
        st.bar_chart(dados,x="Data", y="Contratos")
        
    with st.container():
        st.write("---")
        st.subheader("Gráfico de linhas.")
        st.line_chart(dados,x="Data", y="Contratos", height=0)
        
    with st.container():
        st.header("Dashboards com Looker Studio:")
        st.subheader("Dashboard Google Ads e Analytcs")
        image1 = Image.open('Dashboard-2.jpg')
        st.image(image1, caption='Análise completa')
        image2 = Image.open('Dashboard-1.jpg')
        st.image(image2, caption='Análise completa')
        
        

 
with guias[2]:
    st.header('KPIs')
    st.write('Aqui estarão os KPIs, gráficos e explicações de cada um.')
    
with guias[3]:
    st.header('Projetos pessoais')
    st.write('Aqui estarão meus projetos pessoais em geral.')
 


