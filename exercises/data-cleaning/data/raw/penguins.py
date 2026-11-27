import pandas as pd
from data.config import penguins_url

def load_penguins():
    return pd.read_csv(penguins_url)
