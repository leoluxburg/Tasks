from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__ ,static_url_path='/static')
@app.before_request
def before_request():
	"""Abre la base de datos"""

	initialize_db()

@app.teardown_request
def teardown_request(exception):
	"""Cierra la base de datos"""
	db.close()

@app.route('/')
def home():
	"""Homepage"""
	return render_template('home.html')

@app.route('/tasks/')
def tasks():
	"""Tasks Pages"""
	return render_template('tasks.html',posts=Post.select().order_by(Post.date))

@app.route('/new_post/')
def new_post():
	"""Creacion de tasks"""
	return render_template('new_post.html')

@app.route('/create/',methods = ['POST'])
def create_post():
	"""Metodo para la creacion de los tasks"""
	Post.create(
		title = request.form['title'],
		tasks = request.form['tasks'],
	)
	return redirect(url_for('tasks'))

if __name__ == '__main__':
	app.run(debug=True)
