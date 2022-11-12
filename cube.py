def cb(x):
    y = x*x*x
    return y

for i in range(20):
    a = i
    
    
    if i%2 == 1: #this does the odd number
        a = cb(i)
        print(a)
    else:
        a = i
        print(a)
