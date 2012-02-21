*********************
collective.prettydate
*********************

.. contents:: Table of Contents

Overview
--------

This simple package formats dates in a pretty, human readable format.

Requirements
------------

* Plone >= 4.1 (http://plone.org/products/plone)
* five.grok >= 1.2 (http://pypi.python.org/pypi/five.grok)

Introduction
------------

collective.prettydate is a package that helps developers to solve some
usability issues associated with the utilization of absolute date formating on
sites used among different timezones.

When a date is printed as "01/02/2012" it could represent February 1 or
January 2, depending on the format used. Also, if the site is located on a
different timezone, it could take you to situations when today's date is
printed as yesterday, or tomorrow's date.

collective.prettydate represents dates on a relative format so it would be
printed as "last month" or "2 months ago", which is easier to read and
understand for most people.

collective.prettydate is specially well suited for sites that produce a lot of
content, like breaking news.

Usage
-----

This product provides a utility which will convert a DateTime object into a
human readable text.

::

    from zope.component import getUtility
    from collective.prettydate.interfaces import IPrettyDate
    date_utility = getUtility(IPrettyDate)

At this point, you can use the 'date' method to convert the DateTime object

::

    from DateTime import DateTime
    today = DateTime()
    str_date = date_utility.date(today)

in previous example, 'str_date' will be "now"

'date' method also allows 2 additional parameters: 'short' and 'asdays' which
will modify the output to be in short format ('h' instead of 'hours', 'd'
instead of 'days', etc) and whole days (it will use 'today' instead of any
amount of seconds, minutes or hours for current day). They both default to
"False".

Timezones
^^^^^^^^^

If your server timezone is configured correctly, and the DateTime object
contains valid timezone info, then the text output will reflect the correct
time. You do not need to convert date and time between different timezones.

Output examples
^^^^^^^^^^^^^^^

* '4 hours ago'
* '4h ago' (short format)
* 'in 28 minutes'
* 'in 6 months'
* 'today'
* 'last week'
* 'yesterday'
* 'last year'

