*********************
collective.prettydate
*********************

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

Fuzzy dates for Plone.

This package helps developers to solve some usability issues associated with the utilization of absolute date formating on sites used among different timezones.

When a date is printed as "01/02/2012" it could represent "February 1" or "January 2",
depending on the format used.
Also,
if the site is located on a different timezone,
it could take you to situations when today's date is printed as yesterday,
or tomorrow's date.

collective.prettydate represents a date on a relative format so it would be displayed as "4 hours ago",
"yesterday" or "last week",
which is easier to read and understand for most people.

This feature is really nice for news sites or sites with upcoming events.

Mostly Harmless
===============

.. image:: https://secure.travis-ci.org/collective/collective.prettydate.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/collective/collective.prettydate

.. image:: https://coveralls.io/repos/collective/collective.prettydate/badge.png?branch=master
    :alt: Coveralls badge
    :target: https://coveralls.io/r/collective/collective.prettydate

.. image:: https://pypip.in/d/collective.prettydate/badge.png
    :alt: Downloads
    :target: https://pypi.python.org/pypi/collective.prettydate/

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`opening a support ticket`: https://github.com/collective/collective.prettydate/issues

Don't Panic
===========

Installation
------------

To enable this product in a buildout-based installation:

1. Edit your buildout.cfg and add ``collective.prettydate`` to the list of
   eggs to install ::

    [buildout]
    ...
    eggs =
        collective.prettydate

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Usage
-----

This product provides a utility which will convert a DateTime object into a human readable text::

    from zope.component import getUtility
    from collective.prettydate.interfaces import IPrettyDate
    date_utility = getUtility(IPrettyDate)

At this point, you can use the ``date`` method to convert the DateTime object::

    from DateTime import DateTime
    today = DateTime()
    str_date = date_utility.date(today)

In previous example, ``str_date`` will be "now".

The 'date' method also allows 2 additional parameters: 'short' and 'asdays'
which will modify the output to be in short format ('h' instead of 'hours',
'd' instead of 'days', etc) and whole days (it will use 'today' instead of any
amount of seconds, minutes or hours for current day). They both default to
"False".

Timezones
^^^^^^^^^

If your server timezone is configured correctly,
and the DateTime object contains valid timezone info,
then the text output will reflect the correct time.
You do not need to convert date and time between different timezones.

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

DateTime 3.0
^^^^^^^^^^^^

This package is fully compatible with `DateTime 3.0`_ which provides a significantly smaller memory footprint.

.. _`DateTime 3.0`: http://pypi.python.org/pypi/DateTime

Not entirely unlike
===================

`collective.js.timeago`_
    An alternative, and probably clever way of dealing with fuzzy dates in Plone.
    This package registers the `timeago`_ JQuery plugin into the resource registry so convertion takes place client-side.

.. _`collective.js.timeago`: https://pypi.python.org/pypi/collective.js.timeago
.. _`timeago`: http://timeago.yarp.com/
