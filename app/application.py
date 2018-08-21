# -*- coding: utf-8 -*-
import re
import logging
from views import views


logging.basicConfig(level=logging.INFO)


# map urls to functions
urls = [
    (r'^$', views.index),
    (r'hello/?$', views.hello),
    (r'hello/(.+)$', views.hello),
    (r'joy/?$', views.joy),
    (r'joy/(.+)$', views.joy)
]


def application(environ, start_response):
    logging.debug('PATH_INFO ' + environ.get('PATH_INFO', ''))
    logging.debug('QUERY_STRING ' + environ.get('QUERY_STRING', ''))
    logging.debug('SCRIPT_NAME ' + environ.get('SCRIPT_NAME', ''))

    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            environ['minimaluwsgi.url_args'] = match.groups()
            return callback(environ, start_response)
    return views.not_found(environ, start_response)
