import turtle
import time 
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'yellow', 'brown', 'black', 'cyan']

def get_number_of_turtles():
    racers = 0
    while True: 
        racers = input("Enter the number of turtles (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric! Please enter a number!.")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Please enter a number between 2 and 10!")
            
def race(colors):   
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
            
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles
            
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Dicky Turtle RAce!!")
            
racers = get_number_of_turtles()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

race(colors)
time.sleep(5)
winner = race(colors)
print("The winner is the turtle with color:", winner)