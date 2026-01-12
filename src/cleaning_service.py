import pandas as pd
import io

class CsvCleaner:
    def __init__(self, file_path):
        self.path = file_path
        
    def clean(self):
        df = pd.read_csv(self.path)
        df.dropna(axis=0, inplace=True)
        df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

        stream = io.StringIO()
        df.to_csv(stream, index=False)
        return stream