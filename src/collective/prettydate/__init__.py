# -*- coding: utf-8 -*-

from DateTime import DateTime
from datetime import timedelta

from five import grok

from zope.component import getUtility
from zope.i18nmessageid import MessageFactory

from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot

from collective.prettydate.interfaces import IPrettyDate

_ = MessageFactory('collective.prettydate')


class PrettyDate(object):
    grok.implements(IPrettyDate)

    def normalize(self, seconds, denominator=1):
        return unicode((seconds + denominator / 2) / denominator)

    def date(self, date, short=False, asdays=False):
        now = DateTime()
        time = DateTime(date)

        if time > now:
            past = False
            diff = timedelta(time - now)

        else:
            past = True
            diff = timedelta(now - time)

        seconds = diff.seconds
        days = diff.days

        result = u''

        if short:
            if days == 0 and not asdays:
                if seconds < 10:
                    result = _(u'now')
                elif seconds < 60:
                    if past:
                        result = _(u"result_time_short_seconds_past",
                                   default=u"${time}s ago",
                                   mapping={u"time": self.normalize(seconds,
                                                                      1)})
                    else:
                        result = _(u"result_time_short_seconds_future",
                                   default=u"in ${time}s",
                                   mapping={u"time": self.normalize(seconds,
                                                                      1)})

                elif seconds < 3600:
                    if past:
                        result = _(u"result_time_short_minutes_past",
                                   default=u"${time}m ago",
                                   mapping={u"time": self.normalize(seconds,
                                                                      60)})
                    else:
                        result = _(u"result_time_short_minutes_future",
                                   default=u"in ${time}m",
                                   mapping={u"time": self.normalize(seconds,
                                                                      60)})
                else:
                    if past:
                        result = _(u"result_time_short_hours_past",
                                   default=u"${time}h ago",
                                   mapping={u"time": self.normalize(seconds,
                                                                      3600)})
                    else:
                        result = _(u"result_time_short_hours_future",
                                   default=u"in ${time}h",
                                   mapping={u"time": self.normalize(seconds,
                                                                      3600)})
            else:
                if days == 0:
                    result = _(u'today')
                elif days == 1:
                    result = past and _(u'yest') or _(u'tom')
                elif days < 7:
                    if past:
                        result = _(u"result_date_short_days_past",
                                   default=u"${time}d ago",
                                   mapping={u"time": self.normalize(days,
                                                                      1)})
                    else:
                        result = _(u"result_date_short_days_future",
                                   default=u"in ${time}d",
                                   mapping={u"time": self.normalize(days,
                                                                      1)})
                elif days < 31:
                    if past:
                        result = _(u"result_date_short_weeks_past",
                                   default=u"${time}w ago",
                                   mapping={u"time": self.normalize(days,
                                                                      7)})
                    else:
                        result = _(u"result_date_short_weeks_future",
                                   default=u"in ${time}w",
                                   mapping={u"time": self.normalize(days,
                                                                      7)})
                elif days < 365:
                    if past:
                        result = _(u"result_date_short_months_past",
                                   default=u"${time}mo ago",
                                   mapping={u"time": self.normalize(days,
                                                                      30)})
                    else:
                        result = _(u"result_date_short_months_future",
                                   default=u"in ${time}mo",
                                   mapping={u"time": self.normalize(days,
                                                                      30)})
                else:
                    if past:
                        result = _(u"result_date_short_years_past",
                                   default=u"${time}y ago",
                                   mapping={u"time": self.normalize(days,
                                                                      365)})
                    else:
                        result = _(u"result_date_short_years_future",
                                   default=u"in ${time}y",
                                   mapping={u"time": self.normalize(days,
                                                                      365)})
        else:
            if days == 0 and not asdays:
                if   seconds < 10:
                    result = _(u'now')
                elif seconds < 60:
                    if past:
                        result = _(u"result_time_long_seconds_past",
                                   default=u"${time} seconds ago",
                                   mapping={u"time": self.normalize(seconds,
                                                                      1)})
                    else:
                        result = _(u"result_time_long_seconds_future",
                                   default=u"in ${time} seconds",
                                   mapping={u"time": self.normalize(seconds,
                                                                      1)})
                elif seconds < 120:
                    result = past and _(u'a minute ago') or _(u'in a minute')
                elif seconds < 3600:
                    if past:
                        result = _(u"result_time_long_minutes_past",
                                   default=u"${time} minutes ago",
                                   mapping={u"time": self.normalize(seconds,
                                                                      60)})
                    else:
                        result = _(u"result_time_long_minutes_future",
                                   default=u"in ${time} minutes",
                                   mapping={u"time": self.normalize(seconds,
                                                                      60)})
                elif seconds < 7200:
                    result = past and _(u'an hour ago') or _(u'in an hour')
                else:
                    if past:
                        result = _(u"result_time_long_hours_past",
                                   default=u"${time} hours ago",
                                   mapping={u"time": self.normalize(seconds,
                                                                      3600)})
                    else:
                        result = _(u"result_time_long_hours_future",
                                   default=u"in ${time} hours",
                                   mapping={u"time": self.normalize(seconds,
                                                                      3600)})
            else:
                if days == 0:
                    result = _(u'today')
                elif days == 1:
                    result = past and _(u'yesterday') or _(u'tomorrow')
                elif days == 2:
                    result = past and _(u'day before') or _(u'day after')
                elif days < 7:
                    if past:
                        result = _(u"result_date_long_days_past",
                                   default=u"${time} days ago",
                                   mapping={u"time": self.normalize(days,
                                                                      1)})
                    else:
                        result = _(u"result_date_long_days_future",
                                   default=u"in ${time} days",
                                   mapping={u"time": self.normalize(days,
                                                                      1)})
                elif days < 14:
                    result = past and _(u'last week') or _(u'next week')
                elif days < 31:
                    if past:
                        result = _(u"result_date_long_weeks_past",
                                   default=u"${time} weeks ago",
                                   mapping={u"time": self.normalize(days,
                                                                      7)})
                    else:
                        result = _(u"result_date_long_weeks_future",
                                   default=u"in ${time} weeks",
                                   mapping={u"time": self.normalize(days,
                                                                      7)})
                elif days < 61:
                    result = past and _(u'last month') or _(u'next month')
                elif days < 365:
                    if past:
                        result = _(u"result_date_long_months_past",
                                   default=u"${time} months ago",
                                   mapping={u"time": self.normalize(days,
                                                                      30)})
                    else:
                        result = _(u"result_date_long_months_future",
                                   default=u"in ${time} months",
                                   mapping={u"time": self.normalize(days,
                                                                      30)})
                elif days < 730:
                    result = past and _(u'last year') or _(u'next year')
                else:
                    if past:
                        result = _(u"result_date_long_years_past",
                                   default=u"${time} years ago",
                                   mapping={u"time": self.normalize(days,
                                                                      365)})
                    else:
                        result = _(u"result_date_long_years_future",
                                   default=u"in ${time} years",
                                   mapping={u"time": self.normalize(days,
                                                                      365)})

        return result


class TestView(grok.View):
    grok.context(IPloneSiteRoot)
    grok.name("test-view")

    def render(self):

        la = getUtility(IPrettyDate).date(DateTime('2012/01/17 00:00:00'))

        return la


grok.global_utility(PrettyDate(),
                    provides=IPrettyDate,
                    direct=True)
