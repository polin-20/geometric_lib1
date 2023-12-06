import unittest
import math
import circle.py
import rectangle.py
import square.py
import triangle.py

class TestTriangleCase(unittest.TestCase):
    def test_triangle_area(self):
        test_data = ((1,1,0.5), (2,4,4), (5,8,20))
        for a,b,c in test_data:
            res = area(a,b)
            self.assertEqual(res, c)
            
    def test_triangle_perimetr(self):
        test_data = ((1,1,1,3), (2,4,6,12))
        for a,b,c,d in test_data:
            res = perimetr(a, b, c)
            self.assertEqual(res, d)

class TestSquareCase(unittest.TestCase):
    def test_square_area(self):
        test_data = ((1,1), (2,4), (5,25))
        for a,b in test_data:
            res = area(a)
            self.assertEqual(res, b)
            
    def test_square_perimetr(self):
        test_data = ((1,4), (2,8), (5,40))
        for a,b in test_data:
            res = perimetr(a)
            self.assertEqual(res, b)

class TestRectangleCase(unittest.TestCase):
    def test_rectangle_area(self):
        test_data = ((1,1,1), (2,4,8), (5,8,40))
        for a,b,c in test_data:
            res = area(a,b)
            self.assertEqual(res, c)
            
    def test_rectangle_perimetr(self):
        test_data = ((1,1,4), (2,4,12), (5,8,26))
        for a,b,c in test_data:
            res = perimetr(a, b)
            self.assertEqual(res, c)


class TestCircleCase(unittest.TestCase):
    def test_circle_area(self):
        test_data = ((1,1*math.pi), (2,4*math.pi), (5,25*math.pi))
        for a,b in test_data:
            res = area(a)
            self.assertEqual(res, b)
            
    def test_circle_perimetr(self):
        test_data = ((1,2*math.pi), (2,4*math.pi), (5,10*math.pi))
        for a,b in test_data:
            res = perimetr(a)
            self.assertEqual(res, b)


