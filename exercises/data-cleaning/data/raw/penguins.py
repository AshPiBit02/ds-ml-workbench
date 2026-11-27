import pandas as pd

penguins_url = (
    "https://raw.githubusercontent.com/allisonhorst/"
    "palmerpenguins/main/inst/extdata/penguins.csv"
)

raw_penguins = pd.read_csv(penguins_url)