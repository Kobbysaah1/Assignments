def PrimeNums():
    data= int(input("enter a number: "))
    i=1
    sum = 0
    while i<=data:
        if i+1>1 and i+1 ==3:
            i=i+1
            print (i)
        elif(i%i==0 and i%3!=0 and i%2!=0):
            if i>=2:
                 print (i)
                 sum = sum+i
        i=i+1
    print(sum +5)
PrimeNums()
