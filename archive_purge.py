from datetime import datetime, timedelta
import subprocess
import os

#Convert Unixtime to datetime object
#def convert_unixtime(timestamp):
#    return datetime.datetime.fromtimestamp(float(timestamp))

#Fetch unixtime from aws cli
timestamp_dday = subprocess.check_output('aws storagegateway describe-tape-archives | grep DDAY | cut -f 2', shell=True)
timestamp_dmon = subprocess.check_output('aws storagegateway describe-tape-archives | grep DMON | cut -f 2', shell=True)

if timestamp_dmon is None:
    timestamp_dmon = 0


print timestamp_dday
print timestamp_dmon

#Below for debugging
#timestamp = 1473875764.39
#print convert_unixtime(float(timestamp))

#Date Comparison
backup_date_dday = datetime.fromtimestamp(float(timestamp_dday))
backup_date_dmon = datetime.fromtimestamp(int(float(timestamp_dmon)))
today_date = datetime.today()

if (today_date - backup_date_dday) > timedelta(days=31):
    tape_to_delete = subprocess.check_output('aws storagegateway describe-tape-archives | grep DDAY | cut -f 2', shell=True)
    os.system('aws storagegateway delete-tape-archive --tape-arn tape_to_delete')

if (today_date - backup_date_dmon) > timedelta(months=12):
    tape_to_delete = subprocess.check_output('aws storagegateway describe-tape-archives | grep DMON | cut -f 2', shell=True)
    os.system('aws storagegateway delete-tape-archive --tape-arn tape_to_delete')
