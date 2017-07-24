import jinja2
import webapp2
import os
from google.appengine.ext import ndb


class MainHandler(webapp2.RequestHandler):
    def get(self):
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
