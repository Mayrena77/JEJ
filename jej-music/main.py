import jinja2
import webapp2
import os
from google.appengine.ext import ndb


class MainHandler(webapp2.RequestHandler):
    def get(self):

class InputHandler(webapp2.RequestHandler):
    def get(self):

class ResultsHandler(webapp2.RequestHandler):
    def get(self):



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/input', InputHandler),
    ('/results', ResultsHandler)
], debug=True)
