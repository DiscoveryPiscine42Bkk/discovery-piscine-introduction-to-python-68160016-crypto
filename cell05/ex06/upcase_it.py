import sys
if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].upper())
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/upcase_it.py
none
PS C:\Users\user\.vscode>

PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/upcase_it.py "initiation"
INITIATION
PS C:\Users\user\.vscode>

PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/upcase_it.py "This exercise is quite easy!"
THIS EXERCISE IS QUITE EASY!
PS C:\Users\user\.vscode>
