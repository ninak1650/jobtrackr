import streamlit as st
import pandas as pd

st.set_page_config(page_title="jobtrackr", layout="wide")

st.title("📊 jobtrackr")
st.subheader("Your smart job application companion")
st.markdown(
    """
    Welcome to your personal job tracker!
    
    Upload your Excel file to view and explore your job applications.
    - Track which companies replied (and how fast)
    - Visualize patterns over time
    - Get organized, stay sane 🧠
    """
)

# 📂 Upload Section
uploaded_file = st.file_uploader("⬆️ Upload your job tracker (.xlsx)", type=["xlsx"])

# 📋 Show content if file uploaded
if uploaded_file:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    st.success("File uploaded successfully!")
    
    st.subheader("🗂️ Preview of your data")
    st.dataframe(df)
