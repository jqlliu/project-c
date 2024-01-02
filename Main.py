import pandas as p
import numpy as numpy
from sklearn.linear_model import LinearRegression
import csv

with open('testset.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	field = ["age", "ltcare"]

	for i in range(200):
		writer.writerow(str(random.randint(40, 100)), str(random.randint(0, 1)))

df = p.read_csv("DataSetSunlife.csv")

reg = LinearRegression().fit(ages, ltcare)

