import TTT_Board as TiTaToB

def print_board(b):
    print(f"\n\t\t\t\t\t {b[0][0]} | {b[0][1]} | {b[0][2]} ")
    print("\t\t\t\t\t----|----|----")
    print(f"\t\t\t\t\t {b[1][0]} | {b[1][1]} | {b[1][2]} ")
    print("\t\t\t\t\t----|----|----")
    print(f"\t\t\t\t\t {b[2][0]} | {b[2][1]} | {b[2][2]} ")
    
def check_board(b):
    # To check if the diagonals are identical
    if (b[0][0] == b[1][1] == b[2][2]) or (b[2][0] == b[1][1] == b[0][2]):
        if b[1][1] == "❌":
            return True
        elif b[1][1] == "🔘":
            return True
        
    # To check if the columns are identical
    if (b[0][0] == b[1][0] == b[2][0] == "❌") or (b[0][1] == b[1][1] == b[2][1] == "❌") or (b[0][2] == b[1][2] == b[2][2] == "❌"):
        return True
    elif (b[0][0] == b[1][0] == b[2][0] == "🔘") or (b[0][1] == b[1][1] == b[2][1] == "🔘") or (b[0][2] == b[1][2] == b[2][2] == "🔘"):
        return True
            
    # To check if the rows are identical
    if (b[0][0] == b[0][1] == b[0][2] == "❌") or (b[1][0] == b[1][1] == b[1][2] == "❌") or (b[2][0] == b[2][1] == b[2][2] == "❌"):
        return True
    elif (b[0][0] == b[0][1] == b[0][2] == "🔘") or (b[1][0] == b[1][1] == b[1][2] == "🔘") or (b[2][0] == b[2][1] == b[2][2] == "🔘"):
        return True
    
    return False

def is_board_full(game_board):
    for row in game_board:
        for space in row:
            if space == "  ":
                return False  # checking for an empty space
    return True  # No empty space



print(TiTaToB.game_name)

board = [
    ["  ", "  ", "  "],
    ["  ", "  ", "  "],
    ["  ", "  ", "  "]
]

print_board(board)

player_one_choice = "❌"
player_two_choice = "🔘"

print(f'\n\n\t\t\t\t\tPlayer one uses {player_one_choice}')
print(f'\t\t\t\t\tPlayer two uses {player_two_choice}')

player_one = True
value = 1
game = True

while game:
    
    if check_board(board):  # Checking for a winner
        if value == 2:
            value = 1
        else:
            value = 2
        print(f"\n\n\t\t\t\t\tPlayer {value} Won ✨🎉")
        break
    
    if is_board_full(board):    # Checking for a Draw
        print("\n\t\t\t\t\tIt's a Tie 👔. You can shake hands")
        break
        
    user_choice = int(input(f"\n\t\t\t\t\tPlayer_{value} Enter a position from (1 - 9): ")) - 1
    
    row = user_choice // 3
    column = user_choice % 3

    if user_choice < 0 or user_choice > 8:
        print("\t\t\t\t\tPosition out of bound")
    elif board[row][column] == "  ":
        if value == 1:
            board[row][column] = player_one_choice
            value = 2
        else:
            board[row][column] = player_two_choice
            value = 1
    else:
        print("\t\t\t\t\tThis position is already occupied. Try another one.")
            
    print_board(board)