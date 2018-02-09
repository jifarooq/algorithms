'''
1.6 String Compression: 
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the 'compressed' string would not become smaller than the original string, 
your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a - z).
'''

import unittest

def compress(string):
  compressed = ''
  count = 1

  for i, char in enumerate(string):
    if i == 0:
      continue
    prev_char = string[i - 1]

    if char == prev_char:
      count += 1
    else:
      compressed += prev_char + str(count)
      count = 1

  compressed += char + str(count)
  return compressed if len(compressed) < len(string) else string


class TestSubsets(unittest.TestCase):
  def test_provided_example(self):
    self.assertEqual(compress('aabcccccaaa'), 'a2b1c5a3')

  def test_return_of_original_string(self):
    self.assertEqual(compress('aabbcc'), 'aabbcc')

  def test_return_compressed_if_just_shorter_than_original(self):
    self.assertEqual(compress('aabbccc'), 'a2b2c3')

if __name__ == '__main__':
    unittest.main()
