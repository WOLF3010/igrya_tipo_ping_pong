from tkinter import *
import random
import time

screen = Tk()
screen.title("пинг понг")
screen.resizable(False, False)
screen.wm_attributes("-topmost", 1)
canvas = Canvas(screen, width=500, height=400)
canvas.pack()
screen.update()


class Ball:
    def __init__(self, canvas, color, platforma_2, score):
        self.score = score
        self.platforma_2 = platforma_2
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 500 / 2 - 7, 150)
        self.x = -5
        self.y = -5
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_platform(self, pos):
        platform_pos = self.canvas.coords(self.platforma_2.id)
        if pos[0] <= platform_pos[2] and pos[2] >= platform_pos[0]:
            if platform_pos[1] <= pos[3] <= platform_pos[3]:
                self.score.hit()
                return True
        return False



    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 5
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(241, 100, text="Вы сус", font=('Courier', 42), fill="red")
        if pos[0] <= 0:
            self.x = 5
        if pos[2] >= self.canvas_width:
            self.x = -5
        if self.hit_platform(pos):
            self.y = -5


class Platforma:
    def __init__(self, canvas, color):
        self.x = 0
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 201, 20, fill=color)
        self.canvas.move(self.id, 153, 300)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        koordinati = self.canvas.coords(self.id)
        if koordinati[0] <= 0:
            self.x = 0
        if koordinati[2] >= self.canvas_width:
            self.x = 0

    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2

class Score:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.score = 0
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

score = Score(canvas,  "red")
platforma_2 = Platforma(canvas, "black")
ball = Ball(canvas, "red", platforma_2, score)
while True:
    if not ball.hit_bottom:

        platforma_2.draw()
        ball.draw()
    else:
        time.sleep(2)
        break
    screen.update_idletasks()
    screen.update()
    time.sleep(0.01)
