from turtle import Turtle, Screen

nikki = Turtle()
nikki.shape("turtle")
nikki.color("green")

def triangle():
    nikki.pencolor("green")
    nikki.forward(100)
    nikki.left(60) 
    nikki.backward(100)
    nikki.left(60)
    nikki.forward(100)
    nikki.right(120)
       
def square():
    for i in range(4):
        nikki.pencolor("black")
        nikki.forward(100)
        nikki.right(90)

def pentagon():
    for i in range(5):
        nikki.pencolor("pink")
        nikki.forward(100)
        nikki.right(72) 
  

def hexagon():
    for i in range(6):
        nikki.pencolor("green")
        nikki.forward(100)
        nikki.right(60) 
  
def heptagon():
    for i in range(7):
        nikki.pencolor("black")
        nikki.forward(100)
        nikki.right(51.4)
        
def octagon():
    for i in range(8):
        nikki.pencolor("green")
        nikki.forward(100)
        nikki.right(45)
        
def nonagon():
    for i in range(9):
        nikki.pencolor("brown")
        nikki.forward(100)
        nikki.right(40)

def decagon():
    for i in range(10):
        nikki.pencolor("gray")
        nikki.forward(100)
        nikki.right(36)   
    
    
    
    
def draw():
    triangle()
    square()
    pentagon()
    hexagon()
    heptagon()
    nonagon()
    decagon()
    
 
#draw()

##optimized version of draw

def draw_shape(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
        nikki.forward(100)
        nikki.right(angle)

for shape_side_n in range(3,11):
    draw_shape(shape_side_n)
    
screen = Screen()
screen.exitonclick()
