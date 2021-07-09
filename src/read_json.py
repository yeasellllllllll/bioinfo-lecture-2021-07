import json

with open("data.json", "r") as handle:
    data = json.load(handle)

print(data)
# [{'id': 1, 'sequence': 'ACAGGGTTA', 'species': 'Influenza'},\n
# {'id': 2, 'sequence': 'TTAACCAAG', 'species': 'Herpes'}, \n
# {'id': 3, 'sequence': 'GCGAATGAC', 'species': 'Epstein-barr'}]

for i in data:
    print(f"{i['id']}\t{i['sequence']}\t{i['species']}")
