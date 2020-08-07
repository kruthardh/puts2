#!usr/bin/python
from flask import Flask, request
import unittest
import requests
import json
import statistics as stat



X = [1, 1.2 ,3 ,-5,0,100]

main_mean    = []
main_avg     = []
main_average = []

test_mean    = []
test_avg     = []
test_average = []



test_mean.append(stat.mean(X))
test_avg.append(stat.mean(X))
test_average.append(stat.mean(X))



r1 = requests.get('http://127.0.0.1:5000/mean?X=1,1.2,3,-5,0,100')
data1= r1.json()
main_mean.append(data1)

r2 = requests.get('http://127.0.0.1:5000/avg?X=1,1.2,3,-5,0,100')
data1= r2.json()
main_avg.append(data1)

r3 = requests.get('http://127.0.0.1:5000/average?X=1,1.2,3,-5,0,100')
data1= r3.json()
main_average.append(data1)


if main_mean == test_mean:
	print ("Mean OK")
else:
	print ("Mean not OK")

if main_avg == test_avg:
	print ("Avg OK")
else:
	print ("Avg not OK")

if main_average == test_average:
	print ("Average OK")
else:
	print ("Average not OK")

