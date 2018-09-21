from sklearn import svm
import pandas as pd

# get heart-rate data from csv file
data_file = pd.read_csv("output6.csv", delimiter=',')

# First row of the csv file will have these values
data = data_file[['HeartRate', 'Temperature', 'SystolicBloodPressure', 'DiastolicBloodPressure']]
# data = data_file[['A', 'B']]
# training algo
algo = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
algo.fit(data)
