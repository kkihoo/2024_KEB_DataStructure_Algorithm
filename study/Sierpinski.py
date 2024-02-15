from tkinter import *


def draw_triangle(x, y, size):
    if size >= 30:
        draw_triangle(x, y, size / 2)
        draw_triangle(x + size / 2, y, size / 2)
        draw_triangle(x + size / 4, int(y - size * (3**0.5) / 4), size / 2)
    else:
        canvas.create_polygon(
            x,
            y,
            x + size,
            y,
            x + size / 2,
            y - size * (3**0.5) / 2,
            fill="yellow",
            outline="black",
        )


c_size = 700


window = Tk()
window.title("삼각형 프랙탈")
canvas = Canvas(window, height=c_size, width=c_size, bg="white")

draw_triangle(c_size / 5, c_size / 5 * 4, c_size * 2 / 3)

canvas.pack()
window.mainloop()
