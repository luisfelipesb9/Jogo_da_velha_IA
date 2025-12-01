import tkinter as tk
from tkinter import messagebox

class TicTacToeView:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI - Senior Dev Edition")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        
        self.buttons = []
        self.restart_callback = None
        
        self.create_widgets()

    def create_widgets(self):
        # Title / Status Label
        self.status_label = tk.Label(
            self.root, 
            text="Your Turn (X)", 
            font=('Helvetica', 16, 'bold'),
            pady=10
        )
        self.status_label.pack()

        # Game Grid Frame
        grid_frame = tk.Frame(self.root)
        grid_frame.pack(pady=10)

        for i in range(9):
            btn = tk.Button(
                grid_frame, 
                text=" ", 
                font=('Helvetica', 20, 'bold'), 
                width=5, 
                height=2
            )
            btn.grid(row=i//3, column=i%3, padx=2, pady=2)
            self.buttons.append(btn)

        # Restart Button
        self.restart_btn = tk.Button(
            self.root, 
            text="Restart Game", 
            font=('Helvetica', 12),
            bg="#f0f0f0"
        )
        self.restart_btn.pack(pady=20)

    def bind_button_click(self, callback):
        """Bind the grid buttons to a callback function (controller)."""
        for i, btn in enumerate(self.buttons):
            # Use default argument to capture 'i' correctly in lambda
            btn.config(command=lambda idx=i: callback(idx))

    def bind_restart_click(self, callback):
        """Bind the restart button to a callback function."""
        self.restart_btn.config(command=callback)

    def update_button(self, index, letter):
        """Update the text and color of a specific button."""
        color = "blue" if letter == "X" else "red"
        self.buttons[index].config(text=letter, fg=color)

    def update_status(self, message):
        """Update the status label text."""
        self.status_label.config(text=message)

    def reset_board(self):
        """Reset all buttons to empty state."""
        for btn in self.buttons:
            btn.config(text=" ", bg="SystemButtonFace")
        self.update_status("Your Turn (X)")

    def show_game_over(self, message):
        """Show a popup message and update status."""
        self.update_status(message)
        if "AI Wins" in message:
            messagebox.showinfo("Game Over", "The AI has beaten you! Better luck next time.")
        elif "You Win" in message:
            messagebox.showinfo("Game Over", "Congratulations! You won!")
        else:
            messagebox.showinfo("Game Over", "It's a Draw!")
