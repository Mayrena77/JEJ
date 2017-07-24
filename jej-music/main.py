import jinja2
import webapp2
import os
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/homepage.html')
        self.response.out.write(template.render())

class InputHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/input.html')
        self.response.out.write(template.render())

class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/results.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/input', InputHandler),
    ('/results', ResultsHandler)
], debug=True)
