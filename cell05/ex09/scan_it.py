import sys
args = sys.argv[1:]
if len(args) != 2:
    print("none")
else:
    keyword = args[0]
    text = args[1]
    count = text.count(keyword)
    if count == 0:
        print("none")
    else:
        print(count)
    ไม่กรอกอะไร  C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py Python piscine hello 
none
กรอก the 
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py the 
none
กรอก the "the quick brown fox jumps over the lazy dog"
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py the "the quick brown fox jumps over the lazy dog" 
2
