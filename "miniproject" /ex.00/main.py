from checkmate import is_king_in_check

def main():
    # ตัวอย่าง 1: Success (King ถูกโจมตี)
    # B = Bishop, P = Pawn, K = King, . = ช่องว่าง
    chess_board_success = """\
....
.B..
.PK.
....
"""
    print("Test 1 (King โดนโจมตี):")
    is_king_in_check(chess_board_success)  # ควรพิมพ์ Success

    print("\nTest 2 (King ปลอดภัย):")
    # ตัวอย่าง 2: Fail (King ปลอดภัย)
    chess_board_fail = """\
....
....
..K.
....
"""
    is_king_in_check(chess_board_fail)  # ควรพิมพ์ Fail

if __name__ == "__main__":
    main()
