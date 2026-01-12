from cleaning_service import CsvCleaner
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from datetime import datetime

app = FastAPI()

@app.post("/upload-csv")
def clean_csv(file: UploadFile = File(...)):
    df = CsvCleaner()
    stream = df.clean(file.file)
    stream.seek(0)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name_file = f"cleaned_data_{timestamp}.csv"

    return StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={name_file}"}
    )

