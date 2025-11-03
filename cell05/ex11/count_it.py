import sys
args = sys.argv[1:]
if len(args) == 0:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{arg}: {len(arg)}")
PS C:\Users\user\.vscode\ex11> & C:/Users/user/.vscode/.venv/Scripts/python.exe .\count_it.py
none
PS C:\Users\user\.vscode\ex11> & C:/Users/user/.vscode/.venv/Scripts/python.exe .\count_it.py "Game" "of" "Thrones"
parameters: 3
Game: 4
of: 2
Thrones: 7
PS C:\Users\user\.vscode\ex10>
