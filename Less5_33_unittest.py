from Less5.Less5_modules_for_tests import is_year_leap, triangle, what_triangle
import unittest


class MyTests(unittest.TestCase):

    def test_is_year_leap(self):
        res = is_year_leap(2000)
        res1 = is_year_leap(2001)
        self.assertEqual(res, True)
        self.assertEqual(res1, False)

    def test_triangle(self):
        res = triangle(0,0,0)
        self.assertEqual(res, False)

    def test_what_triangle(self):
        res = what_triangle(1, 1, 1)
        self.assertEqual(res, "Equilateral triangle")


if __name__ == "__main__":
    unittest.main()


