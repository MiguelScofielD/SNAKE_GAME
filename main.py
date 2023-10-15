from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# snake = []
#
# for i in range(3):
#     snake_piece = Turtle(shape="square")
#     snake_piece.penup()
#     snake_piece.color("white")
#     snake_piece.goto(-20*i,0)
#     snake.append(snake_piece)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


# time.sleep(1)

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.new_snake()
        food.refresh()
        scoreboard.increase_score()
        print("yomi yomi")

    if snake.head.xcor() > 300 or snake.head.xcor() < -300:
        # game_is_on = False
        # scoreboard.GameOver()
        scoreboard.reset()
        snake.reset()
    if snake.head.ycor() > 300 or snake.head.ycor() < -290:
        # game_is_on = False
        # scoreboard.GameOver()
        scoreboard.reset()
        snake.reset()

    for piece in snake.snake_pieces[1:]:
        if snake.head.distance(piece) < 10:
            # game_is_on = False
            # scoreboard.GameOver()
            scoreboard.reset()
            snake.reset()


#     for i in range(len(snake)-1,0,-1):
#         snake[i].setpos(snake[i-1].position())
#         # snake[1].setpos(snake[0].position())
#         # snake[0].setpos(20,0)
#     snake[0].forward(20)
screen.exitonclick()
