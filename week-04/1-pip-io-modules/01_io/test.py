import unittest
import basics
import crypto_1dup
import crypto_2revlines
import crypto_3revorder
import crypto_4encoded

class TestIO(unittest.TestCase):

    def setUp(self):
        self.line = 'asdasdsadasad'
        self.content = 'askdaslkdjsalkd\n' + self.line + '\asdasdsadsad'
        self.file_name = 'test.txt'
        self.words = ['This', 'is', 'a', 'long', 'sentence']
        self.sentence = 'This is a long sentence.'
        self.char_codes = [97, 108, 109, 97, 102, 97]
        self.string = 'almafa'

    def test_basics_readfile(self):
        self.create_file_width_content(self.file_name, self.content)
        self.assertEqual(basics.readfile(self.file_name), self.content)

    def test_basics_readline(self):
        self.create_file_width_content(self.file_name, self.content)
        self.assertEqual(basics.readline(self.file_name, 2), self.line)

    def test_basics_words(self):
        self.assertEqual(basics.words(self.sentence), self.words)

    def test_basics_sentence(self):
        self.assertEqual(basics.sentence(self.words), self.sentence)

    def test_basics_char_codes(self):
        self.assertEqual(basics.char_codes(self.string), self.char_codes)

    def test_basics_string(self):
        self.assertEqual(basics.string(self.char_codes), self.string)

    def test_crypto_dup(self):
        self.assertEqual(crypto_1dup.decrypt('texts/duplicated_chars.txt'),
                         self.load_file_content('texts/zen_of_python.txt'))

    def test_crypto_revlines(self):
        self.assertEqual(crypto_2revlines.decrypt('texts/reversed_zen_lines.txt'),
                         self.load_file_content('texts/zen_of_python.txt'))

    def test_crypto_revorder(self):
        self.assertEqual(crypto_3revorder.decrypt('texts/reversed_zen_order.txt'),
                         self.load_file_content('texts/zen_of_python.txt'))

    def test_crypto_encoded(self):
        self.assertEqual(crypto_4encoded.decrypt('texts/duplicated_chars.txt'),
                         self.load_file_content('texts/zen_of_python.txt'))

    def create_file_width_content(self, file_name, content):
        f = open(file_name, 'w')
        f.write(content)
        f.close()

    def load_file_content(self, file_name):
        f = open(file_name)
        result = f.read()
        f.close()
        return result

if __name__ == '__main__':
    unittest.main()
