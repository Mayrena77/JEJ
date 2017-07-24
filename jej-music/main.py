import jinja2
import webapp2
import os
from google.appengine.ext import ndb

    jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
