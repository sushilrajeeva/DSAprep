from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0
    
    def add(self, data):
        self.queue.append(data)  # Add to the right end

    def remove(self):
        if self.is_empty():
            raise IndexError("Remove from an empty queue")
        return self.queue.popleft()  # Remove from the left end efficiently
    
    def peek(self):
        if self.is_empty():
            print("Empty Queue")
            return None
        return self.queue[0]  # Peek at the leftmost item
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", " -> ".join(map(str, self.queue)))

# Example usage
input_elements = [11, 22, 33, 44]
queue = Queue()

print("Adding elements to the queue:")
for ele in input_elements:
    print(f"Adding {ele}")
    queue.add(ele)
    queue.display()

print("\nCurrent front element of the queue:", queue.peek())

print("\nRemoving two elements from the queue:")
for _ in range(2):
    removed = queue.remove()
    print(f"Removed {removed}")
    queue.display()

print("\nIs the queue empty?:", queue.is_empty())

print("\nRemoving all remaining elements:")
while not queue.is_empty():
    removed = queue.remove()
    print(f"Removed {removed}")
    queue.display()

print("\nIs the queue empty now?:", queue.is_empty())


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
