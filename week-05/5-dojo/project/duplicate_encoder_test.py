import unittest
from duplicate_encoder import DuplicateEncoder

class TestDuplicateEncoder(unittest.TestCase):
  def test_instantiate(self):
    self.assertIsInstance(DuplicateEncoder(''), DuplicateEncoder)

  def test_encode_char(self):
    subject = DuplicateEncoder('did')
    self.assertEqual(subject.encode_char('d'), ')')
    self.assertEqual(subject.encode_char('i'), '(')

  def test_encoder_when_empty(self):
    self.assertEqual(DuplicateEncoder('').encode(), '')

  def test_encoder(self):
    self.assertEqual(DuplicateEncoder('din').encode(), '(((')
    self.assertEqual(DuplicateEncoder('recede').encode(), '()()()')

  def test_encoder_when_mixed_case(self):
    self.assertEqual(DuplicateEncoder('Success').encode(), ')())())')

unittest.main()
