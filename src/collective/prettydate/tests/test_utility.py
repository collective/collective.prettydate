# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.component import getUtility
from collective.prettydate.interfaces import IPrettyDate

from collective.prettydate.testing import INTEGRATION_TESTING

from DateTime import DateTime


class UtilityTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.utility = getUtility(IPrettyDate)

        self.second = (DateTime('2012/12/21 00:00:01') -
                       DateTime('2012/12/21 00:00:00'))
        self.minute = (DateTime('2012/12/21 00:01:00') -
                       DateTime('2012/12/21 00:00:00'))
        self.hour = (DateTime('2012/12/21 01:00:00') -
                     DateTime('2012/12/21 00:00:00'))
        self.day = (DateTime('2012/12/21 00:00:00') -
                       DateTime('2012/12/20 00:00:00'))
        self.week = self.day * 7
        self.month = self.day * 31
        self.year = self.day * 365

    def test_long_past_time(self):
        # Let's ask for a date up to 9 seconds ago, we should get "now"
        for i in range(0, 10):
            now = DateTime()
            result = self.utility.date(now - (self.second * i))
            self.assertEqual(self.portal.translate(result), u'now')

        # From 10 seconds and up to 1 minute, we should get the number of
        # seconds ago
        for i in range(10, 60):
            now = DateTime()
            result = self.utility.date(now - (self.second * i))
            self.assertEqual(self.portal.translate(result), u'%s seconds ago' % i)

        # From 1 minute and up to 2 minutes, we get "a minute ago"
        now = DateTime()
        result = self.utility.date(now - (self.minute))
        self.assertEqual(self.portal.translate(result), u'a minute ago')
        result = self.utility.date(now - (self.minute * 2 - self.second))
        self.assertEqual(self.portal.translate(result), u'a minute ago')

        # From 3 minutes and up to an hour, we get the number of minutes ago
        for i in range(2, 60):
            now = DateTime()
            result = self.utility.date(now - (self.minute * i))
            self.assertEqual(self.portal.translate(result), u'%s minutes ago' % i)

        # From 1 hour and up to 2 hours, we get "an hour ago"
        now = DateTime()
        result = self.utility.date(now - (self.hour))
        self.assertEqual(self.portal.translate(result), u'an hour ago')
        result = self.utility.date(now - (self.hour * 2 - self.second))
        self.assertEqual(self.portal.translate(result), u'an hour ago')

        # From 3 hours and up to a day, we get the number of hours ago
        for i in range(3, 24):
            now = DateTime()
            result = self.utility.date(now - (self.hour * i))
            self.assertEqual(self.portal.translate(result), u'%s hours ago' % i)

    def test_long_past_date(self):
        # Let's ask for yesterday
        now = DateTime()
        result = self.utility.date(now - (self.day))
        self.assertEqual(self.portal.translate(result), u'yesterday')

        # And for the day before
        now = DateTime()
        result = self.utility.date(now - (self.day * 3 - self.second))
        self.assertEqual(self.portal.translate(result), u'day before')

        #Now from 3 to up to 6 days, we get how many days ago
        for i in range(3, 7):
            now = DateTime()
            result = self.utility.date(now - (self.day * i))
            self.assertEqual(self.portal.translate(result), u'%s days ago' % i)

        #Let's check for last week
        now = DateTime()
        result = self.utility.date(now - (self.week))
        self.assertEqual(self.portal.translate(result), u'last week')
        now = DateTime()
        result = self.utility.date(now - (self.week * 2 - self.second))
        self.assertEqual(self.portal.translate(result), u'last week')

        # From 2 and up to 4 weeks we get the number of weeks ago
        for i in range(2, 5):
            now = DateTime()
            result = self.utility.date(now - (self.week * i))
            self.assertEqual(self.portal.translate(result), u'%s weeks ago' % i)

        #Let's check for last month
        now = DateTime()
        result = self.utility.date(now - (self.month))
        self.assertEqual(self.portal.translate(result), u'last month')
        now = DateTime()
        result = self.utility.date(now - (self.month * 2 - self.day * 2))
        self.assertEqual(self.portal.translate(result), u'last month')

        # From 2 and up to 12 months we get the number of months ago
        for i in range(2, 12):
            now = DateTime()
            result = self.utility.date(now - (self.month * i))
            self.assertEqual(self.portal.translate(result), u'%s months ago' % i)

        #Let's check for last year
        now = DateTime()
        result = self.utility.date(now - (self.year))
        self.assertEqual(self.portal.translate(result), u'last year')
        now = DateTime()
        result = self.utility.date(now - (self.year * 2 - self.second))
        self.assertEqual(self.portal.translate(result), u'last year')

        # Over 2 years, we get the number of years ago, let's test it up to
        # 20 years
        for i in range(2, 20):
            now = DateTime()
            result = self.utility.date(now - (self.year * i))
            self.assertEqual(self.portal.translate(result), u'%s years ago' % i)

    def test_long_future_time(self):
        # Let's ask for a date up to 10 seconds in the future, we should get
        # "now"
        for i in range(0, 11):
            now = DateTime()
            result = self.utility.date(now + (self.second * i))
            self.assertEqual(self.portal.translate(result), u'now')

        # From 12 seconds and up to 1 minute, we should get the number of
        # seconds it takes
        # XXX There's a slight mismatch in the calculus, and is a bit off for
        #     future seconds, so we are going to make a little adjustement
        #     and hope for the best :P
        for i in range(11, 60):
            now = DateTime()
            result = self.utility.date(now + (self.second * (i + 1)))
            self.assertEqual(self.portal.translate(result), u'in %s seconds' % i)

        # From 1 minute and up to 2 minutes, we get "in a minute"
        now = DateTime()
        result = self.utility.date(now + (self.minute + self.second))
        self.assertEqual(self.portal.translate(result), u'in a minute')
        result = self.utility.date(now + (self.minute * 2 - self.second))
        self.assertEqual(self.portal.translate(result), u'in a minute')

        # From 3 minutes and up to an hour, we get the number of minutes to go
        for i in range(2, 60):
            now = DateTime()
            result = self.utility.date(now + ((self.minute + self.second / 2.0) * i))
            self.assertEqual(self.portal.translate(result), u'in %s minutes' % i)

        # From 1 hour and up to 2 hours, we get "in an hour"
        now = DateTime()
        result = self.utility.date(now + (self.hour + self.second))
        self.assertEqual(self.portal.translate(result), u'in an hour')
        result = self.utility.date(now + (self.hour * 2 - self.second))
        self.assertEqual(self.portal.translate(result), u'in an hour')

        # From 3 hours and up to a day, we get the number of hours to go
        for i in range(3, 24):
            now = DateTime()
            result = self.utility.date(now + (self.hour * i))
            self.assertEqual(self.portal.translate(result), u'in %s hours' % i)

    def test_long_future_date(self):
        # Let's ask for tomorrow
        now = DateTime()
        result = self.utility.date(now + (self.day + self.second))
        self.assertEqual(self.portal.translate(result), u'tomorrow')

        # And for the day after
        now = DateTime()
        result = self.utility.date(now + (self.day * 3 - self.hour))
        self.assertEqual(self.portal.translate(result), u'day after')

        #Now from 3 to up to 6 days, we get how many days to go
        for i in range(3, 7):
            now = DateTime()
            result = self.utility.date(now + ((self.day + self.second) * i))
            self.assertEqual(self.portal.translate(result), u'in %s days' % i)

        #Let's check for next week
        now = DateTime()
        result = self.utility.date(now + (self.week + self.second))
        self.assertEqual(self.portal.translate(result), u'next week')
        now = DateTime()
        result = self.utility.date(now + (self.week * 2 - self.second))
        self.assertEqual(self.portal.translate(result), u'next week')

        # From 2 and up to 4 weeks we get the number of weeks to go
        for i in range(2, 5):
            now = DateTime()
            result = self.utility.date(now + ((self.week + self.second) * i))
            self.assertEqual(self.portal.translate(result), u'in %s weeks' % i)

        #Let's check for next month
        now = DateTime()
        result = self.utility.date(now + (self.month + self.second))
        self.assertEqual(self.portal.translate(result), u'next month')
        now = DateTime()
        result = self.utility.date(now + (self.month * 2 - self.day))
        self.assertEqual(self.portal.translate(result), u'next month')

        # From 2 and up to 12 months we get the number of months to go
        for i in range(2, 12):
            now = DateTime()
            result = self.utility.date(now + ((self.month + self.second) * i))
            self.assertEqual(self.portal.translate(result), u'in %s months' % i)

        #Let's check for next year
        now = DateTime()
        result = self.utility.date(now + (self.year + self.second))
        self.assertEqual(self.portal.translate(result), u'next year')
        now = DateTime()
        result = self.utility.date(now + (self.year * 2 - self.second))
        self.assertEqual(self.portal.translate(result), u'next year')

        # Over 2 years, we get the number of years to go, let's test it up to
        # 20 years
        for i in range(2, 20):
            now = DateTime()
            result = self.utility.date(now + ((self.year + self.second) * i))
            self.assertEqual(self.portal.translate(result), u'in %s years' % i)

    def test_short_past_time(self):
        # Let's ask for a date up to 9 seconds ago, we should get "now"
        for i in range(0, 10):
            now = DateTime()
            result = self.utility.date(now - (self.second * i), short=True)
            self.assertEqual(self.portal.translate(result), u'now')

        # From 10 seconds and up to 1 minute, we should get the number of
        # seconds ago
        for i in range(10, 60):
            now = DateTime()
            result = self.utility.date(now - (self.second * i), short=True)
            self.assertEqual(self.portal.translate(result), u'%ss ago' % i)

        # From 1 minute and up to an hour, we get the number of minutes ago
        for i in range(1, 60):
            now = DateTime()
            result = self.utility.date(now - (self.minute * i), short=True)
            self.assertEqual(self.portal.translate(result), u'%sm ago' % i)

        # From 1 hour and up to a day, we get the number of hours ago
        for i in range(1, 24):
            now = DateTime()
            result = self.utility.date(now - (self.hour * i), short=True)
            self.assertEqual(self.portal.translate(result), u'%sh ago' % i)

    def test_short_past_date(self):
        # Let's ask for yesterday
        now = DateTime()
        result = self.utility.date(now - (self.day), short=True)
        self.assertEqual(self.portal.translate(result), u'yest')

        # And for the day before
        now = DateTime()
        result = self.utility.date(now - (self.day * 3 - self.second), short=True)
        self.assertEqual(self.portal.translate(result), u'2d ago')

        #Now from 3 to up to 6 days, we get how many days ago
        for i in range(3, 7):
            now = DateTime()
            result = self.utility.date(now - (self.day * i), short=True)
            self.assertEqual(self.portal.translate(result), u'%sd ago' % i)

        # From 1 and up to 4 weeks we get the number of weeks ago
        for i in range(1, 5):
            now = DateTime()
            result = self.utility.date(now - (self.week * i), short=True)
            self.assertEqual(self.portal.translate(result), u'%sw ago' % i)

        # From 1 and up to 12 months we get the number of months ago
        for i in range(1, 12):
            now = DateTime()
            result = self.utility.date(now - (self.month * i), short=True)
            self.assertEqual(self.portal.translate(result), u'%smo ago' % i)

        # Over 1 year, we get the number of years ago, let's test it up to
        # 20 years
        for i in range(1, 20):
            now = DateTime()
            result = self.utility.date(now - (self.year * i), short=True)
            self.assertEqual(self.portal.translate(result), u'%sy ago' % i)

    def test_short_future_time(self):
        # Let's ask for a date up to 10 seconds in the future, we should get
        # "now"
        for i in range(0, 11):
            now = DateTime()
            result = self.utility.date(now + (self.second * i), short=True)
            self.assertEqual(self.portal.translate(result), u'now')

        # From 12 seconds and up to 1 minute, we should get the number of
        # seconds it takes
        # XXX There's a slight mismatch in the calculus, and is a bit off for
        #     future seconds, so we are going to make a little adjustement
        #     and hope for the best :P
        for i in range(11, 60):
            now = DateTime()
            result = self.utility.date(now + (self.second * (i + 1)), short=True)
            self.assertEqual(self.portal.translate(result), u'in %ss' % i)

        # From 1 minute and up to an hour, we get the number of minutes to go
        for i in range(1, 60):
            now = DateTime()
            result = self.utility.date(now + ((self.minute + self.second / 2.0) * i), short=True)
            self.assertEqual(self.portal.translate(result), u'in %sm' % i)

        # From 1 hour and up to a day, we get the number of hours to go
        for i in range(1, 24):
            now = DateTime()
            result = self.utility.date(now + ((self.hour + self.second) * i), short=True)
            self.assertEqual(self.portal.translate(result), u'in %sh' % i)

    def test_short_future_date(self):
        # Let's ask for tomorrow
        now = DateTime()
        result = self.utility.date(now + (self.day + self.second), short=True)
        self.assertEqual(self.portal.translate(result), u'tom')

        # And for the day after
        now = DateTime()
        result = self.utility.date(now + (self.day * 3 - self.hour), short=True)
        self.assertEqual(self.portal.translate(result), u'in 2d')

        #Now from 3 to up to 6 days, we get how many days to go
        for i in range(3, 7):
            now = DateTime()
            result = self.utility.date(now + ((self.day + self.second) * i), short=True)
            self.assertEqual(self.portal.translate(result), u'in %sd' % i)

        # From 1 and up to 4 weeks we get the number of weeks to go
        for i in range(1, 5):
            now = DateTime()
            result = self.utility.date(now + ((self.week + self.second) * i), short=True)
            self.assertEqual(self.portal.translate(result), u'in %sw' % i)

        # From 1 and up to 12 months we get the number of months to go
        for i in range(1, 12):
            now = DateTime()
            result = self.utility.date(now + ((self.month + self.second) * i), short=True)
            self.assertEqual(self.portal.translate(result), u'in %smo' % i)

        # Over 1 years, we get the number of years to go, let's test it up to
        # 20 years
        for i in range(1, 20):
            now = DateTime()
            result = self.utility.date(now + ((self.year + self.second) * i), short=True)
            self.assertEqual(self.portal.translate(result), u'in %sy' % i)

    def test_asdays(self):
        # For less than a day, it will always return today, and not hours.
        # for more than one day, it just behaves as the regular date. which
        # is already tested

        # let's repeat the time test, but always get "today"
        for i in range(0, 60):
            now = DateTime()
            result = self.utility.date(now - (self.second * i), asdays=True)
            self.assertEqual(self.portal.translate(result), u'today')

        for i in range(1, 60):
            now = DateTime()
            result = self.utility.date(now - (self.minute * i), asdays=True)
            self.assertEqual(self.portal.translate(result), u'today')

        for i in range(1, 24):
            now = DateTime()
            result = self.utility.date(now - (self.hour * i), asdays=True)
            self.assertEqual(self.portal.translate(result), u'today')

        # The same goes for the future
        for i in range(0, 60):
            now = DateTime()
            result = self.utility.date(now + (self.second * i), asdays=True)
            self.assertEqual(self.portal.translate(result), u'today')

        for i in range(1, 60):
            now = DateTime()
            result = self.utility.date(now + (self.minute * i), asdays=True)
            self.assertEqual(self.portal.translate(result), u'today')

        for i in range(1, 24):
            now = DateTime()
            result = self.utility.date(now + (self.hour * i), asdays=True)
            self.assertEqual(self.portal.translate(result), u'today')


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
