from turtle import Turtle, Screen
from random import randint

fruit = Turtle()
sc = Screen()
sc.addshape("img/raspberry.gif")

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("img/raspberry.gif")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
