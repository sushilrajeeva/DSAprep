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
        
        
    