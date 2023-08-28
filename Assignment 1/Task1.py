# Write a Python program to get the Fibonacci series between 0 to 50

def fibonacciSeries(n):
    # a = []
    if n <= 1:
        # print ("hhi")
        return n
        
    else:
        # print("hhiiiii")
        return fibonacciSeries(n-1) + fibonacciSeries(n-2)

n = 10
a =[]
for i in range(1, n):
    # print(fibonacciSeries(i))
    a.append(fibonacciSeries(i))
print(a)
