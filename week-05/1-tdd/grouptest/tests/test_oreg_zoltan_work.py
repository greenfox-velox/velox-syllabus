import unittest
from work import anagramm
from work import count_letters

class AnagrammAndCountLettersTest(unittest.TestCase):

    def test_if_anagramm_abrak(self):
        self.assertTrue(anagramm('abrak','akraB'))

    def test_if_anagramm_qwer(self):
        self.assertTrue(anagramm('qwer tzu','UzTwerq '))

    def test_if_anagramm_qwer_mnb(self):
        self.assertFalse(anagramm('mnbmnb','mnb mnb'))


    def test_count_letters_asd(self):
        self.assertEqual(count_letters('asdssdd a'), ({'a':2, 's':3, 'd':3}))

    def test_count_letters_stars(self):
        self.assertEqual(count_letters('**01 *01 *a'), ({'a':1}))

    def test_count_letters_stars_vv(self):
        self.assertEqual(count_letters(' VVqqovv '), ({'v':4, 'q':2, 'o':1}))

if __name__ == '__main__':
    unittest.main()
