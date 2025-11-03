import sys
if len(sys.argv) == 1:
    print("none")
else:
    for word in sys.argv[1:]:
        if not word.endswith("ism"):
            print(f"{word}ism")
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/append_it.py
none
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/append_it.py "parallel" "egoism" "human"
parallelism
humanism
PS C:\Users\user\.vscode>
