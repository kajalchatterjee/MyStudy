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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#call_list =[ x[0] for x in calls if x[0][:5]=="(080)"]
#print(call_list)

#initialize variable and and list
area_code_list=[]
from_blr_count=0
to_blr_count=0

blr_area_code="(080)"
mobile_starts_with=('7','8', '9')
fixed_area_code_starts_with="(0"


#iterate through calls list
for callingnumber,callednumber, timestamp, duration  in calls:
    #check if the calling number is a bangaluru number
    if (callingnumber[:5]==blr_area_code): #increase from count
        from_blr_count +=1
        if (callednumber[:5]==blr_area_code): #increase to call count if the called number is also a bangaluru number
            to_blr_count +=1

        #no need to check telemeraketer code as they never receive calls or text as per task4

        if callednumber.startswith(mobile_starts_with): #check if the called number is a mobile numbner
             area_code_list.append(callednumber[:4])
        elif callednumber.startswith(fixed_area_code_starts_with): #check if the called number is landline number
             area_code_index=callednumber.index(")")  #get the index position of closing bracket
             area_code_list.append(callednumber[1:area_code_index])


#Remove dup area code and sort by code
sorted_area_code_list=sorted(set(area_code_list))

#print(from_blr_count)
#print(to_blr_count)

#calculate percentage
blr_percent=round((to_blr_count/from_blr_count) * 100,2)

#Part A:
print('The numbers called by people in Bangalore have codes:')
for area_code in sorted_area_code_list:
    print(area_code)

#Part B:
print("{0} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(blr_percent))



