#find prime number

for num in range(1, 251): 
    if num > 1: 
        for i in range(2, num): 
            if num % i == 0:  
                break
        else:
            print(num)



#to Redirect Output to a Text File
#Bash

python3 prime_script.py >> results.txt

