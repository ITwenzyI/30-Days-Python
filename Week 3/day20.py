import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
]

# opens the above list of websites in a different tab
for url in url_lists:
    pass
    #webbrowser.open_new_tab(url)

import requests

# URL der API
url = 'https://jsonplaceholder.typicode.com/users'

# GET-Anfrage senden
response = requests.get(url)

# Prüfen, ob die Anfrage erfolgreich war (Statuscode 200)
# if response.status_code == 200:
#     users = response.json()  # Antwort als JSON laden
#     for user in users:
#         print(f"{user['name']} ({user['email']})")
# else:
#     print("Fehler beim Abrufen:", response.status_code)

from mypackage import arithmetics
#print(arithmetics.add_numbers(3, 5))

import requests

new_url = "https://api.thecatapi.com/v1/breeds"
response = requests.get(new_url)

if response.status_code == 200:

    cats = response.json()
    max_list = []
    min_list = []

    import json

    print(json.dumps(cats[0], indent=4))
    print(cats[0].keys())
    print(cats[0]["weight"].keys())

    for cat in cats:
        weight_str = cat['weight']['metric']  # z.B. "3 - 5"
        if weight_str:
            try:
                max_val = int(weight_str.split(" - ")[-1])  # nehme das Maximum
                min_val = int(weight_str.split(" - ")[0]) # nehme das Minimum
                max_list.append((max_val, cat["name"]))     # mit Namen
                min_list.append((min_val, cat["name"]))
            except ValueError:
                pass  # überspringe Einträge mit ungültigem Format

    heaviest = max(max_list)
    lightest = min(min_list)

    print(f"Die schwerste Katze ist: {heaviest[1]} mit {heaviest[0]} kg.")
    print(f"Die leichteste Katze ist: {lightest[1]} mit {lightest[0]} kg.")

else:
    print("Fehler beim Abrufen:", response.status_code)

