# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf import settings

from .defaults import DEFAULT_REQUEST_ID_HEADER_NAME

REQUEST_ID_HEADER = getattr(settings, 'REQUEST_ID_HEADER', DEFAULT_REQUEST_ID_HEADER_NAME)

REQUEST_ID_AUOTGEN = getattr(
    settings, 'REQUEST_ID_AUTOGEN', DEFAULT_REQUEST_ID_AUTOGEN)

"""
Default header name as defined in
`heroku request-id <https://devcenter.heroku.com/articles/http-request-id>`_
"""
