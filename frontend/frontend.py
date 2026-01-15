import streamlit as st
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.cleaning_service import clean


st.set_page_config(page_title="CSV_Cleaner", page_icon="👁️")


st.title("CSV Cleaner Tools")
st.write("Upload CSV file to be cleaned")


uploaded_file = st.file_uploader("Select CSV file...", type=["csv"])



if uploaded_file is not None:
    

    if st.button("Clean now!"):
        with st.spinner('Processing file...'):
            try:

                bytes_data = uploaded_file.getvalue()
                result_csv = clean(bytes_data)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                name_file = f"cleaned_data_{timestamp}.csv"

                st.success("Done!")
                st.download_button("Download!", result_csv, name_file)
                    
            except Exception as e:
                st.error(f"Error: {e}")

# Sidebar (Pemanis)
st.sidebar.title("About")
st.sidebar.info("This tools made by UPH FAIDAS student using FastAPI & Streamlit.")