import turtle as turtle_module
import random
import colorgram

tim = turtle_module.Turtle()
tim.shape("turtle")
tim.color("red")
colors = ["red","green","blue","orange","gray","pink","aquamarine","purple"]

def draw_shape(num_corner):
    for i in range(num_corner):
        tim.right(360/num_corner)
        tim.forward(150)
    

def shape():
    for i in range(3,11):
        tim.color(colors[i - 3])
        draw_shape(i)

# Draw a randome walk
def draw_random_walk():
    tim.pensize(10)
    tim.speed(200)
    angle = [90, 180, 270, 360]
    for i in range(100):
        tim.color(random.choice(colors))
        tim.forward(30)
        tim.setheading(random.choice(angle))


# draw a spirograph
def draw_spirograph(size_of_gap):
    tim.speed(300)
    for i in range(int(360 / size_of_gap)):
        tim.color(random.choice(colors))
        tim.circle(50)
        tim.right(i + size_of_gap)
    

# draw hirst painting 
def getColorRgb(color):
    return (color.rgb)

def draw_hirst_painting():
    tim.hideturtle()
    turtle_module.colormode(255)
    tim.penup()
    colors = colorgram.extract("hirst-spot.jpg",30)
    tim.speed("fastest")
    tim.setposition(-200,0)
    multiply = 50
    index = 1
    for color in colors:
        new_color = getColorRgb(color)
        tim.dot(15,new_color.r, new_color.g, new_color.b)
        tim.forward(50)             
        if index % 5 == 0:
            tim.setposition(-200, multiply)
            multiply += 50

        index += 1
    # tim.speed("fastest")
    # index = 0
    # for row in colors:
    #     tim.penup()
    #     tim.setposition(-200,index)
    #     for color in row:
    #         tim.fillcolor(color)
    #         tim.begin_fill()
    #         tim.circle(10)
    #         tim.end_fill()
    #         tim.forward(30)
    #         tim.pendown()


    #     index += 30
draw_hirst_painting()

screen = turtle_module.Screen()
screen.exitonclick()