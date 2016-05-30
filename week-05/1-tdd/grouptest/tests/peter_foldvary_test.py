import unittest
from work import anagramm, count_letters

class TestAnagrammAndCountLetters(unittest.TestCase):
    def setUp(self):
        pass

    def test_anagramm__only_letter_method_correct_result(self):
        result = anagramm('imaliv', 'vilami')
        self.assertEqual(True, result)

    def test_anagramm_method_only_numbers_correct_result(self):
        result = anagramm('123456', '623541')
        self.assertEqual(True, result)

    def test_anagramm_method_letters_and_numbers_correct_result(self):
        result = anagramm('123456asdfg', 'gafsd623541')
        self.assertEqual(True, result)

    def test_anagramm_method_letters_and_numbers_and_asterix_correct_result(self):
        result = anagramm('123456*asdfg', 'gafsd6*23541')
        self.assertEqual(True, result)

    def test_anagramm_method_uppercase_and_lowercase_letters_correct_result(self):
        result = anagramm('1ADS23456*asdfg', 'gafSDsd6*23A541')
        self.assertEqual(True, result)

    def test_anagramm_method_mixed_uppercase_and_lowercase_letters_correct_result(self):
        result = anagramm('Macska', 'MaKaCs')
        self.assertEqual(True, result)

    def test_anagramm_method_mixed_uppercase_and_lowercase_letters_failed_result(self):
        result = anagramm('MacskaI', 'MaKaCsii')
        self.assertEqual(False, result)

    def test_anagramm_method_mixed_letters_with_colon_correct_result(self):
        result = anagramm('Macska:I', 'MaKaCs:i')
        self.assertEqual(True, result)

    def test_anagramm_method_mixed_with_first_letter_space_correct_result(self):
        result = anagramm('Macska I', ' MaKaCsi')
        self.assertEqual(True, result)

    def test_anagramm_method_mixed_with_last_letter_space_correct_result(self):
        result = anagramm('Macska I', 'MaKaCsi ')
        self.assertEqual(True, result)

    def test_count_letters_method_only_lowercase_letters_correct_result(self):
        result = count_letters('kismacska')
        self.assertEqual({'i': 1, 'c': 1, 's': 2, 'm': 1, 'a': 2, 'k': 2}, result)

    def test_count_letters_method_lowercase_and_uppercase_letters_correct_result(self):
        result = count_letters('Kismacska')
        self.assertEqual({'i': 1, 'c': 1, 's': 2, 'm': 1, 'a': 2, 'k': 2}, result)

    def test_count_letters_method_numbers_and_letters_true_if_only_letters_counted_correct_result(self):
        result = count_letters('kismacska 12 kisoccse')
        self.assertEqual({'c': 3, 'i': 2, 's': 4, 'k': 3, 'm': 1, 'e': 1, 'a': 2, 'o': 1}, result)

if __name__ == '__main__':
    unittest.main()
