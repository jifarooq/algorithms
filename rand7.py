'''
16.23 Rand7 from Rands: 
Implement a method rand7() given rand5(). 
That is, given a method that generates a random number between O and 4 (inclusive), 
write a method that generates a random number between O and 6 (inclusive).
'''

import random
import unittest

def rand7():
  total = 5 * rand5() + rand5()
  return total / 3 if total < 21 else rand7()

def rand5():
  return random.randint(0, 4)


class TestRand7(unittest.TestCase):

  # Will fail about .083% of the time due to [pseudo] randomness!
  def test_equal_distribution_of_ints(self):
    # We can expect an average count of 126 for each number from 0 to 6
    avg_count = 126
    deviation = 40
    sample_size = 882
    counts = {}

    for i in range(0, sample_size):
      num = rand7()
      counts[num] = counts.get(num, 0) + 1

    for j in range(0, 7):
      self.assertTrue(avg_count - deviation <= counts[j] <= avg_count + deviation)


if __name__ == '__main__':
    unittest.main()
