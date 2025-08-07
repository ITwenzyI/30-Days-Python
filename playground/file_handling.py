from datetime import datetime

currently_time = datetime.now()
current_time = currently_time.strftime("%d.%m.%Y %H:%M:%S")
print(current_time)


#with open ("./data/test_file.txt", "w") as file:
with open("./data/test_file.txt", "a") as file:
    #file.write(f"\nAppend at the end: {current_time}")
    pass
with open("./data/test_file.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)

import os
if os.path.exists("./data/test_file.txt"):
    os.remove("./data/test_file.txt")
else:
    print("File doesn't exist")

import json
text_json = """{
    "apple": "apple",
    "banana": "banana",
    "orange": "orange"
}"""

person = {
    "name" : "Kilian",
    "age": 19,
}

person_json = json.dumps(person)
print(person_json)

with open("./data/test_file.json", "r", encoding="utf-8") as file:
    #file.write(text_json)
    #file.write(person_json)
    data = json.load(file)
    for item in data:
        print(item)

