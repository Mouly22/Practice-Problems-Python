# Given a list of tuples, your task is to group the tuples based on the second element in the tuples as shown in the examples below. We can achieve this using dictionary by checking the second element in each tuple.
# [You do not need to take tuple as input and can assume that it is given as below]
# Example 1: [(20, 80), (31, 80), (1, 22), (88, 11), (27, 11)]
# Output:  {80: [(20, 80), (31, 80)], 11: [(88, 11), (27, 11)], 22: [(1, 22)]}
s = [(20, 'Sad'), (31, 'Sad'), (88, 'NotSad'), (27, 'NotSad')]
dd = {}
for i in s:
    if i[1] not in dd:
        dd[i[1]] = [i]
    else:
        dd[i[1]] += [i]
print(dd)