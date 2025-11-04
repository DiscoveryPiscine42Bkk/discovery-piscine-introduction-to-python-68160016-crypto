import sys
num_params = len(sys.argv) - 1
print(f"Number of parameters: {num_params}.")
PS C:\Users\user\.vscode> & C:/Users/user/.vscode/.venv/Scripts/python.exe c:/Users/user/.vscode/hello_world.py
Number of parameters: 0.
PS C:\Users\user\.vscode\ex04> python parameters.py
Number of parameters: 0.
PS C:\Users\user\.vscode\ex04> python parameters.py initiation
Number of parameters: 1.
PS C:\Users\user\.vscode\ex04> python parameters.py this is crazy "there's everywhere!"
Number of parameters: 5.
PS C:\Users\user\.vscode>
ใน VS Code เราไม่กรอกค่าภายในตัวไฟล์ แต่ต้อง “ใส่ค่าพารามิเตอร์ด้านนอก” ตอนรันโปรแกรม เช่นใน Terminal ด้านล่างของ VS Code
