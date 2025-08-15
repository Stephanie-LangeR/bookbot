from collections import Counter
def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_num_char(text):
    lower_case_text = text.lower()
    char_count = Counter(lower_case_text)
    return dict(char_count)

def get_sorted_list(char_count):
    sorted_list = []
    for key, value in char_count.items():
        sorted_list.append({"char" : key, "num" : value})
    sorted_list.sort(key=lambda i: i["num"], reverse=True)
    return sorted_list