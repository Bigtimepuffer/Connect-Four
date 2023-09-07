def main():
    ROW_COUNT = 6
    COLUMN_COUNT = 7
    board = []
    for row in range(ROW_COUNT):
        board.append([" "," "," "," "," "," "," "])
    turn = 0
    Game = True
    
    def is_valid(board,col):
        #Checks to see if the column is full.
        if board[0][col] == " ":
            return True
        else:
            return False
    
    def open_spot(board,col):
        #Looks for the lowest slot in the column.
        empty=-1
        for row in range(ROW_COUNT):
            if board[row][col] == " ":
                empty+=1
        return empty
                
    
    def drop(board,col,row,piece):
        #Changes one of the slots into a piece
        board[row][col] = piece
        return board
    
    def show_board(board):
        #Prints out the board row by row, and adds numbers at the bottom.
        for x in range(len(board)):
            #print(board[len(board)-1-x])
            print(board[x])
        print(" (1)  (2)  (3)  (4)  (5)  (6)  (7)")
        
    def win(board,piece):
        #Checks for a horizontal win
        for col in range(COLUMN_COUNT-3):
            for row in range(ROW_COUNT):
                if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                    return True
                
        #Checks for a vertical win
        for col in range(COLUMN_COUNT):
            for row in range(ROW_COUNT-3):
                if board[row][col] == piece and board[row+1][col] == piece and  board[row+2][col] == piece and  board[row+3][col] == piece:
                    return True
                
        #Checks for a positive slope win        
        for col in range(COLUMN_COUNT-3):
            for row in range(ROW_COUNT-3):
                if board[row][col] == piece and board[row+1][col+1] == piece and  board[row+2][col+2] == piece and  board[row+3][col+3] == piece:
                    return True
                
        #Checks for a negative slope win
        for col in range(COLUMN_COUNT-3):
            for row in range(3,ROW_COUNT):
                if board[row][col] == piece and board[row-1][col+1] == piece and  board[row-2][col+2] == piece and  board[row-3][col+3] == piece:
                    return True
    while Game:
        show_board(board)
        if turn%2 == 0:
            col = int(input("Player 1. 1-7 >"))-1
            piece = "X"
        
        elif turn%2 == 1:
            col = int(input("Player 2. 1-7 >"))-1
            piece = "O"
        
        if is_valid(board, col):
            row = open_spot(board,col)
            board = drop(board,col,row,piece)
            if win(board,piece) == True:
                show_board(board)
                print(f'{piece} wins!')
                Game = False
            turn+=1
if __name__ == "__main__":
    main()