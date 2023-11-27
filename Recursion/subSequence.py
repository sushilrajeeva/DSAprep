def fib(number: int) -> int:
    
    # Base Condition
    if number == 0: return 0
    if number == 1: return 1
    
    # Work
    return fib(number - 1) + fib(number - 2)

number = 4
print("Fibonacci value of", number, "is :", fib(number))

# Subsequences
# it's a contigous/ non-contigous sequence, which follows the order


# Find all the sub-sequence of the array
# https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=7

def subSeq(inputArr: list, sequence: list = [], index: int = 0):
    
    # Base Condition
    if(index == len(inputArr)):
        return print(sequence, end="\n")
        
    
    # Algo for Take
    sequence.append(inputArr[index])
    subSeq(inputArr, sequence, index+1)
    
    # Algo for Leave
    sequence.pop()
    subSeq(inputArr, sequence, index+1)
      
    
inputArr = [3, 2, 1]

print("Given Input Array :", inputArr)
print("Sub-sequences of the given Array :")
subSeq(inputArr)
        
        
# Printing all the subsequences of an array whose sum is a perticular number
def sumSubSeq(inputArr: list, target: int, sequence: list = [], index: int = 0):
    
    # Base Condition
    if index == len(inputArr): # I have gone to the last index, i,e i have traversesd to end of a sequence
        # Print but only if sum of the elements in sequence is the required sum
        if(sum(sequence) == target):
            print(sequence, end="\n")
        return
            
    # Algo for Take
    sequence.append(inputArr[index])
    sumSubSeq(inputArr, target, sequence, index+1)
    
    # Algo for Leave
    sequence.pop()
    sumSubSeq(inputArr, target, sequence, index+1)
    

inputArr = [1, 2, 1]
target = 2

print("Given Input Array :", inputArr)
print("Sub-sequences of the given Array where sum is", target, "is :")
sumSubSeq(inputArr, target)

# Modified - > print any one subsequnce whose sum is k

# (Technique to print only one answer)

def firstSumSubSeq(inputArr: list, target: int, sequence: list = [], index: int = 0):
    
    # Base Condition
    if index == len(inputArr): # I have gone to the last index, i,e i have traversesd to end of a sequence
        # Print but only if sum of the elements in sequence is the required sum
        if(sum(sequence) == target):
            print(sequence, end="\n")
            return True
        return False
            
    # Algo for Take
    sequence.append(inputArr[index])
    if(firstSumSubSeq(inputArr, target, sequence, index+1)): return True
    
    # Algo for Leave
    sequence.pop()
    if(firstSumSubSeq(inputArr, target, sequence, index+1)): return True
    
    return False
    

inputArr = [1, 2, 1]
target = 2

print("Given Input Array :", inputArr)
print("First Sub-sequences of the given Array where sum is", target, "is :")
firstSumSubSeq(inputArr, target)

# Modified -> Give the count of how many sub-sequences satisfies the sum = k condition

# def countSumSubSeq(inputArr: list, target: int, sequence: list = [], index: int = 0) -> int:
    
#     if index == len(inputArr):
#         if(sum(sequence) == target):
#             return 1
#         return 0
    
#     # Logic for Take
#     sequence.append(inputArr[index])
#     left = countSumSubSeq(inputArr, target, sequence, index+1)
    
#     # Logic for Leave 
#     sequence.pop()
#     right = countSumSubSeq(inputArr, target, sequence, index+1)
    
#     return left + right

# More optimized version
def countSumSubSeq(inputArr: list, target: int, index: int = 0, current_sum: int = 0) -> int:
    if index == len(inputArr):
        return 1 if current_sum == target else 0

    # Include the current element in the sum
    count_with = countSumSubSeq(inputArr, target, index + 1, current_sum + inputArr[index])
    
    # Exclude the current element from the sum
    count_without = countSumSubSeq(inputArr, target, index + 1, current_sum)
    
    return count_with + count_without


    
inputArr = [2, 1, 2, 1]
target = 2

print("Given Input Array :", inputArr)
print("Count of Sub-sequences of the given Array where sum is", target, "is :")
print(countSumSubSeq(inputArr, target))