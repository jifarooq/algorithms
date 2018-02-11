'''
16.24 Pairs with Sum:
Design an algorithm to find all [unique] pairs of integers within an array 
which sum to a specified value.
'''

import unittest

def pair_sums(array, target):
  pair_sums = []
  nums = set()

  for i, num in enumerate(array):
    if (target - num) in nums:
      pair_sums.append((num, target - num))
    else:
      nums.add(num)

  return pair_sums


class TestPairSums(unittest.TestCase):
  def test_finds_all_pairs_that_sum_to_target(self):
    self.assertEqual(
      pair_sums([1, 5, 3, 7, -1], 6),
      [(5, 1), (-1, 7)]
    )

if __name__ == '__main__':
    unittest.main()
