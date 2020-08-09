from flask import Flask, request
import statistics as stat

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

@app.route('/median')
def median():
	Y =map(float, request.args.get('X').split(','))
	a= stat.median(Y) 
	return "%s \n" %a

@app.route('/min')
def min():
	Y =(request.args.get('X').split(','))
	min_ele=Y[0]
	for i in range(1,len(Y)): 
		if Y[i]<min_ele: 
			min_ele=Y[i] 
	return "%s \n" %min_ele

@app.route('/max')
def max():
	Y =request.args.get('X').split(',')
	max_ele=Y[0]
	for i in range(1,len(Y)): 
		if Y[i]>max_ele: 
			max_ele=Y[i] 
	return "%s \n" %max_ele

if __name__=='__main__':
        app.debug=True
        app.run()
