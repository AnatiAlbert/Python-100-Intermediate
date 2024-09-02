from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_input = screen.textinput(title="Which turtle wins the race?", prompt="Choose your colour")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-80, -50, -20, 10, 40, 70]
all_turtles = []

for t_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[t_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[t_index])
    all_turtles.append(new_turtle)


if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"The winner is {winning_color}. You have won the race.")
            else:
                print(f"The loser is {winning_color}. You have lost the race.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
