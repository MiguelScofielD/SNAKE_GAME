from turtle import Turtle

SNAKE_POSITION = [(0,0),(-20,0),(-40,0)]
SNAKE_PASS = 20

class Snake():

    def __init__(self):
        self.snake_pieces = []
        self.create_snake()
        self.head = self.snake_pieces[0]


    def create_snake(self):
        for position in SNAKE_POSITION:
            self.add_piece(position)

    def add_piece(self,position):
        snake_piece = Turtle(shape="square")
        snake_piece.penup()
        snake_piece.color("white")
        snake_piece.goto(position)
        self.snake_pieces.append(snake_piece)

    def new_snake(self):
        self.add_piece(self.snake_pieces[-1].position())

    def reset(self):
        for piece in self.snake_pieces:
            piece.goto(1000,1000)
        self.snake_pieces.clear()
        self.create_snake()
        self.head = self.snake_pieces[0]


    def move(self):
        for i in range(len(self.snake_pieces) - 1, 0, -1):
            self.snake_pieces[i].setpos(self.snake_pieces[i-1].position())
            # snake[1].setpos(snake[0].position())
            # snake[0].setpos(20,0)
        self.snake_pieces[0].forward(SNAKE_PASS)

    def up(self):
        if self.snake_pieces[0].heading() == 270:
            pass
        else:
            self.snake_pieces[0].setheading(90)

    def down(self):
        if self.snake_pieces[0].heading() == 90:
            pass
        else:
            self.snake_pieces[0].setheading(270)
    def right(self):
        if self.snake_pieces[0].heading() == 180:
            pass
        else:
            self.snake_pieces[0].setheading(0)

    def left(self):
        if self.snake_pieces[0].heading() == 0:
            pass
        else:
            self.snake_pieces[0].setheading(180)

    def aumentar(self):
        self.snake_pieces.append()