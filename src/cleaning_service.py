import pandas as pd
import io

class CsvCleaner:

    @staticmethod
    def clean(file_path):
        df = pd.read_csv(file_path)
        df.dropna(axis=0, inplace=True)
        df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

        stream = io.StringIO()
        df.to_csv(stream, index=False)
        stream.seek(0)
        return stream