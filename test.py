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
main_median  = []
main_max     = []
main_min     = []

test_mean    = []
test_avg     = []
test_average = []
test_median  = []
test_max     = []
test_min     = []


test_mean.append(stat.mean(X))
test_avg.append(stat.mean(X))
test_average.append(stat.mean(X))
test_median.append(stat.median(X))
test_min.append(min(X))
test_max.append(max(X))




r1 = requests.get('http://127.0.0.1:5000/mean?X=1,1.2,3,-5,0,100')
data1= r1.json()
main_mean.append(data1)

r2 = requests.get('http://127.0.0.1:5000/avg?X=1,1.2,3,-5,0,100')
data1= r2.json()
main_avg.append(data1)

r3 = requests.get('http://127.0.0.1:5000/average?X=1,1.2,3,-5,0,100')
data1= r3.json()
main_average.append(data1)


r4 = requests.get('http://127.0.0.1:5000/median?X=1,1.2,3,-5,0,100')
data2= r4.json()
main_median.append(data2)

r5 = requests.get('http://127.0.0.1:5000/min?X=1,1.2,3,-5,0,100')
data3 = r5.json()
main_min.append(data3)

r6 = requests.get('http://127.0.0.1:5000/max?X=1,1.2,-5,0,100')
data4 = r6.json()
main_max.append(data4)


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

if main_median == test_median:
	print ("Median OK")
else:
	print ("Median not OK")

if main_min == test_min:
	print ("Min OK")
else:
	print ("Min not OK")

if main_max == test_max:
	print ("Max OK")
else:
	print ("Max not OK")



print ("testing done")

