import webapp2
import jinja2
import os
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template("game.html")
        self.response.write(template.render())
    def post(self):
        template = the_jinja_env.get_template("game.html")
        self.response.write(template.render())
class EnterInfoHandler2(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template("tetris.html")
        self.response.write(template.render())
    def post(self):
        template = the_jinja_env.get_template("tetris.html")
        self.response.write(template.render())
class EnterInfoHandler3(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template("tictactoe.html")
        self.response.write(template.render())
    def post(self):
        template = the_jinja_env.get_template("tictactoe.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/tetris', EnterInfoHandler2),
    ('/tictactoe', EnterInfoHandler3)
], debug=True)
