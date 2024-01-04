# Program to generate Pascal’s Triangle
# Problem Statement: This problem has 3 variations. They are stated below:

# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

# Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

# Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.

# In Pascal’s triangle, each number is the sum of the two numbers directly above it as shown in the figure below:



# Variant 1
# In this case, we are given the row number r and the column number c, and we need to find out the element at position (r,c). 

# Naive Approach
# In this case, we are given the row number r and the column number c, and we need to find out the element at position (r,c). 

# One of the Naive approaches is to generate the entire Pascal triangle and then find the element at position (r,c). We will discuss in variation 3 how to generate Pascal’s triangle.

# We have an easier formula to find out the element i.e. r-1Cc-1. Let’s try to analyze the formula to find the value of the combination assuming r-1 as n and c-1 as r:

def findPascalElement(rows: int, columns: int) -> int:
    
    numerator = 1
    denominator = 1
    rows = rows-1
    columns = columns-1
    
    # formula is n-1 c r-1 => row -1 c col - 1
    
    for i in range(columns):
        
        numerator = numerator * (rows-i)
        
        denominator = denominator * (i+1)
        
    return numerator // denominator

print(findPascalElement(5, 3))


# Variant 2
# Given the row number n. Print the n-th row of Pascal’s triangle.

# Our first observation regarding Pascal’s triangle should be that the n-th row of the triangle has exactly n elements. With this observation, we will proceed to solve this problem.

def getPascalRow(row: int) -> list:
    
    pascal_row = [findPascalElement(row,ele) for ele in range(1, row+1)]
    return pascal_row

print(getPascalRow(4))