# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader, select_autoescape

HOST = 'localhost'
PORT = 8000

env = Environment(
    loader=PackageLoader('minimaluwsgi', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

from app.application import application

if __name__ == '__main__':
    # script is started directly from commandline
    try:
        # create a simple WSGI server and run the application
        from wsgiref import simple_server
        print "Running application - at http://%s:%i" % (HOST, PORT)
        srv = simple_server.make_server(HOST, PORT, application)
        srv.serve_forever()
    except ImportError:
        # wsgiref not installed, just output html to stdout
        for content in application({}, lambda status, headers: None):
            print content
