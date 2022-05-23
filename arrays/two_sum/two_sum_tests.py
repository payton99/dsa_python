from two_sum import Solution
import unittest

class SumTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_two_integer_list(self):
        self.assertIn(self.sol.twoSum([6, 8], 14), ([0,1], [1, 0]))

    def test_four_integer_list(self):
        self.assertIn(self.sol.twoSum([5, 3, 1, 9], 6), ([0,2], [2, 0]))

    def test_seven_integer_list(self):
        self.assertIn(self.sol.twoSum([3, 6, 2, 1, 1, 7, 4], 2), ([3,4], [4,3]))

if __name__ == '__main__':
    unittest.main()