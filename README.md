🌍 ESG Insight — Automated ESG Information Extraction and Scoring Pipeline
📘 Overview

ESG Insight is a data-driven pipeline designed to help businesses and analysts automatically extract, classify, and evaluate ESG (Environmental, Social, and Governance) information from complex corporate reports such as annual reports or sustainability disclosures.

The system leverages Natural Language Processing (NLP) and machine learning to process unstructured documents, identify key ESG-related content, and generate an ESG rating that reflects a company’s sustainability performance. It also provides data visualization tools to help users interpret ESG trends and patterns effectively.

🚀 Features

Automated Text Extraction
Extracts text from complex corporate documents (PDFs, reports, scanned files) while preserving structure and meaning — even for tables, bullet points, and multi-column layouts.

Intelligent Text Labeling
Labels extracted sentences or paragraphs as Environmental (E), Social (S), Governance (G), or Unrelated (U) using trained classification models.

ESG Scoring Engine
Aggregates labeled data and calculates a company’s ESG score based on content coverage, sentiment, and keyword intensity.

Visualization Dashboard
Displays ESG metrics and labeled data through interactive charts and summaries to highlight ESG strengths and weaknesses.

🧠 Pipeline Architecture
PDF / Report File
        ↓
 [Text Extraction Layer]
        ↓
 [Data Cleaning & Sentence Segmentation]
        ↓
 [ESG Labeling Model]
        ↓
 [ESG Scoring Engine]
        ↓
 [Visualization & Report Generation]


Each stage in the pipeline is modular, allowing users to customize or improve components such as the NLP model or the scoring algorithm.

🧩 Technologies Used

Language & Frameworks: Python, Pandas, NumPy, scikit-learn, PyTorch / TensorFlow

NLP Tools: spaCy, NLTK, transformers (BERT-based models)

PDF Parsing: PyMuPDF, pdfminer.six, Camelot (for table extraction)

Visualization: Matplotlib, Seaborn, Plotly / Dash

Storage & Processing: SQLite / PostgreSQL, JSON, CSV

Optional UI / Dashboard: Streamlit or Dash

⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/LeightonAkimitsu2030/Unveiling_Social_Insights_NLP-Based_Analysis_of_Annual_Reports.git

cd esg-insight

After cloning, go to "Prodcut" folder to continue the proceed

3. Create a Virtual Environment
python -m venv venv
source venv/bin/activate     # on macOS/Linux
venv\Scripts\activate        # on Windows

4. Install Dependencies
pip install -r requirements.txt

5. Run the Pipeline
python app.py

6. View Visualization

Once the pipeline completes, the interface will show up and you can choose the model as well as the output of the dashboard and report, then proceed to view ESG reports and visual summaries.

📊 Output Example

Labeled Dataset: output/labeled_sentences.csv

ESG Score Report: output/esg_score.json

Dashboard / Visualization: Accessible via Streamlit or Dash UI

🧪 Model & Training

The ESG classifier was trained on a curated dataset of corporate sentences manually labeled under Environmental, Social, Governance, and Unrelated categories.
Users can retrain or fine-tune the model using their own labeled data for improved domain adaptation.

📈 Future Enhancements

Add multi-language support for non-English corporate reports

Integrate OCR for scanned PDFs

Incorporate temporal ESG analysis (track changes across years)

Deploy a web-based interface for easier interaction and report uploads

👤 Author

Nguyen Lam
📧 nglamtruong.work@gmail.com

🪪 License

This project is released under the MIT License — free for personal and commercial use with attribution.
