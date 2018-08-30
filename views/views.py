# -*- coding: utf-8 -*-
from cgi import escape
from jinja2 import Environment, PackageLoader, select_autoescape
from minimaluwsgi import env

response_OK = ('200 OK', [('Content-Type', 'text/html')])
response_NOT_FOUND = ('404 NOT FOUND', [('Content-Type', 'text/html')])


def hello(environ, start_response):
    # get the name from the url if it was specified there.
    args = environ['minimaluwsgi.url_args']
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    start_response(*response_OK)
    return ['Hello %(subject)s' % {'subject': subject}]


def joy(environ, start_response):
    template = env.get_template('joy.html')
    args = environ['minimaluwsgi.url_args']
    if args:
        passed_name = escape(args[0])
    else:
        passed_name = u'World'
    args2 = environ.get('QUERY_STRING', '')
    passed_args = args2 if args2 else u'Ничего!'
    start_response(*response_OK)
    r_val = {'pname': passed_name, 'pargs': passed_args}
    return template.render(r_val).encode('utf-8')


def index(environ, start_response):
    """This function will be mounted on "/"."""
    start_response(*response_OK)
    return ['minimaluwsgi Application']


def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response(*response_NOT_FOUND)
    return ['Not Found']
