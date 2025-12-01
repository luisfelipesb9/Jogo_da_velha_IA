from model import TicTacToe, SmartComputerPlayer
from view import TicTacToeView
import tkinter as tk

class TicTacToeController:
    def __init__(self, root):
        self.model = TicTacToe()
        self.view = TicTacToeView(root)
        self.ai_player = SmartComputerPlayer('O')
        self.human_letter = 'X'
        self.game_over = False

        # Bind View events to Controller methods
        self.view.bind_button_click(self.handle_click)
        self.view.bind_restart_click(self.reset_game)

    def handle_click(self, index):
        if self.game_over or self.model.board[index] != ' ':
            return

        # Human Move
        if self.model.make_move(index, self.human_letter):
            self.view.update_button(index, self.human_letter)
            
            if self.check_game_end(self.human_letter):
                return

            # AI Turn
            self.view.update_status("AI is thinking...")
            self.view.root.update()
            
            # Small delay for UX
            self.view.root.after(500, self.ai_move)

    def ai_move(self):
        if self.game_over:
            return

        square = self.ai_player.get_move(self.model)
        if self.model.make_move(square, self.ai_player.letter):
            self.view.update_button(square, self.ai_player.letter)
            
            if self.check_game_end(self.ai_player.letter):
                return
            
            self.view.update_status("Your Turn (X)")

    def check_game_end(self, letter):
        if self.model.current_winner == letter:
            msg = "You Win!" if letter == self.human_letter else "AI Wins!"
            self.view.show_game_over(msg)
            self.game_over = True
            return True
        
        if not self.model.empty_squares():
            self.view.show_game_over("It's a Tie!")
            self.game_over = True
            return True
            
        return False

    def reset_game(self):
        self.model = TicTacToe()
        self.game_over = False
        self.view.reset_board()
