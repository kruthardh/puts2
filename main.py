from flask import Flask, request
import statistics as stat
import sys

app=Flask(__name__)


@app.route('/')
def index():
    return 'Usage;\n<Operation>?X=sys.args[0].split(',')\n'

@app.route('/mean')
@app.route('/avg')
@app.route('/average') 
def mean():
	Y =map(float, request.args.get('X').split(','))
	b= stat.mean(Y) 
	return "%s\n" %b



if __name__=='__main__':
        app.debug=True
        app.run()
