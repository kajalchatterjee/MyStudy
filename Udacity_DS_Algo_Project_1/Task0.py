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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

#Get the 1st item for the text from the list
if len(texts) > 0:
    text_list=texts[0]
    if len(text_list) > 0:
        print("First record of texts, {0} texts {1} at time {2}".format(text_list[0], text_list[1], text_list[2]))

#Get the last iten item for the text from the list
if len(calls) > 0:
    call_list= calls[-1]
    if len(call_list) > 0:
        print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(call_list[0], call_list[1], call_list[2], call_list[3]))
