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

This product is based on http://pypi.python.org/pypi/py-pretty
It is intended to be used by developers.

Installation
------------

This product does not require installation. Just add it as a dependency
for your custom product or list it in the 'eggs' section, if using buildout.

Usage
-----

This product provides a utility which will convert a DateTime object into
a human readable text.

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
amount of seconds, minutes or hours for current day).
They both default to "False".

Output examples
---------------
 * '4 hours ago'
 * '4h ago' (short format)
 * 'in 28 minutes'
 * 'in 6 months'
 * 'today'
 * 'last week'
 * 'yesterday'
 * 'last year'
