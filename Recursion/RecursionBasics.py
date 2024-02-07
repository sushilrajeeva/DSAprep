# Print n numbers in descending order using recursion

def print_numbers_descending(n: int) -> None:
    
    # Base condition
    if n == 0:
        return
    
    # Faith
    print(n)
    print_numbers_descending(n-1)
    
print("Printing in Descending order")
    
print_numbers_descending(5)


# Print in ascending order 
def print_ascending(n: int) -> None:
    
    # Base Condition
    if n == 0:
        return
    
    # Faith
    print_ascending(n-1)
    print(n)
    
print("Printing in Ascending order")
    
print_ascending(5)

# Print sum of n natural numbers

def sum_of_n_natural(n: int) -> int:
    
    if n == 1:
        return 1
    
    
    # Faith
    return n + sum_of_n_natural(n-1)

print("Sum of n natural numbers")
print(sum_of_n_natural(5))


# Print factorial of a given number
def fact(n: int) -> int:
    
    # Base Condition
    if n == 0 or n == 1:
        return 1
    
    # Faith
    return n * fact(n-1)

print("Factorial of a given number")
print(fact(5))
    
    