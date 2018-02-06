import unittest

'''
Living People: Given a list of people with their birth and death years, 
implement a method to compute the year with the most number of people alive.
You may assume that all people were born between 1900 and 2000 (inclusive).
If a person was alive during any portion of that year, they should be included in that year's count. 
For example, Person (birth= 1908, death= 1909) is included in the counts for both 1908 and 1909.
'''

# runs in O(P log P) time with P = number of people or year-pairs
def most_living_people(persons):
  births = set(map(lambda y:y[0], persons))
  deaths = set(map(lambda y:y[1], persons))
  sorted_years = sorted(births.union(deaths))

  populations = {}
  populations[sorted_years[0]] = 1  #earliest year must be a birth year

  for i, year in enumerate(sorted_years):
    if i == 0:
      continue
    delta = 1 if (year in births) else -1
    last = sorted_years[i - 1]
    populations[year] = populations[last] + delta

  return max(populations, key=populations.get)


class TestLivingPeople(unittest.TestCase):
  def test_normal_use_case(self):
    persons = [(1920, 1939), (1911, 1944), (1920, 1955), (1938, 1939)]
    self.assertEqual(most_living_people(persons), 1938)

if __name__ == '__main__':
    unittest.main()