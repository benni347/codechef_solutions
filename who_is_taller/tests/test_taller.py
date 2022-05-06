import unittest
import taller

class TestTaller(unittest.TestCase):

    def test_get_taller_A(self):
        t = taller.Taller()
        t.a = 654
        t.b = 321
        self.assertEqual(t.get_taller(), "A", "Should be A")

    def test_get_taller_B(self):
        t = taller.Taller()
        t.a = 123
        t.b = 456
        self.assertEqual(t.get_taller(), "B", "Should be B")

    def test_get_taller_NegativeA(self):
        t = taller.Taller()
        t.a = -1
        t.b = 456
        self.assertEqual(t.get_taller(), "B", "Should be B")

    def test_get_taller_LetterA(self):
        t = taller.Taller()
        t.a = "a"
        t.b = 456
        self.assertEqual(t.get_taller(), "TypeError", "Should be TypeError")
    # def test_get_taller_ERR(self):
    #     t = taller.Taller()
    #     t.a = 987
    #     t.b = 456
    #     self.assertEqual(t.get_taller(), "AssertionError", "Should be AssertionError")


if __name__ == '__main__':
    unittest.main()
