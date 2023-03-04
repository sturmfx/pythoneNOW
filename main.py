import time
import tkinter as tk
import tkinter.colorchooser as colorchooser
import random

root = tk.Tk()
root.title("DRAWING CIRCLES")

canvas = tk.Canvas(root, width=500, height=500)
size = tk.Entry(root)

color1 = '#F0F8FF'


def choose_color():
    global color1
    color_c = colorchooser.askcolor(title="CHOOSE COLOR")[1]
    if color_c:
        color1 = color_c
    canvas.focus_set()


def draw(event):
    circle_size = int(size.get())
    x = event.x
    y = event.y
    item = canvas.create_oval(x - circle_size, y - circle_size, x + circle_size, y + circle_size, fill=color1)
    return item


def draw2(event):
    circle_size = int(size.get())
    x = event.x
    y = event.y
    item = canvas.create_rectangle(x - circle_size / 2, y - circle_size / 2, x + circle_size / 2, y + circle_size / 2,
                                   fill=color1)
    return item


def draw3(event):
    circle_size = int(size.get())
    x = event.x
    y = event.y
    item = canvas.create_polygon(x, y - circle_size, x - circle_size, y + circle_size, x + circle_size, y + circle_size,
                                 fill=color1, outline='#000000')
    return item


def clear(event):
    canvas.delete("all")


def increase(event):
    current = int(size.get())
    size.delete(0, tk.END)
    size.insert(0, str(current + 1))


def decrease(event):
    current = int(size.get())
    if current > 1:
        size.delete(0, tk.END)
        size.insert(0, str(current - 1))


def random_color(event):
    global color1
    color1 = '#' + ''.join(random.choices('1234567890ABCDEF', k=6))
    canvas.focus_set()


def move(item):
    x1 = random.randint(0, 500)
    y1 = random.randint(0, 500)

    x2 = random.randint(0, 500)
    y2 = random.randint(0, 500)

    dx = (x2 - x1) / 50
    dy = (y2 - y1) / 50

    for i in range(50):
        canvas.move(item, dx, dy)
        root.update()
        time.sleep(0.05)


color = tk.Button(root, text="CHOOSE COLOR", command=choose_color)
canvas.bind("<Button-1>", lambda event: move(draw(event)))
canvas.bind("<Button-2>", lambda event: move(draw3(event)))
canvas.bind("<Button-3>", lambda event: move(draw2(event)))
canvas.bind("<Key-r>", clear)
canvas.bind("<Key-minus>", decrease)
canvas.bind("<Key-plus>", increase)
canvas.bind("<Key-f>", random_color)
canvas.pack()
size.pack()
color.pack()
root.mainloop()
