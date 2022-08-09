def PrimeNums():
    data = int (input("Enter a number: "))
    sum = 0
    for i in range(2,data):
        if i==2 or i==3:
            print(i)
            i+1
            sum = sum+i
        elif(i%3!=0 and i%2!=0):
            print(i)
            sum = sum+i
            i=i+1
    print(("The sum of prime numbers less than"),(data),("is"),(sum))

PrimeNums()
