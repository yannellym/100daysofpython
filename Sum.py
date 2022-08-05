Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)


def find(n):
    sum = 0
    for i in range(0,n+1):
        if i % 3 == 0:
            sum += i 
        if i % 5 == 0:
            sum += i 
    return sum
