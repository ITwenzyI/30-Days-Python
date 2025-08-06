def count_words_lines(path):
    lines = 0
    words = 0
    with open(path) as f:
        for line in f:
            print(line.split())
            lines += 1
            words += len(line.split())

        print(lines, words)



count_words_lines('./data/obama_speech.txt')

import json
def most_spoken_language(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    language_count = {}

    for country in data:
        for language in country.get("languages", []):
            language_count[language] = language_count.get(language, 0) + 1

    language_count = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    print(language_count)





most_spoken_language('./data/countries_data.json')