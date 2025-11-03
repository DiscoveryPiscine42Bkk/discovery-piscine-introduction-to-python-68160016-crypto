import sys
if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        result = list(range(start, end + 1))
        print(result)
    except ValueError:
        print("none")
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/ex14/free_range.py
none
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/ex14/free_range.py 10 14
[10, 11, 12, 13, 14]
PS C:\Users\user\.vscode>
