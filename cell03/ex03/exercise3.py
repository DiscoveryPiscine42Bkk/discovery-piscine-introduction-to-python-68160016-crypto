import sys
if len(sys.argv) > 1:
    print("none")
    sys.exit()
i = 0
while i <= 10:
    print("Table de {}:".format(i), end=" ")
    j = 0
    while j <= 10:
        print(i * j, end="")
        if j < 10:
            print(" ", end="")
        j += 1
    print()  
    i += 1
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/hello_world.py
Table de 0: 0 0 0 0 0 0 0 0 0 0 0
Table de 1: 0 1 2 3 4 5 6 7 8 9 10
Table de 2: 0 2 4 6 8 10 12 14 16 18 20
Table de 3: 0 3 6 9 12 15 18 21 24 27 30
Table de 4: 0 4 8 12 16 20 24 28 32 36 40
Table de 5: 0 5 10 15 20 25 30 35 40 45 50
Table de 6: 0 6 12 18 24 30 36 42 48 54 60
Table de 7: 0 7 14 21 28 35 42 49 56 63 70
Table de 8: 0 8 16 24 32 40 48 56 64 72 80
Table de 9: 0 9 18 27 36 45 54 63 72 81 90
Table de 10: 0 10 20 30 40 50 60 70 80 90 100
PS C:\Users\user\.vscode>
