import unittest

'''
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

# O(N) time complexity, O(N) space complexity
def is_unique1(string):
  return len(string) == len(set(string))

# O(N^2) time complexity, O(1) space complexity
def is_unique2(string):
  for i in range(0, len(string)):
    for j in range(i + 1, len(string)):
      if string[i] == string[j]:
        return False
  return True


class TestIsUnique(unittest.TestCase):
  def test_is_unique1_positive(self):
    self.assertEqual(is_unique1('abcde'), True)

  def test_is_unique2_positive(self):
    self.assertEqual(is_unique2('abcde'), True)

  def test_is_unique1_negative(self):
    self.assertEqual(is_unique1('fobaro'), False)

  def test_is_unique2_negative(self):
    self.assertEqual(is_unique2('fobaro'), False)

if __name__ == '__main__':
  unittest.main()