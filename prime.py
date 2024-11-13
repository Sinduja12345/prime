#find prime number

for num in range(1, 251): 
    if num > 1:  # Prime numbers are greater than 1
        for i in range(2, num):  # Check divisibility from 2 to num-1
            if num % i == 0:  # If num is divisible by any number other than 1 and itself
                break
        else:
            print(num)
