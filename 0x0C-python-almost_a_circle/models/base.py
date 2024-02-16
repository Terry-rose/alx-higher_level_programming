#!/usr/bin/python3
"""Base module."""
import turtle


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using Turtle graphics."""
        turtle.clear()
        turtle.bgcolor("white")
        turtle.title("Draw Rectangles and Squares")
        turtle.speed(2)

        def draw_shape(obj, color):
            turtle.penup()
            turtle.goto(obj.x - obj.width / 2, obj.y - obj.height / 2)
            turtle.pendown()
            turtle.color(color)
            turtle.begin_fill()
            for _ in range(4):
                if _ % 2 == 0:
                    turtle.forward(obj.width)
                else:
                    turtle.forward(obj.height)
                turtle.left(90)
            turtle.end_fill()

        for rect in list_rectangles:
            draw_shape(rect, "blue")

        for square in list_squares:
            draw_shape(square, "red")

        turtle.done()


if __name__ == "__main__":
    # Sample usage
    from models.rectangle import Rectangle
    from models.square import Square

    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)

