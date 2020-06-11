"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

called_numbers= [x[1]  for x in calls]
#print(called_numbers)
#print(calls[:[1:4]])

telemarketer_list=[x[0] for x in  calls  if x[0] not in called_numbers and any(x[0] in y for y in texts)==False]

print('These numbers could be telemarketers:')
print('\n'.join(sorted(set(telemarketer_list))))

#print(calls_list)
#print(calls_list.items())
