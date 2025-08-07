import re

text = ("hallo das ist ein test Text egal hallo "
        "Wie geht Hallo ein test Test")

def word_counter(text, n=10):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)

    # word_counts = {}
    # for word in words:
    #     if word in word_counts:
    #         word_counts[word] += 1
    #     else:
    #         word_counts[word] = 1

    word_counts = {}
    for word in text.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_words[:n]
    #return word_counts

print(word_counter(text))