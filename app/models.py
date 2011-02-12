from google.appengine.ext import db

class Nome(db.Model):
  nome = db.StringProperty()
  tipo = db.StringProperty()