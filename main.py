import tkinter as tk
import random

root = tk.Tk()
root.title("TEST")
canvas = tk.Canvas(root, width=500, height=500)

colors = ['#37AB65', '#3DF735', '#AD6D70', '#EC2504', '#8C0B90']
circle_size_max = 100
circle_size_min = 20


def draw_random_circle(event):
    global circle_size_min
    global circle_size_max
    circle_size = random.randint(circle_size_min, circle_size_max)
    x = random.randint(circle_size, 500 - circle_size)
    y = random.randint(circle_size, 500 - circle_size)
    color = random.choice(colors)
    canvas.create_oval(x - circle_size, y - circle_size, x + circle_size, y + circle_size, fill=color)
    canvas.focus_set()


canvas.bind("<Key-r>", draw_random_circle)
canvas.pack()
canvas.focus_set()
root.mainloop()
