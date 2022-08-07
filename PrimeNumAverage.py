def PrimeNums():
    data= int(input("enter a number: "))
    j=0
    sum = 0
    for i in range(2,data):
        if i == 2 or i ==3:
            print (i)
            i+1
            j=j+1
            sum = sum+i
        elif(i%i==0 and i%3!=0 and i%2!=0):
            print (i)
            j=j+1
            sum = sum+i
            i=i+1
        
    print(("The sum of prime numbers less than"),(data),("is"),(sum))
    print(("Number of prime numbers:"),(j))
    PrimeNumsAverage = sum/j
    print(("The average of prime numbers less than"),(data),("is"),(PrimeNumsAverage))
PrimeNums()