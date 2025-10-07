import streamlit as st
import pandas as pd
from run_pipeline import run_pipeline
import os

st.set_page_config(page_title="ESG SOCIAL & GRI Labeler", layout="wide")
st.title("📊 ESG SOCIAL FACTOR DETECTION AND GRI CLASSIFICATION")

st.sidebar.header("Upload & Model Selection")

uploaded_file = st.sidebar.file_uploader("Upload PDF", type="pdf")
social_model_path = st.sidebar.text_input("Social Model Path", "D:\Files\KhoaLuan\daily_update\Final_result\Model\PhobertSClassify\checkpoint2360")
gri_model_path = st.sidebar.text_input("GRI Model Path", "D:\Files\KhoaLuan\daily_update\Final_result\Model\VibertGriClassification\checkpoint1295")

if uploaded_file:
    st.sidebar.success("✅ PDF uploaded")

    if st.sidebar.button("Run Pipeline"):
        with st.spinner("Running pipeline... Please wait."):
            input_pdf = "input.pdf"
            output_csv = "D:\Files\KhoaLuan\daily_update\Final_result\TestingResult\output.csv"

            with open(input_pdf, "wb") as f:
                f.write(uploaded_file.read())

            df = run_pipeline(
                pdf_path=input_pdf,
                output_csv_path=output_csv,
                social_model_path=social_model_path,
                gri_model_path=gri_model_path
            )

        st.subheader("✅ Labeled Data")
        st.dataframe(df)

        st.subheader("🔎 EDA")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Distribution of SOCIAL_LABEL**")
            st.bar_chart(df['SOCIAL_LABEL'].value_counts())

        with col2:
            st.markdown("**Distribution of GRI_LABEL**")
            gri_counts = df['GRI_LABEL'][df['GRI_LABEL'] != ""].value_counts()
            if not gri_counts.empty:
                st.bar_chart(gri_counts)
            else:
                st.warning("No GRI labels detected.")

        csv_download = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download CSV",
            data=csv_download,
            file_name='labeled_output.csv',
            mime='text/csv'
        )
