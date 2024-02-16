#!/usr/bin/python3
"""Rectangle module."""
import json
import csv
from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        self.__validate_positive_int("width", value)
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        self.__validate_positive_int("height", value)
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        self.__validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        self.__validate_int("y", value)
        self.__y = value

    def __validate_int(self, attribute, value):
        """Validate if a value is an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))

    def __validate_positive_int(self, attribute, value):
        """Validate if a value is a positive integer."""
        self.__validate_int(attribute, value)
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """Compute area."""
        return self.width * self.height

    def display(self):
        """Display the rectangle."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """String representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Update attributes."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return list of dictionaries represented by json_string."""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list_objs to a file in JSON format."""
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Load list_objs from a file in JSON format."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares."""
        import turtle

        turtle.bgcolor("white")
        turtle.title("Draw Rectangles and Squares")

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list_objs to a file in CSV format."""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y]
                        )
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load list_objs from a file in CSV format."""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                list_objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls.create(
                            id=int(row[0]),
                            width=int(row[1]),
                            height=int(row[2]),
                            x=int(row[3]),
                            y=int(row[4]),
                        )
                    elif cls.__name__ == "Square":
                        obj = cls.create(
                            id=int(row[0]),
                            size=int(row[1]),
                            x=int(row[2]),
                            y=int(row[3]),
                        )
                    list_objs.append(obj)
                return list_objs
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

