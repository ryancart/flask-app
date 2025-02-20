from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Such enhancements...imma be mad if i get billed for this...'
