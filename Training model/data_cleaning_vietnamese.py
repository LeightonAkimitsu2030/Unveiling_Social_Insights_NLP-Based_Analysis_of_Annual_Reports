import pandas as pd
import re

# Load input file
df = pd.read_excel("Input") #, sheet_name="2_steps_translator_data")

# Vietnamese text cleaning function
def clean_vietnamese_text(text: str) -> str:
    if pd.isna(text):
        return ""
    t = str(text).lower()
    t = re.sub(r"http\\S+|www\\.\\S+", " ", t)        # delete URL
    t = re.sub(r"@\\w+|#\\w+", " ", t)                # delete mentions, hashtags
    t = re.sub(r"[^\w\\sÀ-ỹ.,!?–-]", "", t)           # only keep Vietnamese characters, numbers, some punctuation marks
    t = re.sub(r"\\s+", " ", t).strip()               # whitespace normalization
    return t

# Clean up the relevant columns
df['Sentences'] = df['Sentences'].apply(clean_vietnamese_text)
if 'GRI_classification' in df.columns:
    df['RI_classification'] = df['GRI_classification'].apply(clean_vietnamese_text)

# Optional: remove rows with 'Sentence' not empty but missing 'GRI_classification'
if 'GRI_classification' in df.columns:
    df = df[~((df['Sentences'].notna()) & (df['Câu'].str.strip() != "") & 
              (df['GGRI_classification'].isna() | (df['GRI_classification'].str.strip() == "")))]

# Lưu ra file Excel
df.to_excel("Output file", index=False)
print("✅ The file has been cleaned and saved.")