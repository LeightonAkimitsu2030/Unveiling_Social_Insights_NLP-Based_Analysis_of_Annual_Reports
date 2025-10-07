import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import joblib

label_encoder = joblib.load('label_encoder.pkl')

def load_gri_model(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

def predict_gri_label(df, tokenizer, model, device='cpu', batch_size=16):
    s_rows = df[df['SOCIAL_LABEL'] == 'S'].copy()
    if s_rows.empty:
        df['GRI_LABEL'] = ""
        return df

    sentences = s_rows['sentence'].tolist()
    model.to(device)
    model.eval()

    all_labels = []
    for i in range(0, len(sentences), batch_size):
        batch_sentences = sentences[i:i+batch_size]
        inputs = tokenizer(batch_sentences, padding=True, truncation=True, return_tensors='pt').to(device)
        with torch.no_grad():
            outputs = model(**inputs)
            preds = torch.argmax(outputs.logits, dim=1).cpu().numpy()
            all_labels.extend(preds)

    # ✅ decode
    decoded_labels = label_encoder.inverse_transform(all_labels)
    s_rows['GRI_LABEL'] = decoded_labels
    df = df.merge(s_rows[['sentence', 'GRI_LABEL']], on='sentence', how='left')
    df['GRI_LABEL'] = df['GRI_LABEL'].fillna("")
    return df