from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
class clean_docs:
    def __init__(self):
        self.all_names = set(names.words())
    def is_letter_only(self, word):
        """
        PARAMETERS:a word
        RETURNS: a bool value to expressing if the word is entirely alpha neumeric
        """
        return word.isalpha()

    def clean_text(self, docs):
        """
        PARAMETERS:a list of documents
        RETURNS: a list of cleaned documents
            'cleaned':
                -->number and punctuation removed
                -->human name removal
                -->stop-word removal
                -->lemmatization
        """
        docs_cleaned = []
        for doc in docs:
            doc = doc.lower()
            word_list = [lemmatizer.lemmatize(word) for word in doc.split() if is_letter_only(word) and word not in self.all_names]
            doc_cleaned = ' '.join(word_list)
            docs_cleaned.append(doc_cleaned)
        return docs_cleaned

