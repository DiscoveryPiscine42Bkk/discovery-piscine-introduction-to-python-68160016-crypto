def find_the_redheads(family):
    redheads = list(filter(lambda name: family[name] == "red", family))
    return redheads
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(dupont_family))
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py lol physically backpack 
['florian', 'david', 'franck']
