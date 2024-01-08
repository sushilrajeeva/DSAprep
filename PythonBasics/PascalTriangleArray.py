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
    
    # Brute Force method
    
    # pascal_row = [findPascalElement(row,ele) for ele in range(1, row+1)]
    # return pascal_row
    
    pascal_row_optimized = [1] * row
    
    for i in range(1, row):
        
        numerator = pascal_row_optimized[i-1] * (row - i)
        
        pascal_row_optimized[i] = numerator // i
        
    return pascal_row_optimized
    
    
    
    

print(getPascalRow(4))

# Variation 3: 
# Given the number of rows n. Print the first n rows of Pascal’s triangle.

# Algorithm / Intuition
# Now, in the optimal approach of variation 2, we have learned how to generate a row in O(n) time complexity. So, in order to optimize the overall time complexity, we will be using that approach for every row. Thus the total time complexity will reduce.

# First, we will run a loop(say row) from 1 to n.
# Inside the loop, we will call a generateRow() function and add the returned list to our final answer. Inside the function we will do the following:
# First, we will store the 1st element i.e. 1 manually.
# After that, we will use a loop(say col) that runs from 1 to n-1. It will store the rest of the elements.
# Inside the loop, we will use the specified formula to print the element. We will multiply the previous answer by (row-col) and then divide it by col itself.
# Thus, the entire row will be stored and returned.
# Finally, we will return the answer list.

def generate_pascal_triangle(height: int):
    
    pascal_triangle = []
    
    for i in range(1, height + 1):
        
        pascal_triangle.append(getPascalRow(i))
        
    return pascal_triangle

print(generate_pascal_triangle(5))
