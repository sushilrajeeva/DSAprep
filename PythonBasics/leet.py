def groupAnagrams(strs: list[str]) -> list[list[str]]:
        
        if strs == [""]: return [[""]]

        if len(strs) == 1: return [strs]

        keyDict = {}

        for word in strs:

            ## checking if the sorted word exists as key in keyDict if exist then add it to value
            key = ''.join(sorted(word)) 
            # print("key", key)
            # print("value", keyDict.get(key,[]))
            if(key in keyDict.keys()):
                keyDict[key].append(word)
            else:
                
                keyDict[key] = [word]
                

        return keyDict.values()
        
        
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


from collections import Counter
def productExceptSelf(nums: list[int]) -> list[int]:
        
    # Approach 1

    count_zero = Counter(nums).get(0, 0)

    if(count_zero > 1):
        return [0 for i in range(len(nums))]

    zero_index = -1
    prod = 1
    for i in range(len(nums)):
        if(nums[i] == 0): zero_index = i
        else: prod *= nums[i]
    
    if(count_zero == 1):
        answer = []
        for i in range(len(nums)):
            answer.append(0) if i != zero_index else answer.append(prod)
        return answer
    
    return [prod//nums[i] for i in range(len(nums))]

print(productExceptSelf([-1,1,0,-3,3]))

def isValidSudoku(board: list[list[str]]) -> bool:
    seen = set()

    for i in range(9):
        for j in range(9):
            number = board[i][j]
            if number != ".":
                row_key = f"{number} in row {i}"
                col_key = f"{number} in column {j}"
                box_key = f"{number} in box {i//3}-{j//3}"

                if (row_key in seen) or (col_key in seen) or (box_key in seen):
                    return False
                
                seen.update({row_key, col_key, box_key})

    print(seen)
    return True

board = [["5","5",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

# LeetCode -> https://leetcode.com/problems/encode-and-decode-strings/
def encode(strs):
    encode_str = ""
    for word in strs:
        # Escape any natural occurrence of ":;"
        escaped_word = word.replace(":;", ":;;")
        
        if encode_str == "":
            encode_str = escaped_word
        else:
            encode_str = encode_str + ":;" + escaped_word  

    return encode_str

def decode(s):
    # Split by the delimiter and unescape any escaped ":;"
    return [word.replace(":;;", ":;") for word in s.split(":;")]


input = ["lint","code","love","you"]
print("Input -> ", input)
encode_str = encode(input)

print("Output -> ", decode(encode_str))

input1 = ["we", "say", ":", "yes"]
encode_str1 = encode(input1)
print("Input -> ", input1)
print("Output -> ", decode(encode_str1))