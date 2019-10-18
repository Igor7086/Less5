from Less5_3 import ITEmployee
import unittest


class MyTests1(unittest.TestCase):

    def test_ITEmployee(self):
        res = ITEmployee('Python')
        self.assertEqual(res, "Python")


if __name__ == "__main__":
    unittest.main()
