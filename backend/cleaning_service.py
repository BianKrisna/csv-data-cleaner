import pandas as pd
import io

def clean(file_path):
    df = pd.read_csv(io.BytesIO(file_path))
    df.dropna(axis=0, inplace=True)
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

    return df.to_csv(index=False)