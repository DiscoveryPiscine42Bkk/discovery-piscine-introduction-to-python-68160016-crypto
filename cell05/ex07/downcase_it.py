import sys
if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].lower())
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/downcase_it.py
none
PS C:\Users\user\.vscode>

PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/downcase_it.py "LUCIOLE"
luciole
PS C:\Users\user\.vscode>

PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/downcase_it.py "This exercise is quite easy!"
this exercise is quite easy!
PS C:\Users\user\.vscode>
