import unittest

# A combinatorics way of finding all subsets of a set
def subsets(my_set):
  subsets = []
  limit = 2 ** len(my_set)

  for i in range(0, limit):
    subset = convert_subset(my_set, i)
    subsets.append(subset)

  return subsets

def convert_subset(my_set, i):
  subset = []
  idx = 0
  j = i

  while j > 0:
    if (j % 2 == 1):
      subset.append(my_set[idx])
    idx += 1
    j = j / 2

  return subset


class TestSubsets(unittest.TestCase):
  def test_empty(self):
    self.assertEqual(subsets([]), [[]])

  def test_ints(self):
    self.assertEqual(
      subsets([1, 2, 3]),
      [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    )

  def test_strings(self):
    self.assertEqual(
      subsets(['a', 'b', 'c']),
      [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    )


if __name__ == '__main__':
    unittest.main()
