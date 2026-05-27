# Dashboard principal do projeto
# Tech Jobs Analytics

import streamlit as st 
from data_loader import carregar_dados 
from transform import limpar_dados, TECNOLOGIAS
from analytics import (
    grafico_top_locais,
    grafico_top_cargos,
    grafico_vagas_tempo,
    grafico_tecnologias,
    grafico_niveis
)

df = carregar_dados()
df = limpar_dados(df)

st.title("Tech Jobs Analytics")

st.markdown("""
Análise de vagas de tecnologia com Python,
Pandas, NLP e Streamlit.
""")

st.sidebar.title("Filtros")

localizacoes = st.sidebar.selectbox(
    "Escolha uma localização",
    df["location"].unique()
)

nivel = st.sidebar.multiselect(
    "Senioridade",
    options=df["nivel"].unique()
)

tecnologia = st.sidebar.selectbox(
    "Tecnologia",
    options=["Todas"] + TECNOLOGIAS
)

df_filtrado = df.copy()

# filtro localização
if localizacoes:
    df_filtrado = df_filtrado[
        df_filtrado["location"] == localizacoes
    ]

# filtro senioridade
if nivel:
    df_filtrado = df_filtrado[
        df_filtrado["nivel"].isin(nivel)
    ]

# filtro tecnologia
if tecnologia != "Todas":

    df_filtrado = df_filtrado[
        df_filtrado["tecnologias"]
        .apply(lambda lista: tecnologia in lista)
    ]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Vagas", len(df_filtrado))
col2.metric("Cargos únicos", df_filtrado["title"].nunique())
col3.metric("Localizações", df_filtrado["location"].nunique())
col4.metric("Skills", len(TECNOLOGIAS))

st.dataframe(df_filtrado)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        grafico_top_locais(df_filtrado),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        grafico_top_cargos(df_filtrado),
        use_container_width=True
    )

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        grafico_tecnologias(df_filtrado),
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        grafico_niveis(df_filtrado),
        use_container_width=True
    )

st.plotly_chart(
    grafico_vagas_tempo(df_filtrado),
    use_container_width=True
)

