# -*- coding: utf-8 -*-
from cgi import escape
from minimaluwsgi import env

responses = {
    200: ('200 OK', [('Content-Type', 'text/html')]),
    404: ('404 NOT FOUND', [('Content-Type', 'text/html')])
}


def hello(environ, start_response):
    # get the name from the url if it was specified there.
    args = environ['minimaluwsgi.url_args']
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    start_response(*responses[200])
    return ['Hello %(subject)s' % {'subject': subject}]


def joy(environ, start_response):
    template = env.get_template('joy.html')
    args = environ['minimaluwsgi.url_args']
    if args:
        try:
            passed_name = escape(args[0])
        except IndexError:
            passed_name = u'Strange World!'
    else:
        passed_name = u'World'
    args2 = environ.get('QUERY_STRING', '')
    passed_args = args2 if args2 else u'Ничего!'
    start_response(*responses[200])
    r_val = {'pname': passed_name, 'pargs': passed_args}
    return template.render(r_val).encode('utf-8')


def index(environ, start_response):
    """This function will be mounted on "/"."""
    start_response(*responses[200])
    return ['minimaluwsgi Application']


def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response(*responses[404])
    return ['Not Found']
