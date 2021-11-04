#!/usr/bin/python

import json
import random
import time

# List to be used with the randomization functions
username = ['A123456', 'Z789321', 'abc0987', 'xyz56789', 'TST76544', 'Alistair', 'Bethany']
message = ['Login_Success', 'Login_Failure', 'Alarm','data entry','test', 'text']
severity_txt = ['Very-High', 'High', 'Medium','Low']
location = ['loc1','loc2','loc3','null']

# Never-ending loop through CEF generator
while True:

# Insert time error
    # Use 'ts' for consistent timestamp to milliseconds
    ts = str(int(time.time()*1000))

    # Use 'ts_2' for random > now() time error for testing 
    ts_2 = str(int(time.time()*1000))
    if random.randint(1,100) >= 85:
        ts_2 = str(int(time.time()*1200))

    sel_severity_txt = random.choice(severity_txt)
    sel_username = random.choice(username)
    sel_message = random.choice(message)
    sel_loc = random.choice(location)
    sel_severity_int = str(random.randint(1,9))
    event_id = str(random.randint(1000000,9999999))
    ip = str(random.randint(1,255))
    ip2 = str(random.randint(1,255))
    ip3 = str(random.randint(1,255))

    cef_message = "CEF:0|DATASRCNAME|FLEX|1.0|MIDNIT|New day|" + sel_severity_txt + "|eventId=" + event_id + " eventmsg=" + sel_message + " deviceSeverity=" + sel_severity_int + "    tsepoch=" + ts_2 + "    cs3=abcdefgh cs4=" + sel_loc + " flexString1=d flexNumber2=0 suser=" + sel_username + " cs3Label=name cs4Label=locations flexString1Label=type  flexNumber2Label=value ahost=testhost1 agt=10.0.3." + ip + " dvchost=testHOST2 shost=TESTHOST3 dvc=100.101.102." + ip2 + " src=11.12.13." + ip3

# Pausing the loop for ## seconds
    time.sleep(5)

# End of script

    print(cef_message)
