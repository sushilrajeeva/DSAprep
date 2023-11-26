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
        
    