to25.py
number = int(input("Enter a number less than 25\n"))
if number > 25:
    print("Error")
else:
    while number <= 25:
        print("Inside the loop, my variable is", number)
        number += 1
ผลลัพธ์ 
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/hello_world.py
Enter a number less than 25
20
Inside the loop, my variable is 20
Inside the loop, my variable is 21
Inside the loop, my variable is 22
Inside the loop, my variable is 23
Inside the loop, my variable is 24
Inside the loop, my variable is 25
PS C:\Users\user\.vscode>
