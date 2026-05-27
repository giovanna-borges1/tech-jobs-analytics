import os
import pandas as pd

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

df = pd.read_csv(
    os.path.join(BASE_DIR, "data", "vagas.csv")
)