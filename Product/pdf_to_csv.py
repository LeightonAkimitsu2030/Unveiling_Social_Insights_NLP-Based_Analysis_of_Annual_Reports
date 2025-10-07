import re
import fitz
import pandas as pd

# === CÁC HÀM XỬ LÝ VĂN BẢN ===
def clean_text(text):
    return ' '.join(text.strip().split())

def is_valid_sentence(sentence):
    if not sentence.strip():
        return False
    if re.fullmatch(r'[\W\d\s]+', sentence):
        return False
    if len(sentence.strip().split()) < 5:
        return False
    if len(sentence.strip().split()) > 49:
        return False
    return True

abbreviation_exceptions = {
    "TP.": "TP<dot>", "Tp.": "Tp<dot>", "Q.": "Q<dot>", "P.": "P<dot>",
    "TS.": "TS<dot>", "Ts.": "Ts<dot>", "ThS.": "ThS<dot>", "Ths.": "Ths<dot>",
    "GS.": "GS<dot>", "Gs.": "Gs<dot>", "PGS.": "PGS<dot>", "Pgs.": "Pgs<dot>",
    "TT.": "TT<dot>", "Tt.": "Tt<dot>", "BV.": "BV<dot>", "Bv.": "Bv<dot>",
    "UBND.": "UBND<dot>"
}

def apply_abbreviation_protection(text):
    for abbr, placeholder in abbreviation_exceptions.items():
        text = text.replace(abbr, placeholder)
    return text

def restore_abbreviations(text):
    for abbr, placeholder in abbreviation_exceptions.items():
        text = text.replace(placeholder, abbr)
    return text

def split_into_sentences(text):
    protected_text = apply_abbreviation_protection(text)
    pattern = re.compile(
        r'(?<=[.!?])\s+(?=[A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÉÈẺẼẸÊẾỀỂỄỆ'
        r'ÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ0-9])'
    )
    raw_sentences = pattern.split(protected_text)
    restored_sentences = [restore_abbreviations(s) for s in raw_sentences]
    return [clean_text(s) for s in restored_sentences if is_valid_sentence(s)]

def extract_sentences_from_pdf(pdf_path):
    """
    Đọc 1 file PDF và trả về DataFrame với cột 'sentence' chứa các câu được tách ra.
    """
    doc = fitz.open(pdf_path)
    full_text = " ".join([page.get_text() for page in doc])
    full_text = clean_text(full_text)
    sentences = split_into_sentences(full_text)
    df = pd.DataFrame({"sentence": sentences})
    return df

def save_sentences_to_csv(df, output_path):
    """
    Lưu DataFrame câu văn ra CSV.
    """
    df.to_csv(output_path, index=False)
