# -*- coding: utf-8 -*-

from zope.interface import Interface


class IPrettyDate(Interface):
    """
    """

    def date(date):
        """
        Given a datetime it will return a formatted output like
        "an hour ago", "tomorrow", "a week ago", etc
        """
