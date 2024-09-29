# -*- coding: utf-8 -*-
"""

@author: musta
"""
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy's small English model for text processing
nlp = spacy.load('en_core_web_sm')

# Function to preprocess text: remove stopwords, punctuation, and lemmatize
def preprocess_text(text):
    doc = nlp(text.lower())  # Process the text with spaCy
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(tokens)

# Function to read and preprocess the files
def read_and_preprocess_file(file_path):
    import docx  # python-docx library to read .docx files
    
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    text = ' '.join(full_text)
    return preprocess_text(text)

# Function to check for plagiarism between two documents
def check_plagiarism(file_paths):
    # Read and preprocess both files
    processed_documents = [read_and_preprocess_file(path) for path in file_paths]

    # Convert the processed documents into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_documents)

    # Calculate cosine similarity between the documents
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Print similarity results between the two documents
    print(f"Similarity between {file_paths[0]} and {file_paths[1]}: {similarity_matrix[0][1] * 100:.2f}%")

if __name__ == "__main__":
    # Specify the paths of the text files to compare
    file_paths = [
        r'C:\Users\musta\OneDrive\Documents\intro op1.docx',  # Path to first .docx file
        r'C:\Users\musta\OneDrive\Documents\op2.docx'          # Path to second .docx file
    ]

    check_plagiarism(file_paths)

