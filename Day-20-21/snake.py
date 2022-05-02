from turtle import Turtle

position_segment = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down =270
left = 180
right = 0
class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]


    def create_snake(self):
        for position in position_segment:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.width(20)
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            cor_x = self.segment[seg_num - 1].xcor()
            cor_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(cor_x, cor_y)
        self.head.forward(move_distance)


    def up(self):
        if self.head.heading() != down:
           self.head.setheading(up)


    def down(self):
        if self.head.heading() != up:
           self.head.setheading(down)


    def right(self):
        if self.head.heading() != left:
           self.head.setheading(right)


    def left(self):
        if self.head.heading() != right:
           self.head.setheading(left)

