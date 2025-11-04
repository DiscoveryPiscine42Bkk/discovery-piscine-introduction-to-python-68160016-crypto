import sys
args = sys.argv[1:]
if len(args) == 0:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for param in args:
        print(f"{param}: {len(param)}")
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py Game of Thrones 
parameters: 3
Game: 4
of: 2
Thrones: 7
