import math
import random
import time
import tkinter as tk
from dataclasses import dataclass


@dataclass
class Star:
    item: int
    x: float
    y: float
    z: float
    size: float
    color: tuple
class Starfield:
    STAR_COUNT = 650
    FAR = 1800.0
    NEAR = 15.0
    COLORS = ((255, 255, 255), (190, 215, 255),
              (255, 225, 170), (255, 185, 160))

    def __init__(self, root):
        self.root = root
        root.title("Звёздное поле")
        root.geometry("1000x700")
        root.minsize(400, 300)
        self.canvas = tk.Canvas(root, background="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.width, self.height = 1000, 700
        self.focal = 600.0
        self.speed = 350.0
        self.keys = set()
        self.target_x = self.target_y = 0.0
        self.heading_x = self.heading_y = 0.0
        self.stars = []
        for _ in range(self.STAR_COUNT):
            star = Star(self.canvas.create_oval(0, 0, 0, 0, outline=""),
                        0, 0, 0, 0, (255, 255, 255))
            self.reset_star(star, initial=True)
            self.stars.append(star)
        self.hud = self.canvas.create_text(
            16, 16, anchor="nw", fill="#b6c5da", font=("Arial", 12))
        self.canvas.bind("<Configure>", self.resize)
        self.canvas.bind("<Motion>", self.mouse_move)
        self.canvas.bind("<Leave>", self.center_direction)
        root.bind("<KeyPress>", self.key_down)
        root.bind("<KeyRelease>", self.key_up)
        root.bind("<FocusOut>", lambda event: self.keys.clear())
        root.bind("<Escape>", lambda event: root.destroy())
        self.last_time = time.perf_counter()
        self.animate()





   

if __name__ == "__main__":
    window = tk.Tk()
    Starfield(window)
    window.mainloop()
