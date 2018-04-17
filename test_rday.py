#run by going `python -m unittest test_rday`

import unittest
import datetime
from rday import (
  fortnight_falls, 
  weekly_falls, 
  when_is_recycling_pickup)

class rday_test_case(unittest.TestCase):

    def test_fortnight_falls(self):
      date1 = datetime.date(2018,1,7)
      date2 = datetime.date(2018,1,14)
      date3 = datetime.date(2018,1,21)
      self.assertFalse(
        fortnight_falls(date1, date2)
      )
      self.assertTrue(
        fortnight_falls(date1, date3)
      )

    def test_weekly_falls(self):
      date1 = datetime.date(2018,1,7)
      date2 = datetime.date(2018,1,14)
      date3 = datetime.date(2018,1,9)
      self.assertTrue(
        weekly_falls(date1, date2)
      )
      self.assertFalse(
        weekly_falls(date1, date3)
      )

    def test_when_is_recycling_pickup(self):
      last_known_pickup_date = datetime.date(2018,1,7)

      two_days_before_a_garbage_only_date = datetime.date(2018,1,12)
      a_day_before_a_garbage_only_date = datetime.date(2018,1,13)
      a_garbage_only_date = datetime.date(2018,1,14)
      a_day_after_a_garbage_only_date = datetime.date(2018,1,15)
      two_days_after_a_garbage_only_date = datetime.date(2018,1,16)

      two_days_before_a_garbage_recycling_date = datetime.date(2018,1,19)
      a_day_before_a_garbage_recycling_date = datetime.date(2018,1,20)
      a_garbage_and_recycling_date = datetime.date(2018,1,21) 
      a_day_after_a_garbage_recycling_date = datetime.date(2018,1,22)
      two_days_after_a_garbage_recycling_date = datetime.date(2018,1,23)

      self.assertEqual(
        when_is_recycling_pickup(
          last_known_pickup_date, 
          two_days_before_a_garbage_only_date
        ),
        "Not this coming collection day"
      )

      self.assertEqual(
        when_is_recycling_pickup(
          last_known_pickup_date, 
          a_day_before_a_garbage_only_date
        ),
        "Not tomorrow"
      )

      self.assertEqual(
        when_is_recycling_pickup(
          last_known_pickup_date, 
          a_garbage_only_date
        ),
        "Not today"
      )

      self.assertEqual(
        when_is_recycling_pickup(
          last_known_pickup_date, 
          a_day_after_a_garbage_only_date
        ),
        "This coming collection day"
      )
      
      self.assertEqual(
        when_is_recycling_pickup(
          last_known_pickup_date, 
          two_days_after_a_garbage_only_date
        ),
        "This coming collection day"
      )

      self.assertEqual(
        when_is_recycling_pickup(
          last_known_pickup_date, 
          two_days_before_a_garbage_recycling_date
        ),
        "This coming collection day"
      )
      
      self.assertEqual(
        when_is_recycling_pickup(
          last_known_pickup_date, 
          a_day_before_a_garbage_recycling_date
        ),
        "Tomorrow"
      )
      
      self.assertEqual(
        when_is_recycling_pickup(
          last_known_pickup_date, 
          a_garbage_and_recycling_date
        ),
        "Today"
      )
      
      self.assertEqual(
        when_is_recycling_pickup(
          last_known_pickup_date, 
          a_day_after_a_garbage_recycling_date
        ),
        "Not this coming collection day"
      )

      self.assertEqual(
        when_is_recycling_pickup(
          last_known_pickup_date, 
          two_days_after_a_garbage_recycling_date
        ),
        "Not this coming collection day"
      )
