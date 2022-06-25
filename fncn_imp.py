def fun1(sub3, sub1, sub2):
    print("My firend is" + sub2)

fun1(sub2= 'ohi', sub3 = 'onnesha', sub1 = 'Samiha')



def fun1(**sub):
    print(f"My firend is", sub['CSE'])

fun1(biotech= 'ohi', microbio = 'onnesha', CSE = 'Samiha')
print(fun1)



def func(k):
    a ='local a' +k
    print(a)
func(' 20')


#use of global a:
s = 'Fahad is cute.'
print(s)
def func1(m, n ):
    global s
    s = s + m
    print(s)
    s = s +' Mouly is cute.' 
    print(s)
    s = s + n
    
func1(' He loves mouly <3.', 'She loves fahad <3.')
print(s)



#use of nonlocal a
g = 1
def random():
    g = 2
    print(g)
    def ran():
        nonlocal g
        g = g + 3
        print(g)
    ran()
    
    print(g)

random()
print(g)