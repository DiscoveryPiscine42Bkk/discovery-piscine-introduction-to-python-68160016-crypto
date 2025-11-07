from checkmate import checkmate

def main():
    # Test 1: King โดนโจมตี
    chess_board_success = """\
....
.B..
.PK.
....\
"""
    print("Test 1 (King โดนโจมตี):")
    checkmate(chess_board_success)

    # Test 2: King ปลอดภัย
    chess_board_fail = """\
R...
....
..K.
....\
"""
    print("\nTest 2 (King ปลอดภัย):")
    checkmate(chess_board_fail)

if __name__ == "__main__":
    main()
