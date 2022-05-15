#Assume, you have been given a tuple.
# a_tuple = ("The Institute",
# ("Best Mystery & Thriller", "The Silent Patient", 68821),
# 75717,
# [1, 2, 3, 400, 5, 6, 7],
# ("Best Fiction", "The Testaments", 98291)
# )
# Write one line of Python code to access and print the value 400.
a_tuple = ("The Institute",
("Best Mystery & Thriller", "The Silent Patient", 68821),
75717,
[1, 2, 3, 400, 5, 6, 7],
("Best Fiction", "The Testaments", 98291)
)
c = a_tuple[3][3]
print(c)