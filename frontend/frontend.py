import streamlit as st
import requests
import re
import os

# 1. Konfigurasi Halaman (Biar terlihat profesional)
st.set_page_config(page_title="CSV_Cleaner", page_icon="👁️")

# 2. Judul dan Deskripsi
st.title("CSV Cleaner Tools")
st.write("Upload CSV file to be cleaned")

# 3. Widget Upload Gambar
uploaded_file = st.file_uploader("Select CSV file...", type=["csv"])


def get_filename_from_response(response, default="result.csv"):
    content_disposition = response.headers.get("content-disposition", "")
    
    match = re.search(r'filename="?([^"]+)"?', content_disposition)
    if match:
        return match.group(1)
    
    return default

# 4. Logika Utama
if uploaded_file is not None:
    
    # Tombol Prediksi
    if st.button("Clean now!"):
        with st.spinner('Processing file...'):
            try:
                # --- CARA KONEK KE API ---
                # Siapkan file untuk dikirim
                # "file" adalah nama parameter yang ditunggu oleh FastAPI nanti
                files = {"file": uploaded_file.getvalue()}
                
                # Tembak ke API (Asumsi jalan di localhost:8000)
                api_url = os.getenv("API_URL", "http://localhost:8000/upload-csv")
                response = requests.post(api_url, files=files)
    
                # Cek status respon
                if response.status_code == 200:
                    filename = get_filename_from_response(response)

                    st.success("Done!")
                    st.download_button(
                        label="⬇️ Download hasil CSV",
                        data=response.content,
                        file_name=filename,
                        mime="text/csv"

                    )
                    
                else:
                    st.error(f"Error API: {response.status_code}")
                    
            except Exception as e:
                st.error(f"Gagal konek ke server. Pastikan API nyala! Error: {e}")

# Sidebar (Pemanis)
st.sidebar.title("About")
st.sidebar.info("This tools made by UPH FAIDAS student using FastAPI & Streamlit.")