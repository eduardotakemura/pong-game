from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        super().color('white')
        super().hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.restart_game()

    def middle_line(self):
        super().teleport(0,280)
        super().width(5)
        super().setheading(270)
        for _ in range(30):
            super().forward(20)
            super().penup()
            super().forward(20)
            super().pendown()

    def scoreboard(self):
        super().teleport(-50,230)
        super().write(arg=self.left_score,align='center',font=('Calibri',50,'normal'))
        super().teleport(50, 230)
        super().write(arg=self.right_score, align='center', font=('Calibri', 50, 'normal'))

    def restart_game(self):
        self.clear()
        self.middle_line()
        self.scoreboard()