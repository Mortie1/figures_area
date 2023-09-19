import unittest
from math import pi
from src.figures.figures import Circle, Triangle, Figure, Point

class TestCircle(unittest.TestCase):
    
    def test_creation_of_circle(self):
        self.assertRaises(ValueError, Circle, 0)
        self.assertRaises(ValueError, Circle, -1)
        try:
            Circle(1)
        except ValueError:
            self.fail("Circle constructor raised ValueError unexpectedly!")
    
    def test_simple_circle_area(self):
        circle = Circle(radius=1.0)
        self.assertEqual(circle.area(), pi)
    
    def test_complex_circle_area(self):
        r = 7.34
        circle = Circle(radius=r)
        self.assertEqual(circle.area(), pi * r * r)


class TestTriangle(unittest.TestCase):
    
    def test_creation_of_triangle(self):
        self.assertRaises(AttributeError, Triangle, 0, 0, 0)
        self.assertRaises(AttributeError, Triangle, -1, -2, -2)
        try:
            Triangle(1, 2, 2)
        except AttributeError:
            self.fail("Triangle constructor raised AttributeError unexpectedly!")
    
    def test_simple_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)

    def test_simple_triangle_rightness(self):
        right_triangle = Triangle(3, 4, 5)
        self.assertTrue(right_triangle.is_right())
        not_right_triangle = Triangle(3, 4, 6)
        self.assertFalse(not_right_triangle.is_right())


class TestFigure(unittest.TestCase):
    def test_creation_of_figure(self):
        self.assertRaises(AttributeError, Figure, [Point(0, 0), Point(1, 1)])
        self.assertRaises(AttributeError, Figure, [Point(1, 2)])
        try:
            Figure([Point(0, 0), Point(1, 1), Point(1, 2)])
        except AttributeError:
            self.fail("Triangle constructor raised AttributeError unexpectedly!")

    def test_simple_figure_area(self):
        figure = Figure([Point(0, 0), Point(1, 0), Point(0, 1)])
        self.assertEqual(figure.area(), 0.5)
        figure = Figure([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])
        self.assertEqual(figure.area(), 1)
        figure = Figure([Point(0, 0), Point(-1, 1), Point(0, 2), Point(1, 1)])
        self.assertEqual(figure.area(), 2)

    def test_complex_figure_area(self):
        figure = Figure([Point(0, 0), Point(-1, 1), Point(-1, 2), Point(0, 3), Point(1, 2), Point(1, 1)])
        self.assertEqual(figure.area(), 4)
        figure = Figure([Point(0, 0), Point(-2, 1.5), Point(-0.5, 2), Point(0, 3), Point(0.5, 1), Point(1, 1)])
        self.assertEqual(figure.area(), 3.375)

if __name__ == "__main__":
    unittest.main()