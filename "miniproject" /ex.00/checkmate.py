def checkmate(board_str):
    board = [list(line) for line in board_str.splitlines()]
    size = len(board)
    
    # หา King
    king_x, king_y = -1, -1
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_x, king_y = i, j

    # ตรวจสอบทุก piece
    for i in range(size):
        for j in range(size):
            piece = board[i][j]

            # Rook ตรวจแนวตั้ง-แนวนอน
            if piece == 'R':
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    x, y = i, j
                    while 0 <= x+dx < size and 0 <= y+dy < size:
                        x += dx
                        y += dy
                        if (x, y) == (king_x, king_y):
                            print("Success")
                            return
                        if board[x][y] != '.':
                            break

            # Bishop ตรวจแนวทแยง
            if piece == 'B':
                for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
                    x, y = i, j
                    while 0 <= x+dx < size and 0 <= y+dy < size:
                        x += dx
                        y += dy
                        if (x, y) == (king_x, king_y):
                            print("Success")
                            return
                        if board[x][y] != '.':
                            break

            # Pawn ตรวจโจมตีเฉียง
            if piece == 'P':
                for dx, dy in [(-1,-1), (-1,1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < size and 0 <= y < size and (x, y) == (king_x, king_y):
                        print("Success")
                        return

    print("Fail")
