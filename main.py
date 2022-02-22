import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()

MICHELANGELO_START = (-100, 20)
LEONARDO_START = (-100, -20)

michelangelo.goto(MICHELANGELO_START)
leonardo.goto(LEONARDO_START)

## 5. your code goes here

#Race Option 2

RACE_INTERVAL = 10
MAX_SPEED = 10
for i in range(RACE_INTERVAL):
  ##leo_move = random.choice(range(MAX_SPEED))
  leonardo.forward(random.choice(range(MAX_SPEED)))
  michelangelo.forward(random.choice(range(MAX_SPEED)))

michelangelo.goto(MICHELANGELO_START)
leonardo.goto(LEONARDO_START)

# Part B - complete part B here
triangle = (3, 10)
square = (4, 10)
hexagon = (6, 10)
nonagon = (9, 10)
dodecagon = (12, 10)

shapeArray = [triangle, square, hexagon, nonagon, dodecagon]

def generateShape(sides, length, isRepeated):
  for i in range(sides):
    leonardo.forward(length)
    leonardo.left(360/sides)
  leonardo.clear()
  if isRepeated:
    getShapeData()
  
def getShapeData():
  sides = int(input("Enter number of sides: "))
  length = int(input("Enter length of each side: "))
  generateShape(sides, length, True)

leonardo.down()

for side, length in shapeArray:
  generateShape(side, length, False)

getShapeData()
window.exitonclick()