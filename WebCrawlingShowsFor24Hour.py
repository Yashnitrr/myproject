import requests, time, calendar, datetime
from email.utils import formatdate

# To check current time and unix time
current_time = datetime.datetime.now()
print(current_time)
unixTime = time.mktime(current_time.timetuple())
unixtime2 = int (time.time())
print (unixTime)

url = "http://mobilelistings.tvguide.com/Listingsweb/ws/rest/schedules/80004.null/start/{}/duration/1440?ChannelFields=Name&ScheduleFields=EndTime%2CStartTime%2CTitle&formattype=json".format(unixtime2)
response = requests.get(url)
jsonData = response.json()
# We got our complete data in json format in jsonData Variable

print(jsonData)
for i in jsonData:
    print (i)


# Now we will parse the json data to convert unix time into current system time.

"""
for i in jsonData:
    # print(jsonData[i])
    for key,value in i.items():
        if key=='Channel':
            for key2, value2 in i[key].items():
                print("Channel Name is: %s" %value2, end="  ")

        if key == 'ProgramSchedules':
            for k in i[key]:
                for key1, value1 in k.items():
                    print(key1, end=': ')
                    print(value1, end=' ')

'''
for j in jsonData:
    for key, value in j.items():
        if key == 'Channel':
            for key2, value2 in j[key].items():
                print ("Channel Name: %s" %value2)
        #print(key, value)
        if key=='ProgramSchedules':
            for k in j[key]:
                for key1, value1 in k.items():
                    print(key1,end=': ')
                    print(value1, end=' ')

"""
