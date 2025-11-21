def initialize_board(num_rows, num_cols):
    board = []
    for i in range(num_rows):
        board.append([])
        for j in range(num_cols):
            board[i].append("-")

    return board

def print_board(board):
    for i in range(len(board)-1, -1, -1):
        for j in board[i]:
            if j == len(board[i])-1:
                print(j, end="")
            else:
                print(j, end=" ")
        print()

def insert_chip(board, col, chip_type):
    for i in range(len(board)):
        if board[i][col] == "-":
            board[i][col] = chip_type
            return i
        
def check_if_winner(board, col, row, chip_type):
    count = 0
    for i in range(len(board[row])):
        if board[row][i] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    
    count = 0
    for j in range(len(board)):
        if board[j][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    
    return False

def is_draw(board):
    for i in range(len(board)):
        for chip in board[i]:
            if chip == "-":
                return False
    return True

if __name__ == "__main__":
    height = int(input("What would you like the height of the board to be?"))
    length = int(input("What would you like the length of the board to be?"))
    board = initialize_board(height, length)
    print_board(board)
    print()

    # Tell players their pieces
    print("Player 1: x\n"
          "Player 2: o\n")
    
    while True:
        p1_col = int(input("Player 1: Which column would you like to choose?"))
        chip_row = insert_chip(board, p1_col, "x")
        print_board(board)
        print()
        if check_if_winner(board, p1_col, chip_row, "x"):
            print("Player 1 won the game!")
            break

        p2_col = int(input("Player 2: Which column would you like to choose?"))
        chip_row = insert_chip(board, p2_col, "o")
        print_board(board)
        print()
        if check_if_winner(board, p2_col, chip_row, "o"):
            print("Player 2 won the game!")
            break
        elif is_draw(board):
            print("Draw. Nobody wins.")
            break
