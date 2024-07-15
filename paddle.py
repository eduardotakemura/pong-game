from turtle import Turtle

class Paddle:
    def __init__(self,position):
        self.paddle_list = []
        self.create_paddle(position)

    def create_paddle(self,position):
        for coord in position:
            seg = Turtle(shape='square')
            seg.color('white')
            seg.penup()
            seg.goto(coord)
            self.paddle_list.append(seg)

    def game_restart(self,position):
        for id in range(len(self.paddle_list)):
            self.paddle_list[id].goto(position[id])

    def move_up(self):
        if self.paddle_list[-1].ycor() < 280:
            for seg in self.paddle_list:
                seg.goto(seg.xcor(),seg.ycor()+20)

    def move_down(self):
        if self.paddle_list[0].ycor() > -280:
            for seg in self.paddle_list:
                seg.goto(seg.xcor(),seg.ycor()-20)

    def check_hit(self,ball):
        for seg in self.paddle_list:
            if seg.distance(ball) < 25 and (ball.xcor() < 350 or ball.xcor() > 350):
                if ball.heading() == 60:
                    ball.setheading(120)
                elif ball.heading() == 120:
                    ball.setheading(60)
                elif ball.heading() == -60:
                    ball.setheading(-120)
                elif ball.heading() == -120:
                    ball.setheading(-60)
                return True
