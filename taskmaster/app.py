from flask import Flask, render_template

app = Flask(__name__)

#create index route
#	avoids 404s when we access url
@app.route('/')
def index():
	#no path specification needed, flask knows to look in templates folder
	return(render_template('index.html'))

if __name__ == '__main__':
	app.run(debug=True)