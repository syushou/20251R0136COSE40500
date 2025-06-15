 # Stack class implementation using a Python list

class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def is_empty(self):
        # Return True if stack is empty, False otherwise
        return self.items == []

    def push(self, item):
        # Add item to the top of the stack
        self.items.append(item)
        print(f"Pushed {item} to stack.")

    def pop(self):
        # Remove and return the top item of the stack
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.items.pop()

    def peek(self):
        # Return the top item without removing it
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.items[-1]

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def display(self):
        # Print all stack elements from top to bottom
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents (top to bottom):")
            for item in reversed(self.items):
                print(item)