import unittest
from printer import print_todos

class TestPrinter(unittest.TestCase):
  def test_no_todos(self):
    out = print_todos([])
    self.assertEqual(out, 'No todos for today!')

  def test_one_todo(self):
    out = print_todos(['Monkey'])
    self.assertEqual(out, '1 - Monkey\n')

  def test_two_todo(self):
    out = print_todos(['Monkey', 'Ape'])
    self.assertEqual(out, '1 - Monkey\n2 - Ape\n')

unittest.main()
