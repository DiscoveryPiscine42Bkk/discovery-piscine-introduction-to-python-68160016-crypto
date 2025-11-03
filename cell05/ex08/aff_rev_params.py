import sys
if len(sys.argv) < 3:
    print("none")
else:
    for param in reversed(sys.argv[1:]):
        print(param)
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/aff_rev_params.py
none
PS C:\Users\user\.vscode>

PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/aff_rev_params.py "coucou"
none
PS C:\Users\user\.vscode>

PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/aff_rev_params.py "Python" "piscine" "hello"
hello
piscine
Python
PS C:\Users\user\.vscode>
