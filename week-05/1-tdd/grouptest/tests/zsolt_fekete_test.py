import unittest
from work import anagramm
from work import count_letters

class Test(unittest.TestCase):

    def test_is_it_anagramm_simple(self):
        self.assertTrue(anagramm('alma','mala'))

    def test_is_it_anagramm_empty(self):
        self.assertFalse(anagramm('',''))

    def test_is_it_anagramm_double_letter(self):
        self.assertFalse(anagramm('allam','malam'))

    # def test_is_it_anagramm_Uper_letter(self):
    #     self.assertFalse(anagramm('Alma','mAlA'))
    #
    # def test_is_it_anagramm_number_in_the_letter(self):
    #     self.assertFalse(anagramm('alma1','1mala'))

    # def test_is_it_anagramm_number(self):
    #     self.assertFalse(anagramm('110','011'))
    #
    # def test_is_it_anagramm_special_character(self):
    #     self.assertFalse(anagramm('a-lma','mal-a'))
    #
    # def test_is_it_anagramm_space(self):
    #     self.assertFalse(anagramm('al ma','m ala'))
    #
    # def test_is_it_anagramm_space(self):
    #     self.assertFalse(anagramm('al ma','m ala'))
    #
    # def test_is_it_anagramm_space(self):
    #     self.assertFalse(anagramm('al ma','m ala'))

    def test_count_letters_simple(self):
        self.assertEqual(count_letters('macska'),count_letters('acskam'))

    # def test_count_letters_special_character(self):
    #     self.assertFalse(count_letters('ma cs-ka'),count_letters('ac-sk am'))

    def test_count_letters_empty(self):
        self.assertFalse(count_letters(''),{})




if __name__ == '__main__':
    unittest.main()
