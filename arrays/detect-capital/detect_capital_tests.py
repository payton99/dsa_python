from detect_capital import Solution
import unittest

class CapitalTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_upper_all_letters(self):
        self.assertTrue(self.sol.detectCapitalUse("USA"))
    
    def test_upper_last_letter(self):
        self.assertFalse(self.sol.detectCapitalUse("usA"))
    
    def test_lower_all_letters(self):
        self.assertTrue(self.sol.detectCapitalUse("hamburger"))

    def test_lower_last_letters(self):
        self.assertFalse(self.sol.detectCapitalUse("hamburgER"))

    def test_title_case(self):
        self.assertTrue(self.sol.detectCapitalUse("Egypt"))

    def test_broken_title_case(self):
        self.assertFalse(self.sol.detectCapitalUse("eGypt"))
        self.assertFalse(self.sol.detectCapitalUse("egYpt"))
        self.assertFalse(self.sol.detectCapitalUse("egyPt"))
        self.assertFalse(self.sol.detectCapitalUse("egypT"))

if __name__ == '__main__':
    unittest.main() 
        