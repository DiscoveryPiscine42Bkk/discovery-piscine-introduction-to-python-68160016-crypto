from checkmate import checkmate

def main():
    # กระดาน 4x4 King ถูกโจมตีโดย Bishop
    board = """\
B...
.K..
....
....\
"""
    checkmate(board)  # จะพิมพ์ "Success"

if __name__ == "__main__":
    main()

