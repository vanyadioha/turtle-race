from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(700, 600)
user_bet = screen.textinput(
    "MAKE YOUR BET", "Which turle color will win? Enter a color from the rainbow: "
).lower()
print(f"Your bet was {user_bet}. Goodluck!\n")
roygbiv = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
mbe_list = []

for i in range(7):
    mbe = Turtle("turtle")
    mbe.penup()
    mbe.color(roygbiv[i])
    mbe.goto(-340, -180 + (60 * i))
    mbe_list.append(mbe)

if user_bet:
    is_race_on = True
while is_race_on:
    for mbe in mbe_list:
        if mbe.xcor() > 310:
            winner = mbe.pencolor()
            if winner == user_bet:
                print(f"You won! {winner.title()} was the winning turtle")
            else:
                print(f"You lost! {winner.title()} was the winning turtle")
            is_race_on = False
        speed = randint(0, 10)
        mbe.forward(speed)


screen.exitonclick()
