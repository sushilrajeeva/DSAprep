class Queue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def add(self, data):
        self.queue.append(data)
        self.size += 1

    def remove(self):
        if self.isEmpty():
            print("Empty Queue")
            return None
        front = self.queue.pop(0)  # Directly remove the first element
        self.size -= 1
        return front
    
    def peek(self):
        if self.isEmpty():
            print("Empty Queue")
            return None
        return self.queue[0]
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue:", " -> ".join(map(str, self.queue)))

# Example usage
input = [11, 22, 33, 44]
queue = Queue()

print("Adding elements to the queue:")
for ele in input:
    print(f"Adding {ele}")
    queue.add(ele)
    queue.display()

print("\nCurrent front element of the queue:", queue.peek())

print("\nRemoving two elements from the queue:")
for _ in range(2):
    removed = queue.remove()
    print(f"Removed {removed}")
    queue.display()

print("\nIs the queue empty?:", queue.isEmpty())

print("\nRemoving all remaining elements:")
while not queue.isEmpty():
    removed = queue.remove()
    print(f"Removed {removed}")
    queue.display()

print("\nIs the queue empty now?:", queue.isEmpty())
