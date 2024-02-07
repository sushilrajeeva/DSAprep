def tower_of_hanoi():
    
    n = int(input("Enter number of disks: "))
    source = input("Enter name of source: ")
    destination = input("Enter name of destination: ")
    helper = input("Enter name of helper: ")
    
    return toh(n, source, destination, helper)
    
    
    
def toh(n: int, source, destination, helper):
    
    if n == 0:
        return
    
    toh(n-1, source, helper, destination) # Will print the instructions to move n - 1 disks from t1 to t3 using t2
    print("Transfer disk " + str(n) + " from " + str(source) + " -> " + str(destination))
    toh(n-1, helper, destination, helper)
    
    
tower_of_hanoi()