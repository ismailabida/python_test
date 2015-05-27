import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('ismail'.upper(), 'ISMAIL')

  def test_isupper(self):
      self.assertTrue('ISMAIL'.isupper())
      self.assertFalse('ismail'.isupper())

  def test_split(self):
      s = 'Bonjour tout le monde'
      self.assertEqual(s.split(), ['Bonjour', 'tout', 'le', 'monde'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()

