import unittest
from work import anagramm, count_letters

class DayOneTestCases(unittest.TestCase):
	def setUp(self):
		pass

	def test_anagramm_basic(self):
		self.assertTrue(anagramm("Madam Curie", "Radium came"))

	def test_anagramm_without_string(self):
		self.assertFalse(anagramm(123, "Yolo"))

	def test_anagramm_different_lenght(self):
		self.assertFalse(anagramm("Abba", "ab"))

	def test_anagramm_empty_input(self):
		self.assertFalse(anagramm("", ""))

	def test_anagramm_random_anagramms(self):
		self.assertTrue(anagramm("Arrigo Boito", "Tobia Gorrio"))
		self.assertFalse(anagramm("Ted Morgan", "dEt Yorgen"))

	def test_count_letters_compare_with_Hello(self):
		hello_count = {'H': 1, 'l': 2, 'o': 1, 'e': 1}
		self.assertEqual(hello_count, count_letters("Hello"))

	def test_count_letters_int_input(self):
		self.assertFalse(count_letters(123))

	def test_count_letters_long_string(self):
		long_string = "abcdefghijklmnopqrst" * 100
		a_count = 100
		self.assertEqual(a_count, count_letters(long_string)['a'])

if __name__ == '__main__':
	unittest.main()
