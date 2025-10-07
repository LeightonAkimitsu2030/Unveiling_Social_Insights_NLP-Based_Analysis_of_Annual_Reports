import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def load_social_model(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

def predict_social_label(df, tokenizer, model, device='cpu', batch_size=16):
    sentences = df['sentence'].tolist()
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

    df['SOCIAL_LABEL'] = ['S' if p == 1 else 'U' for p in all_labels]
    return df
