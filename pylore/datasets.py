import importlib.resources
import pandas as pd


def hello():
    print("Hello")

def load_fangraphs_batting_2024():
    with importlib.resources.open_text('pylore.data', 'fangraphs-batting-2024.csv') as f:
        return pd.read_csv(f)
