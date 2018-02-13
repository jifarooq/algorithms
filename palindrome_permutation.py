import unittest
import random

'''
1.4 Palindrome Permutation: 
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE Input: Tact Coa Output: True (permutations: 'taco cat', 'atco eta', etc.)
'''

def palindrome_permutation(string):
  if not string:
    return False

  even_odd_flags = {}

  for char in string:
    if char == ' ':
      continue
    flag = even_odd_flags.get(char, 0)
    even_odd_flags[char] = 0 if flag else 1

  sum_flags = sum(even_odd_flags.values())
  return sum_flags == 0 or sum_flags == 1


class TestPalindromePermutation(unittest.TestCase):
  def test_single_word_palindrome(self):
    self.assertEqual(palindrome_permutation('carrace'), True)

  def test_non_palindrome(self):
    self.assertEqual(palindrome_permutation('apple'), False)

  def test_multiple_words_palindrome(self):
    chars = list('no lemon no melon')
    shuffled_str = ''.join(random.sample(chars, len(chars)))
    self.assertEqual(palindrome_permutation(shuffled_str), True)

  def test_blank_string_returns_false(self):
    self.assertEqual(palindrome_permutation(''), False)

if __name__ == '__main__':
    unittest.main()
