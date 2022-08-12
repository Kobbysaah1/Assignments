from cmath import sqrt
def std():
#variables
    sum =0 
    var =0
    sd = 0

#standard deviation operation
    data = [30,21,23,45,66,77,3,4,55,22,33,55,777,88]
    n = int (len(data))
    for i in(data):
        sum = sum + i
    mean = (sum/n)
    for i in data:
       var=var+ ((i-mean)*(i-mean))/n
    sd =round(abs(sqrt(var)),4)

# output from the inputs
    print(("The sum of the data set is"),(sum))
    print(("number of data set:"),(n))
    print(("The mean is:"),(mean))
    print(("The variance of the data set is:"),(round((abs(var)),4)))
    print(("The standard deviation is"),(sd),)
print(std())