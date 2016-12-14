from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)

@app.before_request
def before_request():
	initialize_db()

@app.teardown_request
def teardown_request(exception):
	db.close()

@app.route('/')
def home():
	return render_template('home.html') 

@app.route('/tasks/')
def tasks():
	return render_template('tasks.html',posts=Post.select().order_by(Post.date)) 

@app.route('/new_post/')
def new_post():
	return render_template('new_post.html')

@app.route('/create/',methods = ['POST'])
def create_post():
	Post.create(
		title = request.form['title'],
		tasks = request.form['tasks'],
	)
	return redirect(url_for('tasks'))

if __name__ == '__main__':
	app.run(debug=True)


