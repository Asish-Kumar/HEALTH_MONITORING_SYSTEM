# # ****************downloading required user data file*********************
# import requests
# from urllib import request
# import os
#
# # get user id or folder name of the specific user
# get_userid_url = 'https://storage.googleapis.com/aryaproject2-7252e.appspot.com/temp/userid.txt'
# r = requests.get(get_userid_url)
# userid = r.text.rstrip()
# print(userid)
#
# # get name of latest user data file for analysis
# get_recent_csv_url = 'https://storage.googleapis.com/aryaproject2-7252e.appspot.com/temp/recent_csv.txt'
# r = requests.get(get_recent_csv_url)
# recent_csv = r.text.rstrip()
# print(recent_csv)
#
# # url of the main user's latest health data synced
# csv_url = 'https://storage.googleapis.com/aryaproject2-7252e.appspot.com/users/'+userid+'/'+recent_csv
# print("Downloading csv file from "+csv_url)
#
#
# # function to download file from firebase
# def download_csv_data(url, filename):
#     respo = request.urlopen(url)
#     csv_data = respo.read()
#     csv_str_data = str(csv_data)
#     lines = csv_str_data.split('\\n')
#     destination = str(filename)
#     with open(destination, "w") as dest_file:
#         print("Data of "+filename+" file is :")
#         for line in lines:
#             dest_file.write(line.strip("b'\\r")+"\n")
#             print(line.strip("b'\\r"))
#
#
# download_csv_data(csv_url, filename=userid+recent_csv)
#
# # *****************************Uploading the result of ml analysis**********************
# # status of the latest csv file is named same as the csv
# recent_csv_text = recent_csv.strip(".csv") + ".txt"
# status_csv_url = 'https://storage.googleapis.com/aryaproject2-7252e.appspot.com/users/'+userid+"/"+recent_csv_text
#
# # entering the result of analysis (healthy/unhealthy)
# from test import server_send_data
# status = server_send_data()
# with open(recent_csv_text,  "w") as fd:
#     fd.write(status)
#
# # uploading the file
# files = {'file': open(recent_csv_text, "rb")}
# response = requests.post(status_csv_url, files=files)
# print(response.text)
#
# os.remove(recent_csv_text)
# os.remove(userid+recent_csv)
