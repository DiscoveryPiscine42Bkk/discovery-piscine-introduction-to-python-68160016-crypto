import sys
def downcase_it(s):
    return s.lower()
if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        print(downcase_it(arg))
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py 
none
กรอก "HELLO WORLD" "I understood Arrays well!" ในฐานะพารามิเตอร์ 
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py "HELLO WORLD" "I understood Arrays well!" 
hello world
i understood arrays well!
