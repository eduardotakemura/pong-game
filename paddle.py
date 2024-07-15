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
        for pos, seg in enumerate(self.paddle_list):
            # Check if there was a collision #
            if seg.distance(ball) < 25 and (ball.xcor() < 350 or ball.xcor() > 350):
                # Check seg hit #
                if pos == 0:
                    if 90 < ball.heading() < 270:
                        ball.setheading(300)
                    else:
                        ball.setheading(240)
                elif pos == 1:
                    if 90 < ball.heading() < 270:
                        ball.setheading(315)
                    else:
                        ball.setheading(225)
                elif pos == 3:
                    if 90 < ball.heading() < 270:
                        ball.setheading(45)
                    else:
                        ball.setheading(135)
                elif pos == 4:
                    if 90 < ball.heading() < 270:
                        ball.setheading(60)
                    else:
                        ball.setheading(120)
                else:
                    if 0 < ball.heading() < 90:
                        ball.setheading(300)
                    elif 90 < ball.heading() < 180:
                        ball.setheading(240)
                    elif 180 < ball.heading() < 270:
                        ball.setheading(120)
                    else:
                        ball.setheading(60)
                return True
