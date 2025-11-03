import sys
if len(sys.argv) != 2:
    print("none")
else:
    word = input("What was the parameter? ")
    if word == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
PS C:\Users\user\.vscode\ex10> & C:/Users/user/.vscode/.venv/Scripts/python.exe .\parameter_matching.py
none
PS C:\Users\user\.vscode\ex10> & C:/Users/user/.vscode/.venv/Scripts/python.exe .\parameter_matching.py "Hello"
What was the parameter? Bonjour
Nope, sorry...
PS C:\Users\user\.vscode\ex10> & C:/Users/user/.vscode/.venv/Scripts/python.exe .\parameter_matching.py "Hello"
What was the parameter? Hello
Good job!
PS C:\Users\user\.vscode\ex10>
