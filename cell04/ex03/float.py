num_input = input("Give me a number: ")
num = float(num_input)
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/hello_world.py
Give me a number: 1
This number is an integer.
PS C:\Users\user\.vscode>
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/hello_world.py
Give me a number: 42.00
This number is an integer.
PS C:\Users\user\.vscode>
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/hello_world.py
Give me a number: 42.42
This number is a decimal.
PS C:\Users\user\.vscode>
