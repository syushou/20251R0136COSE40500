 #Stack class implementation using a Python list

class Stack:
    def __init__(self):
        #created empty list to store stack items
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
        #return the top item without removing it
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.items[-1]

    def size(self):
        #return the number of items in the stack
        return len(self.items)

    def display(self):
        #print all stack elements from top to bottom
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents (top to bottom):")
            for item in reversed(self.items):
                print(item)

#function to display menu and interact with stack class
def menu():
    s = Stack()

    while True:
        #display options to the user
        print("\nStack Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")

        #get user's choice
        choice = input("Enter your choice: ")

        if choice == "1":
            val = input("Enter value to push: ")
            s.push(val)
        elif choice == "2":
            popped = s.pop()
            if popped is not None:
                print(f"Popped value: {popped}")
        elif choice == "3":
            top = s.peek()
            if top is not None:
                print(f"Top of stack: {top}")
        elif choice == "4":
            s.display()

#enttry point of the program
if __name__ == "__main__":
    menu()