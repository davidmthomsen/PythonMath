def factors(num):
    ''' returns a list of factors of num'''
    factor_list = []
    for i in range(1,num+1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list

print(factors(120))

# Exercise 3-1 
def gcf(num1, num2):    # Decalre the function and take two variables
    if num1 > num2:     # compare the two variables if num1 is greater than num2 then swap
        num1, num2 = num2, num1
    
    for i in range(num1, 0, -1):    # loop with range starting from num1, counting down to 1 range(from, to+1, step)
        if num1 % i == 0 and num2 % i == 0:     # if both num1 and num2 are evenly divisable by i return i
            return i