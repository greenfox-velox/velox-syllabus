import unittest
import vector

class TestVector(unittest.TestCase):
    def test_add_vector(self):
        result = vector.add((10, 20), (30, 40))
        self.assertEqual(result, (40, 60))

    def test_multiply_vector(self):
        result = vector.multiply((10, 20), 4)
        self.assertEqual(result, (40, 80))

unittest.main()


