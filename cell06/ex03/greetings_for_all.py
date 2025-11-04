def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
C:\Users\user\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\user\PyCharmMiscProject\parameter.py "HELLO WORLD" "I understood Arrays well!" 
Hello, Alexandra.
Hello, Wil.
Hello, noble stranger.
Error! It was not a name.
