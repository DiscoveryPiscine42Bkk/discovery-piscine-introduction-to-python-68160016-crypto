import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    text = args[0]

    z_chars = [ch for ch in text if ch.lower() == 'z']

    if len(z_chars) == 0:
        print("none")
    else:
        print("".join(['z' for _ in z_chars]))

ไม่กรอก C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py 
none
ตัว Z 
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py The character Z is not found in this string 
none
ตัว z
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py The character z is found in this string 
none
Z หลายตัว "Zaz visits the zoo with Zazie"
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py "Zaz visits the zoo with Zazie" 
zzz
