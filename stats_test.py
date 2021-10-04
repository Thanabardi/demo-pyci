from unittest import TestCase
from stats import variance, stdev


class StatsTest(TestCase):

    def test_variance_typical_values(self):
        """variance of some typical values"""
        self.assertEqual(0.0, variance([10.0,10.0,10.0,10.0,10.0]))
        self.assertEqual(2.0, variance([1,2,3,4,5]))
        self.assertEqual(8.0, variance([10,2,8,4,6]))

    def test_variance_single_value_is_zero(self):
        """variance of a singleton list should be zero"""
        self.assertEqual(0.0, variance([0.0]))
        self.assertEqual(0.0, variance([99.999]))

    def test_variance_throws_exception(self):
        """variance of an empty list should raise an exception"""
        with self.assertRaises(ValueError):
            var = variance([])

    def test_stdev(self):
        """Test a stdev medthod."""
        self.assertEqual(2.0, stdev([1000000, 1000004]))

