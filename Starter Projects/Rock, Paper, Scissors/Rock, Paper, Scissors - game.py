import random
import sys

class RPS:
    def __init__(self):
        print('Welcome to RPS the game')

        #defining dictionary

        self.moves: dict = {'rock': '🥌', 'paper': '📃', 'scissors': '✂' }
        self.valid_moves: list[str] = list(self.moves.keys())
        self.user_win: int = 0
        self.ai_win: int  = 0

    #three functions - run_game, display_move, check_move

    def run_game(self):
        #Get the user input
        user_move: str = input(f'Rock, Paper, Scissors?: ').lower()

        # user wants to exit the game
        if user_move == 'exit':
            print(f'Total won by you: {self.user_win}')
            print(f'Total won by ai: {self.ai_win}')
            print('Thanks for playing!')
            sys.exit()

        #invalid move
        if user_move not in self.valid_moves:
            print(f'Invalid move')
            return self.run_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_move(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_move(self, user_move: str, ai_move: str):
        #show everything nicely
        print('______')
        print(f'user_move: {self.moves[user_move]}')
        print(f'ai_move: {self.moves[ai_move]}')
        print('______')

    def check_move(self, user_move:str, ai_move: str):
        if user_move == ai_move:
            print(f"It's a tie!")
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win!')
            self.user_win+=1
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win!')
            self.user_win+=1
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win!')
            self.user_win+=1
        else:
            print('You lose!')
            self.ai_win+=1


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.run_game()



