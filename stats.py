from collections import Counter
def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_num_char(text):
    lower_case_text = text.lower()
    char_count = Counter(lower_case_text)
    return dict(char_count)