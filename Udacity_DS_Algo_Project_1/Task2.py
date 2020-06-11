"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from collections import defaultdict
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

result = defaultdict(int)

#iterate through calls list
#create dictionary object with cell phone number as key and duration as value
for callingnumber,callednumber, timestamp, duration  in calls:
    result[callingnumber] += int(duration)
    result[callednumber] += int(duration)

#print(result)

#get the key containg max value
phone_number=max(result, key=lambda k: result[k])

#join the phone numbers from each calls and text list to form a new list of list
#calls_list =[ [x[0] , x[-1]] for x in calls]
#combine list of list into a single list
#print(calls_list)
#calls_list_sorted=sorted(calls_list, key = lambda x: int(x[1]))
#print(calls_list_sorted)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(phone_number, result[phone_number]))



