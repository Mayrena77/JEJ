import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import users

jinja_environment = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Song(ndb.Model):

    genre = ndb.StringProperty()
    artist = ndb.StringProperty()
    song_name = ndb.StringProperty()

class CssiUser(ndb.Model):
    first_name = ndb.StringProperty()
    pass

class MainHandler(webapp2.RequestHandler):
  def get(self):

    self.response.write(''' <head>
    <link rel="stylesheet" href="resources/login.css">
    <link rel="shortcut icon" href="/JEJ_logo_icon.ico" />  </head>
    <title> JEJ Music </title> <body>''')
    template = jinja_environment.get_template('templates/input.html')
    user = users.get_current_user()

    if user:
      email_address = user.nickname()
      cssi_user = CssiUser.get_by_id(user.user_id())
      signout_link_html = '<div class="signout"> <a href="%s">sign out</a> </div>' % (
          users.create_logout_url('/'))
      self.response.write('''
            <div class="greeting"> Hello %s! <br> %s <br> </div>''' % (
              email_address,
              signout_link_html))
      self.response.out.write(template.render())


    else:
      self.response.write('''
        <a href="%s"> <img class="loginImage" src = "JEJ_logo_icon.ico"/> </a>
        <img class"words" src = "JEJ_words.jpg"/>
        </body>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"> </script>
        <script src="function/login.js"></script>''' % (
          users.create_login_url('/name')))


  def post(self):
    template = jinja_environment.get_template('templates/input.html')
    user = users.get_current_user()
    if not user:
      self.error(500)
      return
    cssi_user = CssiUser(
        id=user.user_id())
    cssi_user.put()
    self.response.out.write(template.render())
    self.response.write('Thanks for signing up!')

class NameHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/name.html')
        self.response.write(template.render())
    def post(self):
        user_Id = CssiUser(
        first_name = self.request.get('first_name')
        )
        user_Id.put()
        self.redirect('/')



class InputHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/input.html')
        self.response.out.write(template.render())


class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/results.html')
        self.response.write(template.render( { 'genre': self.request.get('genre'),
        'Name of Artist': self.request.get('artist'),
        'Name of Song': self.request.get('song_name')}))
        user_Input = Song(
        genre = self.request.get('genre'),
        song_name = self.request.get('song_name'),
        artist = self.request.get('artist'),
        )
        user_Input.put()

        """query = user_Input.query()
        query = user_Input.genre
        matches = query
        template = jinja_environment.get_template('templates/results.html')
        self.response.write(template.render({'match': matches}))"""

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/About_Us.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultsHandler),
    ('/about', AboutUsHandler),
    ('/name', NameHandler)
], debug=True)
