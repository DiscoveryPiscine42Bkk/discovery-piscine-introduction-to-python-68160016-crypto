import sys
args = sys.argv[1:]
if len(args) != 1:
    print("none")
else:
    param = args[0]
    user_input = input("What was the parameter? ")
    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")

ไม่กรอก C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py 
none
กรอก  Bonjour
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py "What was the parameter? " 
What was the parameter? Bonjour
Nope, sorry...
กรอก Hello
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py Hello 
What was the parameter? Hello
Good job!

