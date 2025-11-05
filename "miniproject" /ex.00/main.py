from checkmate import is_king_in_check

def main():
    chess_board_success = """\
....
.B..
.PK.
....
"""
    print("Test 1 (King โดนโจมตี):")
    is_king_in_check(chess_board_success) 

    print("\nTest 2 (King ปลอดภัย):")
    chess_board_fail = """\
....
....
..K.
....
"""
    is_king_in_check(chess_board_fail) 

if __name__ == "__main__":
    main()
