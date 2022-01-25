x = input("enter: ")
if len(x) < 4:
    print(x)
elif len(x) > 3:
    if x.endswith('est'):
        print(x)
    elif x.endswith('er'):
        print(x.replace('er'),('est'))
    
    else:
        print(x + 'er')

    
