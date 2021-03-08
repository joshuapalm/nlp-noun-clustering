import nltk

def tokenize_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    c_tokens = [''.join(e for e in string if e.isalpha()) for string in tokens]
    c_tokens = [x for x in c_tokens if x]
    return c_tokens

