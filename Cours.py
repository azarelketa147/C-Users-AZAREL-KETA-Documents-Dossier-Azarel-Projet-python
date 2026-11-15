import turtle as T

t = T.Turtle()
t.speed(0)
t.penup()
t.hideturtle()
couleurs = ["navy", "gold", "red", "green"]

for i in range(36):
    t.goto(-150 + i % 6 * 50, -150 + i // 6 * 50)
    t.color(couleurs[(i % 6 + i // 6) % 4])
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()

T.done()