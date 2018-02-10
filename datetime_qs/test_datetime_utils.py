import unittest
from datetime import datetime
from datetime_utils import overlap_days, Range


class OverlapDaysTestCase(unittest.TestCase):

    def test_adjacent(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        r2 = Range(start=datetime(2018, 1, 11), end=datetime(2018, 1, 30))
        self.assertEqual(overlap_days(r1, r2), 0)
        self.assertEqual(overlap_days(r2, r1), 0)

    def test_gap(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        r2 = Range(start=datetime(2018, 1, 20), end=datetime(2018, 1, 30))
        self.assertEqual(overlap_days(r1, r2), 0)
        self.assertEqual(overlap_days(r2, r1), 0)

    def test_overlap_same(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        self.assertEqual(overlap_days(r1, r1), 10)

    def test_overlap_boundary(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        r2 = Range(start=datetime(2018, 1, 10), end=datetime(2018, 1, 20))
        self.assertEqual(overlap_days(r1, r2), 1)
        self.assertEqual(overlap_days(r2, r1), 1)

    def test_some_overlap(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 10))
        r2 = Range(start=datetime(2018, 1, 5), end=datetime(2018, 1, 20))
        self.assertEqual(overlap_days(r1, r2), 6)
        self.assertEqual(overlap_days(r2, r1), 6)

    def test_contains(self):
        r1 = Range(start=datetime(2018, 1, 1), end=datetime(2018, 1, 20))
        r2 = Range(start=datetime(2018, 1, 5), end=datetime(2018, 1, 12))
        self.assertEqual(overlap_days(r1, r2), 8)
        self.assertEqual(overlap_days(r2, r1), 8)

if __name__ == '__main__':
    unittest.main()
