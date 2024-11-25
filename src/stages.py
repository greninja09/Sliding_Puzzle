import tkinter as tk
from config import *

class StageSelection:
    def __init__(self):
        window_width, window_height = WIDTH(3), HEIGHT(4)
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height //2)
        
        self.root = tk.Tk()
        self.root.title("Stage Selection")
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.selected_stage = None

        tk.Label(self.root, text="Select Stage", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="3x3", font=("Arial", 14), command=lambda: self.select_stage(3)).pack(pady=5)
        tk.Button(self.root, text="4x4", font=("Arial", 14), command=lambda: self.select_stage(4)).pack(pady=5)
        tk.Button(self.root, text="5x5", font=("Arial", 14), command=lambda: self.select_stage(5)).pack(pady=5)

    def select_stage(self, size):
        self.selected_stage = size
        self.root.destroy()

    def run(self):
        self.root.mainloop()
        return self.selected_stage