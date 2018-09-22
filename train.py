from sklearn import svm
import pandas as pd
import classify_users

switcher = {
    "ALGO A": "male_50_60.csv",
    "ALGO B": "male_60_90.csv",
    "ALGO C": "male_60_90.csv",
    "ALGO D": "male_60_90.csv",
    "ALGO E": "female_50_60.csv",
    "ALGO F": "female_60_90.csv",
    "ALGO G": "female_60_90.csv",
    "ALGO H": "female_60_90.csv"
}

# get heart-rate data from csv file
data_file = pd.read_csv(switcher[classify_users.result_algo], delimiter=',')

# First row of the csv file will have these values
data = data_file[['HeartRate', 'Temperature', 'SystolicBloodPressure', 'DiastolicBloodPressure']]
# data = data_file[['A', 'B']]
# training algo
algo = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
algo.fit(data)
