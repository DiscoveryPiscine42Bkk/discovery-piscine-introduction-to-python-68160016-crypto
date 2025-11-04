import sys
if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        numbers = list(range(start, end + 1))
        print(numbers)
    except ValueError:
        print("none")
ไม่กรอก C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py parallel egoism human 
none
กรอก 10 กับ 14 C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py 10 14 
[10, 11, 12, 13, 14]
