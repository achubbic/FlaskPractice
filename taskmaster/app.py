from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#tells app where bd is located			#3 for relative path, 4 for asolute
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	completed = db.Column(db.Integer, default=0)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

#return string every time we create new element
def __repr__(self):
	return '<Task %r>' % self.id


#create index route
#	avoids 404s when we access url
@app.route('/')
def index():
	#no path specification needed, flask knows to look in templates folder
	return(render_template('index.html'))
	#note: must manually refresh page upon index.html update

if __name__ == '__main__':
	app.run(debug=True)