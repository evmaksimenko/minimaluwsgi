# -*- coding: utf-8 -*-
from app.application import application

HOST = 'localhost'
PORT = 8000


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
