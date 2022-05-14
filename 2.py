
def computepay(x, y):
    if x > 40:
        v1 =  (40 + ((x-40)*1.5))*10.5
        return v1
    else:
        v1 = x*y
        return v1
p = computepay(float(input("Enter hour: ")),float(input("Enter rate: ")))
print(p)
