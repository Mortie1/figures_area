from abc import ABC, abstractmethod
from math import pi, sqrt


class BaseFigure(ABC):
    @abstractmethod
    def area(self) -> float:
        return 0.0


class Circle(BaseFigure):
    def __init__(self, radius: float = 1.0) -> None:
        if radius <= 0:
            raise ValueError("radius must be a positive float")
        self.radius = radius

    def area(self) -> float:
        return self.radius * self.radius * pi


class Triangle(BaseFigure):
    def __init__(self, side1: float = 0, side2: float = 0, side3: float = 0) -> None:
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise AttributeError(
                "provided sides do not form a triangle (triangle inequality does not hold)"
            )
        self.side1, self.side2, self.side3 = side1, side2, side3

    def area(self) -> float:
        a, b, c = self.side1, self.side2, self.side3
        s = (a + b + c) / 2
        # Heron's formula (https://en.wikipedia.org/wiki/Heron%27s_formula)
        return sqrt(s * (s - a) * (s - b) * (s - c))

    def is_right(self) -> bool:
        a2, b2, c2 = (
            self.side1 * self.side1,
            self.side2 * self.side2,
            self.side3 * self.side3,
        )
        # Pythagorean theorem (https://en.wikipedia.org/wiki/Pythagorean_theorem)
        return (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2)

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

# class for representing figures with unknown shape. I assume that it is a simple polygon with known vertices
class Figure(BaseFigure):
    def __init__(self, vertices: list[Point] = []) -> None:
        if len(vertices) < 3:
            raise AttributeError("Provided points do not form a polygon - there must be at least 3 points")
        # here should be more checkers to find out if it is a simple polygon
        
        self.vertices = vertices

    def area(self) -> float:
        s = 0
        # shoelace formula (https://en.wikipedia.org/wiki/Shoelace_formula)
        vertices = self.vertices
        for i in range(len(vertices)):
            point1 = vertices[i - 1]
            point2 = vertices[i]
            s += (point2.x - point1.x) * (point2.y + point1.y)
        return abs(s / 2)