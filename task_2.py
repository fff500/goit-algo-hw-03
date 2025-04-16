import turtle
import argparse

parser = argparse.ArgumentParser(description="Draw a Koch snowflake using recursion.")
parser.add_argument("level", type=int, help="Recursion depth level")
args = parser.parse_args()

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        koch_snowflake(t, length / 3, level - 1)
        t.left(60)
        koch_snowflake(t, length / 3, level - 1)
        t.right(120)
        koch_snowflake(t, length / 3, level - 1)
        t.left(60)
        koch_snowflake(t, length / 3, level - 1)

def draw_koch_snowflake(level):
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-150, 150)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, 450, level)
        t.right(120)

    window.mainloop()

def main():
    draw_koch_snowflake(args.level)

if __name__ == "__main__":
    main()
