from pdf_to_csv import extract_sentences_from_pdf
from social_detector import load_social_model, predict_social_label
from gri_classifier import load_gri_model, predict_gri_label
from utils import save_final_csv


import torch

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

def run_pipeline(pdf_path, output_csv_path, social_model_path, gri_model_path):
    print("[INFO] Extracting sentences from PDF...")
    df = extract_sentences_from_pdf(pdf_path)

    print("[INFO] Loading SOCIAL detection model...")
    social_tokenizer, social_model = load_social_model(social_model_path)
    df = predict_social_label(df, social_tokenizer, social_model, device=DEVICE)

    print("[INFO] Loading GRI classification model...")
    gri_tokenizer, gri_model = load_gri_model(gri_model_path)
    df = predict_gri_label(df, gri_tokenizer, gri_model, device=DEVICE)

    print("[INFO] Saving final CSV...")
    save_final_csv(df, output_csv_path)
    print(f"[DONE] Pipeline completed. Output saved at: {output_csv_path}")
    return df
