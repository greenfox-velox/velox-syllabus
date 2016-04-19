import unittest
from intro import MyMagic

class TestIntro(unittest.TestCase):
  def setUp(self):
    self.names = [{ 'id': 1, 'name': 'John'},
                  { 'id': 2, 'name': 'Molly'},
                  { 'id': 3, 'name': 'Jane'}]

  def test_instantiate(self):
    self.assertIsInstance(MyMagic([]), MyMagic)

  def test_names_as_list_when_empty(self):
    subject = MyMagic([])
    self.assertEqual(subject.names_as_list(), [])

  def test_names_as_list(self):
    subject = MyMagic(self.names)
    self.assertEqual(subject.names_as_list(), ['John', 'Molly', 'Jane'])

  def test_names_start_with_j(self):
    subject = MyMagic(self.names)
    self.assertEqual(subject.names_start_with_j(), ['John', 'Jane'])
unittest.main()
