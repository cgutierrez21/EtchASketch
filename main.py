import turtle as t

screen = t.Screen()

cursor = t.Turtle()

def turn_left():
    cursor.setheading(cursor.heading() + 5)

def turn_right():
    cursor.setheading(cursor.heading() - 5)

def go_forward():
    cursor.forward(10)

screen.onkeypress(turn_left, 'Left')
screen.onkeypress(turn_right, 'Right')
screen.onkeypress(go_forward, 'Up')
screen.listen()











screen.mainloop()