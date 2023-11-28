def subSeq( inputArr: list[int], target: int, sequence: list[int] = [], output: list[list[int]] = [], index: int = 0):

    # Base Condition
    # Check if the current sequence's sum equals the target
    if sum(sequence) == target:
        output.append(sequence.copy())
        return
    # If the sum exceeds or we have considered all elements, return
    if sum(sequence) > target or index == len(inputArr):
        return

    # Minimum work
    # Include current element in sequence and recurse without incrementing the index
    sequence.append(inputArr[index])
    subSeq(inputArr, target, sequence, output, index+1)
    

    # Leave logic
    sequence.pop()
    subSeq(inputArr, target, sequence, output, index+1)
    

def combinationSum( candidates: list[int], target: int) -> list[list[int]]:
    output = []
    subSeq(candidates, target, output= output)
    return output


inputArr = [2,3,6,7]
target = 7
output = []

print("Given Input Array :", inputArr)
print("Sub-sequences of the given Array where sum is", target, "is :")
print(combinationSum(inputArr, target))




