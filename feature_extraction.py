from sklearn.feature_extraction.text import CountVectorizer

def get_vectorizer():
    vectorizer = CountVectorizer()
    return vectorizer

def get_feature_vector(data):
    vectorizer = get_vectorizer()
    vectorizer.fit_transform(data)
    vector = vectorizer.transform(data)
    return vector
