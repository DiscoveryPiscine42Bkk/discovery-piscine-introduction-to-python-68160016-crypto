import sys
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    if keyword not in text:
        print("none")
    else:
        count = text.count(keyword)
        print(count)
PS C:\Users\user\.vscode\ex09> & C:/Users/user/.vscode/.venv/Scripts/python.exe .\scan_it.py | cat -e
none$
PS C:\Users\user\.vscode\ex09> & C:/Users/user/.vscode/.venv/Scripts/python.exe .\scan_it.py "the" | cat -e
none$
PS C:\Users\user\.vscode\ex09> & C:/Users/user/.vscode/.venv/Scripts/python.exe .\scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
2$
PS C:\Users\user\.vscode\ex09>
