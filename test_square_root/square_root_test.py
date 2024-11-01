import unittest
from square_roots import get_square_roots


class TestSqrtFunction(unittest.TestCase):
    def test_a_is_zero(self):
        self.assertAlmostEqual(get_square_roots(0, 5, 10), (-2,))
        result_1 = get_square_roots(0, 5, 10)
        self.assertEqual(len(result_1), 1)
        self.assertAlmostEqual(result_1[0], -2)

    def test_a_is_zero_b_is_zero(self):
        self.assertAlmostEqual(get_square_roots(0, 0, 5), tuple())

    def test_b_is_zero_c_negative(self):
        result_1 = sorted(get_square_roots(1, 0, -25))

        self.assertEqual(len(result_1), 2)
        self.assertAlmostEqual(result_1[0], -5)
        self.assertAlmostEqual(result_1[1], 5)

        result_2 = get_square_roots(2445, 0, 0)
        self.assertEqual(len(result_2), 1)
        self.assertAlmostEqual(result_2[0], 0)

    def test_b_is_zero_c_positive(self):
        result = get_square_roots(1, 0, 25)
        self.assertEqual(result, tuple())

    def test_c_is_zero(self):
        result = sorted(get_square_roots(2, 4, 0))
        self.assertEqual(len(result), 2)

        self.assertAlmostEqual(result[0], 0)
        self.assertAlmostEqual(result[1], -2)

    def test_d_greater_than_zero(self):
        result = sorted(get_square_roots(2, -3, 1))
        self.assertEqual(len(result), 2)

        self.assertAlmostEqual(result[0], 0.5)
        self.assertAlmostEqual(result[1], 1)


        result_2 = sorted(get_square_roots(12, 7, -3))
        self.assertEqual(len(result_2), 2)
        self.assertAlmostEqual(result_2[0], -0.87052, 4)
        self.assertAlmostEqual(result_2[1], 0.28719, 4)



    def test_d_lower_than_zero(self):
        result = get_square_roots(50, -1, 1)
        self.assertEqual(result, tuple())

    def test_d_is_zero(self):
        result = get_square_roots(1, 2, 1)
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0], -1)
    # def test_negative_number(self):
    #     with self.assertRaises(ValueError):
    #         get_square_roots(-4)

if __name__ == "__main__":
    unittest.main()