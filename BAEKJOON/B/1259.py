b = True
while(b == True):
    num = list(map(str, input()))
    
    if(num[0] == str(0)):
        b = False
    else:
        t = True
        for i in range(0, len(num)):
            j = (len(num)-1) - i
            if(num[i] != num[j]):
                t = False
        
        if(t):
            print("yes")
        else:
            print("no")
