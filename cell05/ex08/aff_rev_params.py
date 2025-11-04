import sys
args = sys.argv[1:]  
if len(args) < 2:
    print("none")
else:
    for arg in reversed(args):
        print(arg)

ไม่ใส่พารามิเตอร์ C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py 
none
ใส่ cocou  C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py coucou
none 
ใส่ Python piscine hello C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py Python piscine hello 
hello
piscine
Python
