====================
django-flashbriefing
====================

Amazon `Alexa Flash Briefings <https://developer.amazon.com/alexa-skills-kit/flash-briefing>`_ for Django

.. image:: https://circleci.com/gh/istrategylabs/django-flashbriefing/tree/master.svg?style=shield
    :target: https://circleci.com/gh/istrategylabs/django-flashbriefing/tree/master

flashbriefing provides models for feeds and feed items, a view to render the
JSON feed, and default admin configuration.


Installation
------------

It's on `PyPI <https://pypi.python.org/pypi/django-flashbriefing>`_::

    pipenv install django-flashbriefing

Add to *INSTALLED_APPS*::

    INSTALLED_APPS = (
        ...
        'flashbriefing',
        ...
    )

Add a route to *urls.py*::

    urlpatterns = [
        ...
        url(r'^briefings/', include('flashbriefing.urls')),
        ...
    ]

Run migrations::

    python manage.py migrate


Feed URL
--------

The feed URL can found by clicking *View on Site* on the Django admin Feed edit
page or by accessing :code:`get_absolute_url()` on a feed instance. This is the
URL that will need to be registered with Amazon.


Registering with Amazon
-----------------------

1. Login to the `Amazon Developer Console <https://developer.amazon.com>`_.
2. Click *Alexa* in the main navigation.
3. Under *Alexa Skills Kit*, click *Get Started*.
4. Under *Skill Type*, select *Flash Briefing Skill API*.
5. Under *Configuration*, click *Add new feed* and add information about the feed, including the URL of the feed from the application.
