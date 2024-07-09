import pandas as pd

ABSOLUTE_PATH="/Users/tomkusak/Desktop/Personal_Coding/Projects/ff-draft-site/app/data/predraft_rankings.csv"
RELATIVE_PATH="app/data/predraft_rankings.csv"

def read_df(path=ABSOLUTE_PATH):
    df = pd.read_csv(path)
    return df

def optimize_roster(roster):
    pass
