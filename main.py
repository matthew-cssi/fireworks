import jinja2
import os
import webapp2

from google.appengine.ext import ndb

class Counter(ndb.Model):
    count = ndb.IntegerProperty()

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/main.html')
        self.response.write(template.render())

class CountHandler(webapp2.RequestHandler):
    def post(self):
        counter = Counter.query().get()
        if not counter:
            counter = Counter(count=0)

        counter.count += 1
        counter.put()

        self.response.headers['Content-type'] = 'application/json'
        self.response.write('{"count": %s}' % counter.count)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/count', CountHandler),
], debug=True)
