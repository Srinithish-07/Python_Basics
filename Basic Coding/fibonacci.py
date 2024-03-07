# using loop
'''def Fibonacci_series(limit):
    fib_series = [0,1]
    for i in range(2,limit):
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series

limit = int(input("Enter a limit of the series : "))
result = Fibonacci_series(limit)
print(f"The fibonacci series : {result}")'''

#using recursive function
def fibonacci_series(limit):
    if limit == 0:
        return []
    elif limit == 1:
        return [0]
    elif limit == 2:
        return [0,1]
    else:
        fib_seires = fibonacci_series(limit-1)
        fib_seires.append(fib_seires[-1] + fib_seires[-2])
        return fib_seires
    
limit = int(input("Enter a limit of the series : "))
result = fibonacci_series(limit)
print(f"The fibonacci series : {result}")
