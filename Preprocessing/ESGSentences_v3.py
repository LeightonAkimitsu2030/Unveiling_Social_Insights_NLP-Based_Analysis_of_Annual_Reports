import fitz  # only for PDF
import pandas as pd
import re
import os


def clean_text(text):
    # Remove invalid characters in Excel + normalize bullet points
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    text = re.sub(r"\s*•\s*", ".", text)
    return ' '.join(text.strip().split())


def is_valid_sentence(sentence):
    if not sentence.strip():
        return False
    if re.fullmatch(r'[\W\d\s]+', sentence):  # Contains only special characters/numbers
        return False
    if len(sentence.strip().split()) < 5:
        return False
    return True


def split_into_sentences(text):
    pattern = re.compile(
        r'(?<=[.•!?])\s+(?=[A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ0-9])'
    )
    raw_sentences = pattern.split(text)
    return [clean_text(s) for s in raw_sentences if is_valid_sentence(s)]


def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.pdf':
        doc = fitz.open(file_path)
        text = " ".join(page.get_text() for page in doc)
        return clean_text(text)

    elif ext == '.xlsx':
        df = pd.read_excel(file_path)
    elif ext == '.csv':
        df = pd.read_csv(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    # Merge all text contents of cells
    full_text = " ".join(df.astype(str).fillna("").values.flatten())
    return clean_text(full_text)


def extract_sentences_from_file(file_path):
    full_text = extract_text_from_file(file_path)
    sentences = split_into_sentences(full_text)
    return [{'STT': i + 1, 'Sentences': s} for i, s in enumerate(sentences)]


# === RUNNING MANUALLY ===
input_path = "input of the file"
output_path = "choosing the output folder"

sentences = extract_sentences_from_file(input_path)

df = pd.DataFrame(sentences)
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print("✅ Processed and saved to file:", output_path)