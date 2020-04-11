# THIS PROGRAM DOES NOT HAVE A 100% WIN RATE (CHECK LINES 104-127)
# WHEN CALCULATING THE SCORE, THERE IS A PROBLEM AND DOESN'T RETURN THE BEST MOVE ALL THE TIME
# THIS PROGRAM IS IMPLEMENTED USING THE MINIMAX ALGORITHM

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

HUMAN = "X"
COMPUTER = "O"


# Prints out the tic-tac-toe board
def printBoard(gameboard):
    print("\n")
    print(gameboard[0][0] + "  | " + gameboard[0][1] + " | " + gameboard[0][2])
    print(" - " + "+" + " - " + "+" + " - ")
    print(gameboard[1][0] + "  | " + gameboard[1][1] + " | " + gameboard[1][2])
    print(" - " + "+" + " - " + "+" + " - ")
    print(gameboard[2][0] + "  | " + gameboard[2][1] + " | " + gameboard[2][2])
    print("\n")


position = {
    1: [0, 0], 2: [0, 1], 3: [0, 2],
    4: [1, 0], 5: [1, 1], 6: [1, 2],
    7: [2, 0], 8: [2, 1], 9: [2, 2]

}


# Checks the board to see if a player has won or not
def checkBoard(gameboard):
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            if gameboard[i][0] == gameboard[i][1] == gameboard[i][2] and gameboard[i][0] != " ":     # Rows
                return gameboard[i][0]

            elif gameboard[0][j] == gameboard[1][j] == gameboard[2][j] and gameboard[0][j] != " ":     # Columns
                return gameboard[0][j]

    if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] and gameboard[0][0] != " ":             # Diagonal from top-left to bottom-right
        return gameboard[0][0]

    elif gameboard[2][0] == gameboard[1][1] == gameboard[0][2] and gameboard[0][2] != " ":             # Diagonal from top-right to bottom-left
        return gameboard[2][0]

    elif not availableMoves(gameboard):
        return "DRAW"

    else:
        return None


# Checks if the specified position is empty
def isEmpty(row, col, gameboard):
    if gameboard[row][col] == " ":
        return True

    else:
        return False


# The player enters where they would like to place the "X" marker
def playerMove(gameboard):
    choice = int(input("Where do you want to put the marker?: "))
    row, col = position[choice]
    if isEmpty(row, col, gameboard):
        gameboard[row][col] = HUMAN

    else:
        print("Space already occupied")
        playerMove(gameboard)


# Returns a list of all the empty positions in the tic-tac-toe board
def availableMoves(gameboard):
    moves = []
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            if isEmpty(i, j, gameboard):
                moves.append([i, j])

    return moves


# Places the "O" marker where the AI says(Just for the recursion)
def placeAIMarker(row, col, gameboard, player):
    gameboard[row][col] = player
    return gameboard


best_score = 0
best_score_move = [0, 0]
score = 0


# Returns the best move that the AI can move to
def AI_Move(player, max_depth, gameboard):
    bestMove = []
    global best_score_move
    global best_score
    global score

    if not availableMoves(gameboard):
        return 0, [0, 0]

    for move in availableMoves(gameboard):
        row, col = move

        if checkBoard(gameboard) is None:
            if player > 0:
                if isEmpty(row, col, gameboard):
                    new_board = placeAIMarker(row, col, gameboard, HUMAN)
                    AI_Move(-1, max_depth - 1, new_board)

            # If the player is "O"/ the Computer
            else:
                if isEmpty(row, col, gameboard):
                    new_board = placeAIMarker(row, col, gameboard, COMPUTER)
                    AI_Move(1, max_depth - 1, new_board)

        if checkBoard(gameboard) is not None or max_depth == 0:
            if checkBoard(gameboard) == COMPUTER:
                score -= 1
                if player < 0:
                    if score < best_score:
                        best_score = score

            if checkBoard(gameboard) == HUMAN:
                score += 1
                if player > 0:
                    if score > best_score:
                        best_score = score

        if max_depth == 9:
            print(score, gameboard, move)
            bestMove.append((score, move))

            score = 0
            best_score_move = min(bestMove)[1]

            if len(bestMove) == max_depth:
                gameboard[row][col] = " "

        gameboard[row][col] = " "

    return best_score, best_score_move


# Takes the result of the "AI_Move" function and places the "O" marker at that position
def chooseIdealMove(gameboard, function):
    moves = function[1]
    row, col = moves
    gameboard[row][col] = COMPUTER


# The main program
def main():
    while True:
        if checkBoard(board) == "DRAW":
            print("It's a draw!!!")
            printBoard(board)
            break
        elif checkBoard(board) is not None:
            result = checkBoard(board)
            print("Player " + result + " is the winner!!!")
            printBoard(board)
            break

        printBoard(board)
        playerMove(board)
        chooseIdealMove(board, AI_Move(-1, 9, board))


if __name__ == '__main__':
    main()