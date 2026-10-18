import pandas as pd


def make_table(names, scores):
    """pandas: будує DataFrame і повертає середній бал."""
    df = pd.DataFrame({"name": names, "score": scores})
    return df, df["score"].mean()
