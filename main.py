import tkinter as tk
from controller import TicTacToeController

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeController(root)
    root.mainloop()
