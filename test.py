from train import algo as trained_algo
import pandas as pd
# ****************downloading required user data file*********************
import requests
from urllib import request
import os

# 1. before doing anything firstly check if ml_run file on firebase has run instruction
# 2. loop infinitely until you get a run
# 3. just after executing run instruction set content of ml_run file to stop and repeat step 2
#  read content of ml_run file
ml_run_url = "https://storage.googleapis.com/aryaproject2-7252e.appspot.com/temp/ml_run.txt"
while True:
    if requests.get(ml_run_url).text.rstrip() == "run":

        # get user id or folder name of the specific user
        get_userid_url = 'https://storage.googleapis.com/aryaproject2-7252e.appspot.com/temp/userid.txt'
        r = requests.get(get_userid_url)
        userid = r.text.rstrip()
        print(userid)

        # get name of latest user data file for analysis
        get_recent_csv_url = 'https://storage.googleapis.com/aryaproject2-7252e.appspot.com/temp/recent_csv.txt'
        r = requests.get(get_recent_csv_url)
        recent_csv = r.text.rstrip()
        print(recent_csv)

        # url of the main user's latest health data synced
        csv_url = 'https://storage.googleapis.com/aryaproject2-7252e.appspot.com/users/'+userid+'/'+recent_csv
        print("Downloading csv file from "+csv_url)

        # function to download file from firebase
        def download_csv_data(url, filename):
            respo = request.urlopen(url)
            csv_data = respo.read()
            csv_str_data = str(csv_data)
            lines = csv_str_data.split('\\n')
            destination = str(filename)
            with open(destination, "w") as dest_file:
                print("Data of "+filename+" file is :")
                for line in lines:
                    dest_file.write(line.strip("b'\\r")+"\n")
                    print(line.strip("b'\\r"))


        download_csv_data(csv_url, filename=userid+recent_csv)

        # **********************************************************************************************************************

        # get heart-rate data from csv file
        data_file = pd.read_csv(str(userid+recent_csv), delimiter=',')

        # First row of the csv file will have these values
        data = data_file[['HeartRate', 'Temperature', 'SystolicBloodPressure', 'DiastolicBloodPressure']]

        result = trained_algo.predict(data)
        print(result)  # 1 -> lies inside circle, -1 -> lies outside of the circle

        count_inside_points = result[result == 1].size
        count_outside_points = result[result == -1].size
        total_count = result.size

        print(total_count, count_inside_points, count_outside_points)

        if count_outside_points <= 0.15 * total_count:
            print("you are in your good health condition.")
            status = "healthy"

        elif count_outside_points <= 0.3 * total_count:
            print("you may be mildly unhealthy, consult doctor")
            status = "might be unhealthy"

        else:
            print("you are definitely unhealth, consult doctor ")
            status = "unhealthy"

        # *****************************Uploading the result of ml analysis**********************
        # status of the latest csv file is named same as the csv
        recent_csv_text = recent_csv.strip(".csv") + ".txt"
        status_csv_url = 'https://storage.googleapis.com/aryaproject2-7252e.appspot.com/users/'+userid+"/"+recent_csv_text

        # entering the result of analysis (healthy/unhealthy)
        with open(recent_csv_text,  "w") as fd:
            fd.write(status)

        # uploading the file
        files = {'file': open(recent_csv_text, "rb")}
        response = requests.post(status_csv_url, files=files)
        print(response.text)

        os.remove(recent_csv_text)
        os.remove(userid+recent_csv)

        # set content of ml_run = "stop"
        files = {'file': open("ml_run.txt", "rb")}
        response = requests.post(ml_run_url, files=files)
        print(response.text)


    else:
        pass
