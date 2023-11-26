# Summation of N natural numbers

# Parameterized way

def summationParam(number: int, sum: int = 0) -> int:
    
    # Base Condition
    if(number < 1):
        return sum
    
    # Minimum work
    return summationParam(number=number-1, sum=sum+number)

number = 5
print("Param - Summation of", number, "natural numbers is :", summationParam(number))

def summationFunc(number: int) -> int:
    
    # Base Condition
    if(number == 0):
        return 0
    
    # Minimum work
    return number + summationFunc(number-1)
    

print("Func - Summation of", number, "natural numbers is :", summationFunc(number))


# Factorial of N

def fac(number: int) -> int:
    
    if(number == 1 or number == 0):
        return 1
    
    return number * fac(number-1)


num = 5

print("Factorial of", num, "is :", fac(num))