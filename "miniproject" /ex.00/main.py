from checkmate import checkmate

def main():
    chess_board_success = """\
....
.B..
.PK.
....\
"""
    print("Test 1 (King โดนโจมตี):")
    checkmate(chess_board_success)  # ใช้ฟังก์ชัน checkmate

    print("\nTest 2 (King ปลอดภัย):")
    chess_board_fail = """\
....
....
..K.
....\
"""
    checkmate(chess_board_fail)  # ใช้ฟังก์ชัน checkmate

if __name__ == "__main__":
    main()
