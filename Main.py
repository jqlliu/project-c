import pandas as p
import numpy as numpy
from sklearn.linear_model import LinearRegression

df = p.read_csv("DataSetSunlife.csv")
ages = df["AGES"]
ltcare = df["LIVES IN LONG TERM CARE HOME"]

