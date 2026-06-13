import turtle

screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color :")

colors = ["red","orange","yellow","green","blue","purple","cyan"]
index = 0;
for color in colors:
    tim = turtle.Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    tim.goto(-230,-150 + (index * 50))
    index += 1

screen.exitonclick()

