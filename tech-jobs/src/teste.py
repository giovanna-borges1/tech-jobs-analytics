import pandas as pd
import plotly.express as px

df = pd.read_csv("tech-jobs/data/vagas.csv")

localizacoes = df["location"].value_counts().head(10)

grafico = px.bar(
    localizacoes,
    title="Top 10 localizações com mais vagas"
)

grafico.show()
