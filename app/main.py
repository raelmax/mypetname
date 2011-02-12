# -*- coding: utf-8 -*-
import cgi
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from myconf import TEMPLATE_FOLDER

from app.models import Nome

class MainPage(webapp.RequestHandler):
    path = os.path.join(TEMPLATE_FOLDER, 'index.html')
    def get(self):
        self.response.out.write(template.render(self.path, locals()))

    def post(self):
        self.response.out.write(template.render(self.path, locals()))

application = webapp.WSGIApplication(
                                    [('/', MainPage)],debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
