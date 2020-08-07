from flask import Flask, request
import statistics as stat
import sys

app=Flask(__name__)


@app.route('/')
def index():
    return 'Usage;\n<Operation>?X=sys.args[0].split(',')\n'

@app.route('/median')
def median():
	Y =map(float, request.args.get('X').split(','))
	
	a= stat.median(Y) 
	return "%s \n" %a



if __name__=='__main__':
        app.debug=True
        app.run()
