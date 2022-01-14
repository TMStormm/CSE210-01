# Tic Tac Toe
# Author: TJ Miller
def main():
    game  = create_game()
    player = turn_change('')
    while not (winner(game) or draw(game)):
        display_game(game)
        player_move(player, game)
        player = turn_change(player)
    display_game(game)
    if winner(game):
        player = turn_change(player)
        print(f'Congrats to {player}, You have won the game.')
    elif draw(game):
        print(f'Game ended in a tie. Better luck next time')

def create_game():
    game = []
    for square in range(16):
        game.append(square +1)
    return game

def display_game(game):
    print()
    print(f"{game[0]}|{game[1]}|{game[2]}|{game[3]}")
    print('--------')
    print(f"{game[4]}|{game[5]}|{game[6]}|{game[7]}")
    print('--------')
    print(f"{game[8]}|{game[9]}|{game[10]}|{game[11]}")
    print('--------')
    print(f"{game[12]}|{game[13]}|{game[14]}|{game[15]}")
    
def draw(game):
    for square in range(16):
        if game[square] != "x" and game[square] != "o":
            return False
    return True

def winner(game):
    return (game[0] == game[1] == game[2] or
            game[3] == game[4] == game[5] or
            game[6] == game[7] == game[8] or
            game[0] == game[3] == game[6] or
            game[1] == game[4] == game[7] or
            game[2] == game[5] == game[8] or
            game[0] == game[4] == game[8] or
            game[2] == game[4] == game[6])

def player_move(player, game):
    print()
    square = int(input(f"{player}'s turn to choose a square (1-16): "))
    game[square - 1] = player

def turn_change(turn):
    if turn == "" or turn == "o":
        return "x"
    elif turn == "x":
        return "o"

if __name__ == "__main__":
    main()   