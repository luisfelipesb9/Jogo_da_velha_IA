import math
import random
from typing import List, Optional, Dict

class TicTacToe:
    def __init__(self):
        self.board: List[str] = self.make_board()
        self.current_winner: Optional[str] = None

    @staticmethod
    def make_board() -> List[str]:
        return [' ' for _ in range(9)]

    def make_move(self, square: int, letter: str) -> bool:
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square: int, letter: str) -> bool:
        # Check row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([s == letter for s in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        
        return False

    def empty_squares(self) -> bool:
        return ' ' in self.board

    def num_empty_squares(self) -> int:
        return self.board.count(' ')

    def available_moves(self) -> List[int]:
        return [i for i, x in enumerate(self.board) if x == " "]

class Player:
    def __init__(self, letter: str):
        self.letter = letter

    def get_move(self, game: TicTacToe) -> int:
        pass

class SmartComputerPlayer(Player):
    def __init__(self, letter: str):
        super().__init__(letter)

    def get_move(self, game: TicTacToe) -> int:
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state: TicTacToe, player: str) -> Dict[str, Optional[int]]:
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # Check if the previous move was a winner
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            }
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            # Undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best
