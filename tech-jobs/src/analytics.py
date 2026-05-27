# Funções de análise e visualização

import plotly.express as px
import pandas as pd
from collections import Counter

def grafico_top_locais(df):
    contagem = df["location"].value_counts().head(10)

    fig = px.bar(
        contagem,
        title="Top 10 localizações com mais vagas"
    )
    return fig

def grafico_top_cargos(df):
    contagem = df["title"].value_counts().head(10)

    fig = px.bar(
        contagem,
        title="Top 10 cargos mais frequentes"
    )

    return fig

def grafico_vagas_tempo(df):
    vagas_por_dia = (
        df.groupby(df["time"].dt.date)
        .size()
        .reset_index(name="quantidade")
    )

    fig = px.line(
        vagas_por_dia,
        x="time",
        y="quantidade",
        title="Vagas publicadas ao longo do tempo"
    )

    return fig

def grafico_tecnologias(df):

    todas_tecnologias = []

    for lista in df["tecnologias"]:
        todas_tecnologias.extend(lista)

    contagem = Counter(todas_tecnologias)

    df_tech = (
        pd.DataFrame(
            contagem.items(),
            columns=["tecnologia", "quantidade"]
        )
        .sort_values(by="quantidade", ascending=False)
        .head(10)
    )

    fig = px.bar(
        df_tech,
        x="tecnologia",
        y="quantidade",
        title="Tecnologias mais pedidas"
    )

    return fig

def grafico_niveis(df):

    contagem = (
        df["nivel"]
        .value_counts()
        .reset_index()
    )

    contagem.columns = ["nivel", "quantidade"]

    fig = px.pie(
        contagem,
        names="nivel",
        values="quantidade",
        title="Distribuição por senioridade",
        hole=0.4
    )

    return fig