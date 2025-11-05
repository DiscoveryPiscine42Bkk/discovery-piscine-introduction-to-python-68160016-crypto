from checkmate import checkmate

def main():
    chess_board_success = """\
....
.B..
.PK.
....\
"""
    print("Test 1 (King โดนโจมตี):")
    checkmate(chess_board_success)  
    print("\nTest 2 (King ปลอดภัย):")
    chess_board_fail = """\
R...
....
..K.
....\
"""
    checkmate(chess_board_fail)  

if __name__ == "__main__":
    main()
