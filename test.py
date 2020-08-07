#!usr/bin/python
from flask import Flask, request
import unittest
import requests
import json
import statistics as stat



X = [1, 1.2 ,3 ,-5,0,100]

main_median    = []


test_medan    = []




test_median.append(stat.median(X))




r4 = requests.get('http://127.0.0.1:5000/median?X=1,1.2,3,-5,0,100')
data1= r4.json()
main_medan.append(data1)



if main_median == test_median:
	print ("Median OK")
else:
	print ("Median not OK")

