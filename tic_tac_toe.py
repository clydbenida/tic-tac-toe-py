import sys
import re

"""
The player shall pass the character (x, o) it wants to play as. 
If the player did not supply a character, his character shall be
selected randomly.
"""

player_1 = ""
player_2 = ""
move_count = 0

game_running = True
current_player = player_1

game_tile = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

tile_address = {
    "1": [0, 0],
    "2": [0, 1],
    "3": [0, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "7": [2, 0],
    "8": [2, 1],
    "9": [2, 2],
}

class Error(Exception):
    pass

def verify_player_input(player_input):
    if player_input == "o" or player_input == "x":
        return player_input
    else:
        raise Error("User imported an invalid character") 

def game_loop():
    global game_running, current_player, tile_address, game_tile, player_1, player_2, move_count  

    while game_running:
        print('\n')
        player_input = input(f"Player {current_player}'s turn, select the tile you want to play on (1-9): ")
        pattern = r'^-?\d+(\.\d+)?$'

        if re.match(pattern, player_input):
            # player_input_coords
            pic = tile_address[player_input]

            # If the specified tile is not a player input 
            if not ((game_tile[pic[0]][pic[1]] == 'x') or (game_tile[pic[0]][pic[1]] == 'o')):
                # accept user input
                game_tile[pic[0]][pic[1]] = current_player
                move_count += 1

                if (current_player == player_1):
                    current_player = player_2
                else:
                    current_player = player_1

        print_tile(game_tile)
        check_game_state(game_tile)

def print_tile(game_tile):
    print('-------------')
    for row_index, row in enumerate(game_tile):
        for cell_index, cell in enumerate(row):
            if (cell_index == 0):
                print(f'| {cell} |', end="")
            if (cell_index == 1):
                print(f' {cell} ', end="")
            if (cell_index == 2):
                print(f'| {cell} |')
    print('-------------')

def check_game_state(game_tile):
    global game_running, move_count 

    # Check rows
    for row in game_tile:
        if ((row[0] == row[1]) and (row[0] == row[2])):
            print(f'Player {row[0]} won the game!')
            game_running = False

    # Check columns
    for row_index, row in enumerate(game_tile):
        if((game_tile[0][row_index] == game_tile[1][row_index]) and (game_tile[0][row_index] == game_tile[2][row_index])):
            print(f'Player {row[row_index][0]} won the game!')
            game_running = False

    # Check diagonals
    if ((game_tile[0][0] == game_tile[1][1]) and (game_tile[0][0] == game_tile[2][2])):
        print(f'Player {game_tile[0][0]} won the game!')
        game_running = False

    if ((game_tile[0][2] == game_tile[1][1]) and (game_tile[0][2] == game_tile[2][0])):
        print(f'Player {game_tile[0][0]} won the game!')
        game_running = False

    if move_count == 9:
        game_running = False
        print("Nobody won!")

    if not game_running:
        user_conf = input("Do you want to play again? (y/n) ")

        if user_conf == 'y':
            # restart game
            reset_game_state()

def reset_game_state():
    global game_tile, game_running, move_count
    game_running = True
    move_count = 0
    game_tile = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    print_tile(game_tile)
    check_game_state(game_tile)

def main():
    global player_1, player_2, current_player, game_tile
    player_1 = verify_player_input(sys.argv[1])

    if (player_1 == "x"):
        player_2 = "o"
    else:
        player_2 = "x"

    print(f'The player_1 is {player_1}')
    print(f'The player_2 is {player_2}')

    print('\n----------------------------------\n')

    print_tile(game_tile)

    current_player = player_1 
    game_loop()

main()
