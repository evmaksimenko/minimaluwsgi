# -*- coding: utf-8 -*-
from cgi import escape
from jinja2 import Environment, PackageLoader, select_autoescape, Template


def hello(environ, start_response):
    # get the name from the url if it was specified there.
    args = environ['minimaluwsgi.url_args']
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['Hello %(subject)s' % {'subject': subject}]


def joy(environ, start_response):
    env = Environment(
        loader=PackageLoader('minimaluwsgi', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('joy.html')
    args = environ['minimaluwsgi.url_args']
    if args:
        passed_name = escape(args[0])
    else:
        passed_name = u'World'
    args2 = environ.get('QUERY_STRING', '')
    passed_args = args2 if args2 else u'Ничего!'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return template.render(pname=passed_name, pargs=passed_args).encode('utf-8')


def index(environ, start_response):
    """This function will be mounted on "/"."""
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['minimaluwsgi Application']


def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']
