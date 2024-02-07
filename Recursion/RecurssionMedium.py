# Reverse a given string using recursion
def reverse_string(string: str) -> None:
    
    n = len(string)
    
    if n == 0:
        return ""
    
    
    # Faith
    return reverse_string(string[1:]) + string[0]

print("Reverse a string using recursion")
string = "sushil"
print(reverse_string(string))