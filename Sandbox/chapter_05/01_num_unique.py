# summarize the number of unique values for each column using numpy

import os
os.chdir("/Users/fritz/Python_Projects/ML_Mastery/Sandbox/chapter_05")
from numpy import loadtxt
from numpy import unique
# load the dataset
data = loadtxt('oil-spill.csv', delimiter=',')
# summarize the number of unique values in each column
for i in range(data.shape[1]):
	print(i, len(unique(data[:, i])))

