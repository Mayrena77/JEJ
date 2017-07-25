import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import users

jinja_environment = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class CssiUser(ndb.Model):
    pass

class MainHandler(webapp2.RequestHandler):
  def get(self):

    self.response.write(''' <head>
      <link rel="stylesheet" href="/Users/demouser/JEJ/jej-music/resources/logincss.css">
       <link rel="shortcut icon" href="/JEJ_logo_icon.ico" />  </head> ''')
    template = jinja_environment.get_template('templates/homepage.html')
    user = users.get_current_user()

    if user:
      email_address = user.nickname()
      cssi_user = CssiUser.get_by_id(user.user_id())
      signout_link_html = '<a href="%s">sign out</a>' % (
          users.create_logout_url('/'))
      self.response.write('''
            Welcome %s! <br> %s <br>''' % (
              email_address,
              signout_link_html))
      self.response.out.write(template.render())


    else:
      self.response.write('''
        <a href="%s"> <img src = "JEJ_logo_words.jpg"/> </a>''' % (
          users.create_login_url('/home')))


  def post(self):
    template = jinja_environment.get_template('templates/homepage.html')
    user = users.get_current_user()
    if not user:
      self.error(500)
      return
    cssi_user = CssiUser(
        id=user.user_id())
    cssi_user.put()
    self.response.out.write(template.render())
    self.response.write('Thanks for signing up!')

class HomepageHandler(webapp2.RequestHandler):
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
    ('/home', HomepageHandler),
    ('/input', InputHandler),
    ('/results', ResultsHandler)
], debug=True)
