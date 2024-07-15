from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        super().color('white')
        super().shape('circle')
        super().penup()
        self.angles_list = [60,-60,120,-120]
        self.restart_game()

    def move(self):
        super().forward(20)

    def restart_game(self):
        super().home()
        self.angle = random.choice(self.angles_list)
        super().setheading(self.angle)
