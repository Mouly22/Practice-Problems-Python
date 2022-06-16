# Write a python program that will make a dictionary from the given list of Student IDs based on the department and admitted year.
# ID explanation: 
# First 2 digits: Year
# 4th and 5th digit: Department
# 01 = CSE, 41=CS, 21=EEE, Any other digits = Other
# For example, ID: 21121347, in this ID, the first 2 digits are 21. So the year is 2021. 
# The 4th and 5th digit are 21. So the department in EEE.
# Given List [Your code should work for all types of similar IDs if the given List is changed.]:
# IDs = ['20201199','21121347','20141052','20341121','21241369','21272199',
# '19241187','19101007','20101035', '21121875', '19141534', '19301552', '21141135', '21365001']
# Sample Output (You have to print the resultant dictionary only)
# { 2020:{ 'CSE': ['20201199', '20101035'], 'CS': ['20141052', '20341121'] }, 2021:{'EEE': ['21121347', '21121875'], 'CS': ['21241369', '21141135'], 'Other': ['21272199', '21365001'] }, 2019:{'CS': ['19241187', '19141534'], 'CSE': ['19101007', '19301552'] }}
IDs = ['20201199','21121347','20141052','20341121','21241369','21272199','19241187','19101007','20101035', '21121875', '19141534', '19301552', '21141135', '21365001']
dct = {}
for i in IDs:
    yr = "20" + i[:2]
    dept = i[3:5]
    if dept == '01':
        val = "CSE"
    elif dept == '41':
        val = 'CS'
    elif dept == '21':
        val = "EEE"
    else:
        val = "Other"

    if yr not in dct.keys():
        dct[yr] = {val: [i]}
    else:
        if val not in dct[yr].keys():
            dct[yr][val] = [i]
        else:
            dct[yr][val].append(i)    
print(dct)