def tower_of_hanoi():
    
    n = int(input("Enter number of disks: "))
    tower1 = input("Enter name of tower 1: ")
    tower2 = input("Enter name of tower 2: ")
    tower3 = input("Enter name of tower 3: ")
    
    return toh(n, tower1, tower2, tower3)
    
    
    
def toh(n: int, source, destination, helper):
    
    if n == 0:
        return
    
    toh(n-1, source, helper, destination) # Will print the instructions to move n - 1 disks from t1 to t3 using t2
    print(str(n) + "[" + str(source) + " -> " + str(destination) + "]")
    toh(n-1, helper, destination, source)
    
    
tower_of_hanoi()