import sys
args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    text = args[0]
    result = "".join([ch for ch in text if ch == "z"])
    if result:
        print(result)
    else:
        print("none")
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/string_are_arrays.py
none
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/string_are_arrays.py "The character Z is not found in this string"
none
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/string_are_arrays.py "The character z is found in this string"
z
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/string_are_arrays.py "Zaz visits the zoo with Zazie"
zzz
PS C:\Users\user\.vscode>
