import sys
if len(sys.argv) < 2:
    print("none")
else:
    has_output = False  
    for arg in sys.argv[1:]:
        if not arg.endswith("ism"): 
            print(arg + "ism")
            has_output = True
    if not has_output:
        print("none")
กรอก parallel egoism human
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py parallel egoism human 
parallelism
humanism
