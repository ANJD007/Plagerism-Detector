import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # fixed the regex here too
    return text.split()

def calculate_similarity_hashing(text1, text2):
    tokens1 = set(tokenize(text1))
    tokens2 = set(tokenize(text2))

    common = tokens1.intersection(tokens2)
    total = tokens1.union(tokens2)

    if not total:
        return 0.0

    return (len(common) / len(total)) * 100
