#run by going `python -m unittest test_rday`

import unittest
import datetime
from rday import fortnight_falls
from rday import weekly_falls

class rday_test_case(unittest.TestCase):

    def test_fortnight_falls(self):
      date1 = datetime.date(2018,01,07)
      date2 = datetime.date(2018,01,14)
      date3 = datetime.date(2018,01,21)
      self.assertFalse(
        fortnight_falls(date1, date2)
      )
      self.assertTrue(
        fortnight_falls(date1, date3)
      )

    def test_weekly_falls(self):
      date1 = datetime.date(2018,01,07)
      date2 = datetime.date(2018,01,14)
      date3 = datetime.date(2018,01,09)
      self.assertTrue(
        weekly_falls(date1, date2)
      )
      self.assertFalse(
        weekly_falls(date1, date3)
      )
