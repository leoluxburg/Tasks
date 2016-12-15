from peewee import *
import datetime
db= SqliteDatabase('posts.db')

class Post(Model):
	id = PrimaryKeyField()
	date = DateTimeField(default = datetime.datetime.now)
	title = CharField()
	tasks = TextField()
	""" Peewee """

	class Meta:
		database = db

def initialize_db():
	""" La creacion de la abase de datos"""

	db.connect()
	db.create_tables([Post], safe = True)
