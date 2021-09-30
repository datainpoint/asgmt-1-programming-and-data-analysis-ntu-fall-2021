import unittest
import ipynb.fs.full.exercises as ex

class TestAssignmentOne(unittest.TestCase):
    def test_01_calculate_movie_minutes(self):
        self.assertEqual(ex.calculate_movie_minutes(2, 22), 142)
        self.assertEqual(ex.calculate_movie_minutes(2, 55), 175)
        self.assertEqual(ex.calculate_movie_minutes(2, 32), 152)
    def test_02_convert_kilometer_to_mile(self):
        self.assertTrue(ex.convert_kilometer_to_mile(42.195) > 26)
        self.assertTrue(ex.convert_kilometer_to_mile(21.095) > 13)
    def test_03_convert_fahrenheit_to_celsius(self):
        self.assertTrue(ex.convert_fahrenheit_to_celsius(212) > 99)
        self.assertTrue(ex.convert_fahrenheit_to_celsius(212) < 101)
        self.assertTrue(ex.convert_fahrenheit_to_celsius(32) > -1)
        self.assertTrue(ex.convert_fahrenheit_to_celsius(32) < 1)
    def test_04_calculate_bmi(self):
        self.assertTrue(ex.calculate_bmi(216, 147) > 31)
        self.assertTrue(ex.calculate_bmi(216, 147) < 32)
        self.assertTrue(ex.calculate_bmi(206, 113) > 26)
        self.assertTrue(ex.calculate_bmi(206, 113) < 27)
        self.assertTrue(ex.calculate_bmi(211, 110) > 24)
        self.assertTrue(ex.calculate_bmi(211, 110) < 25)
        self.assertTrue(ex.convert_fahrenheit_to_celsius(212) < 101)
        self.assertTrue(ex.convert_fahrenheit_to_celsius(32) > -1)
        self.assertTrue(ex.convert_fahrenheit_to_celsius(32) < 1)
    def test_05_show_integer_with_commas(self):
        self.assertEqual(ex.show_integer_with_commas(1000), "1,000")
        self.assertEqual(ex.show_integer_with_commas(1000000), "1,000,000")
        self.assertEqual(ex.show_integer_with_commas(1000000000), "1,000,000,000")
    def test_06_show_big_mac_index(self):
        self.assertEqual(ex.show_big_mac_index('US', 'USD', 5.65), "A Big Mac costs 5.65 USD in US.")
        self.assertEqual(ex.show_big_mac_index('South Korea', 'Won', 6520), "A Big Mac costs 6,520.00 Won in South Korea.")
        self.assertEqual(ex.show_big_mac_index('Taiwan', 'NTD', 72), "A Big Mac costs 72.00 NTD in Taiwan.")
    def test_07_is_positive(self):
        self.assertFalse(ex.is_positive(-1))
        self.assertTrue(ex.is_positive(0))
        self.assertTrue(ex.is_positive(1))
    def test_08_is_a_divisor(self):
        self.assertTrue(ex.is_a_divisor(1, 3))
        self.assertFalse(ex.is_a_divisor(2, 3))
        self.assertTrue(ex.is_a_divisor(3, 3))
        self.assertTrue(ex.is_a_divisor(1, 4))
        self.assertTrue(ex.is_a_divisor(2, 4))
        self.assertFalse(ex.is_a_divisor(3, 4))
        self.assertTrue(ex.is_a_divisor(4, 4))
    def test_09_are_vowels_contained(self):
        self.assertFalse(ex.are_vowels_contained('pythn'))
        self.assertFalse(ex.are_vowels_contained('ncnd'))
        self.assertFalse(ex.are_vowels_contained('rtclt'))
        self.assertTrue(ex.are_vowels_contained('python'))
        self.assertTrue(ex.are_vowels_contained('anaconda'))
        self.assertTrue(ex.are_vowels_contained('reticulate'))
    def test_10_are_all_vowels_contained(self):
        self.assertFalse(ex.are_all_vowels_contained('python'))
        self.assertFalse(ex.are_all_vowels_contained('anaconda'))
        self.assertFalse(ex.are_all_vowels_contained('reticulate'))
        self.assertTrue(ex.are_all_vowels_contained('anaconda and reticulate'))

suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentOne)
runner = unittest.TextTestRunner(verbosity=2)
if __name__ == '__main__':
    test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))