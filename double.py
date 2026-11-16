import math
i = input("What is your favorite number? We are going to multiply it by itself as many times as it is:" )
initial_number = int(i)
i = int(i)
original_number = i
limit = pow(i,i)
print (limit)
while i < limit and i != 0 and i != 1:
    print( '\n' + str(i) + f" multiplied by {i} is " + str(i*i))
    i *= original_number
    

print(f'\nThe final amount of {initial_number} to the power of {initial_number} is {i}')