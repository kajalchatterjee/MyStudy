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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#join the phone numbers from each calls and text list to form a new list of list
text_list =[ [x[0]] + [x[1]] + [y[0]] + [y[1]] for (x,y) in zip(texts, calls)]
#combine list of list into a single list
result = sum(text_list, [])
#use set to remove dup telephone numbers
record_set=set(result)
print("There are {0} different telephone numbers in the records.".format(len(record_set)))
