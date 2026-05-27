import pandas as pd

def carregar_dados():
    df = pd.read_csv("tech-jobs/data/vagas.csv")
    return df