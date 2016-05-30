import unittest
from work import anagramm, count_letters

class TestCount_and_sorting_method(unittest.TestCase):
        def test_sorting(self):
            self.assertEqual(anagramm('aa', 'aa'), True)
            self.assertEqual(anagramm('aa', 'ac'), False)
            self.assertEqual(anagramm('aa1A', '1aaa'), True)
            self.assertEqual(anagramm('cCc', 'aAa'), False)
            self.assertEqual(anagramm('cCc', 'CcC'), True)


        def test_count(self):
            #self.create_file_width_content(self.file_name, self.content)
            self.assertEqual(count_letters('c'), {'c':1})
            self.assertEqual(count_letters('assa'), {'a':2, 's':2})
            self.assertEqual(count_letters('c11'), {'c':1, '1':2})
            self.assertEqual(count_letters('cc12'), {'c':2, '1':1, '2':1})
            self.assertEqual(count_letters('bbb'), {'b':3})


if __name__ == '__main__':
    unittest.main()
