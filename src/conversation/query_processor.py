import re

def preprocess_query(query):
    query = query.lower()
    query = re.sub(r'[^\w\s]', '', query)  # remove punctuation
    tokens = query.split()
    return tokens

def extract_keywords(query):
    # Simple example: return keywords excluding stopwords
    stopwords = {'show', 'me', 'the', 'from', 'this', 'week', 'latest'}
    tokens = preprocess_query(query)
    keywords = [word for word in tokens if word not in stopwords]
    return keywords

