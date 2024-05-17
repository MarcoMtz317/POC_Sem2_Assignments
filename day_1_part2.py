import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        live = 3 
        self.width = 600
        self.height = 400
        self.bg = "#AAAAFF"
        self.canvas = tk.Canvas(self, bg="#AAAAFF", width = self.width, height = self.height)
        self.canvas.pack()
        self.pack()

class GameObject(object):
    def __int__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item)

    def delete(self):
        self.canvas.delete(self.item)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("BREAKOUT")
    game = Game(root)
    root.mainloop()
    item = game.canvas.create_rectangle(10, 10, 100, 80, fill="green")
    game_object = GameObject(game.canvas, item)
    game_object.move(50,50)
    game_object.delete()

class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 10
        self.direction = [1, -1]
        item = canvas.create_oval(x1, y1, x2, y2, fill = color)
        super(Ball, self).__init__(canvas, item)


class Paddle(GameObject):
    def __init__(self, canvas, x, y):
        self.width = 80
        self.heitght = 30
        self.Ball = None
        x1 = x - self.width / 2
        y1 = y - self.width / 2
        x2 = x - self.width / 2
        y2 = y - self.width / 2
        self.fill = "blue"

        super(Paddle, self).__init__(canvas, item)


def set_ball(self,ball):
    self.ball = ball


def move(self, offset):
        coords = self.get_position()
        width = self.canvas.winfo.width()
        x1 = coords[0]
        y1 = coords[1]
        x2 = coords[2]
        y2 = coords[3]
        if x1 + offset >= 0 and x2 + offset <= width:
            super(Paddle, self).move(offset, 0)
        if self.ball is not None:
            self.ball.move(offset, 0)