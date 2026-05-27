# Funções de limpeza e transformação dos dados

import pandas as pd 
import re

def limpar_dados(df):
    df = df.copy()

# remover linhas vazias importantes
    df = df.dropna(subset=["location", "title", "desc"])

# padronizar textos
    df["location"] = df["location"].str.strip().str.title()
    df["title"] = df["title"].str.strip().str.lower()

# remover duplicados
    df = df.drop_duplicates()

    df["time"] = pd.to_datetime(
    df["time"],
    dayfirst=True,
    errors="coerce"
)
    df["tecnologias"] = df["desc"].apply(extrair_tecnologias)

    df["nivel"] = df["title"].apply(detectar_nivel)

    return df

TECNOLOGIAS = [
    "python",
    "sql",
    "power bi",
    "excel",
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "spark",
    "pandas",
    "tableau",
    "tensorflow",
    "pytorch",
    "java",
    "scala",
    "hadoop"
]

def extrair_tecnologias(texto):
    texto = str(texto).lower()

    encontradas = []

    for tech in TECNOLOGIAS:
        if tech in texto:
            encontradas.append(tech)

    return encontradas

def detectar_nivel(texto):

    texto = str(texto).lower()

    if re.search(r"\bjunior\b|\bjr\b", texto):
        return "junior"

    elif re.search(r"\bpleno\b|\bmid\b", texto):
        return "pleno"

    elif re.search(r"\bsenior\b|\bsr\b", texto):
        return "senior"

    return "não informado"