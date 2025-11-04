def average(students_scores):
    if not students_scores:
        return 0
    total = sum(students_scores.values())
    count = len(students_scores)
    return total / count
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py lol physically backpack 
Average for class 3B: 12.5.
Average for class 3C: 13.25.
