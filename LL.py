class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# SLL
class SLL:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def insert_end(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = temp

    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_front(data)
            return

        temp = Node(data)
        current = self.head
        position = 0

        while current is not None and position < index - 1:
            current = current.next
            position += 1

        if current is None:
            print("Invalid index")
            return

        temp.next = current.next
        current.next = temp

    def delete_front(self):
        if self.head is None:
            return

        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next = None

    def delete_at_index(self, index):
        if index < 0 or self.head is None:
            print("Invalid index")
            return

        if index == 0:
            self.delete_front()
            return

        current = self.head
        position = 0

        while current.next is not None and position < index - 1:
            current = current.next
            position += 1

        if current.next is None:
            print("Invalid index")
            return

        current.next = current.next.next

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def show(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# DLL
class DLL:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        temp = Node(data)
        temp.next = self.head

        if self.head is not None:
            self.head.prev = temp

        self.head = temp

    def insert_end(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = temp
        temp.prev = current

    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_front(data)
            return

        current = self.head
        position = 0

        while current is not None and position < index - 1:
            current = current.next
            position += 1

        if current is None:
            print("Invalid index")
            return

        temp = Node(data)
        temp.next = current.next
        temp.prev = current

        if current.next is not None:
            current.next.prev = temp

        current.next = temp

    def delete_front(self):
        if self.head is None:
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            return

        current = self.head

        while current.next is not None:
            current = current.next

        if current.prev is not None:
            current.prev.next = None
        else:
            self.head = None

    def delete_at_index(self, index):
        if index < 0 or self.head is None:
            print("Invalid index")
            return

        if index == 0:
            self.delete_front()
            return

        current = self.head
        position = 0

        while current is not None and position < index:
            current = current.next
            position += 1

        if current is None:
            print("Invalid index")
            return

        current.prev.next = current.next

        if current.next is not None:
            current.next.prev = current.prev

    def reverse(self):
        current = self.head

        while current is not None:
            current.next, current.prev = current.prev, current.next
            self.head = current
            current = current.prev

    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def show(self):
        current = self.head

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")


# CLL
class CLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, data):
        temp = Node(data)

        if self.front is None:
            self.front = self.rear = temp
            temp.next = temp
        else:
            temp.next = self.front
            self.front = temp
            self.rear.next = self.front

    def insert_end(self, data):
        temp = Node(data)

        if self.front is None:
            self.front = self.rear = temp
            temp.next = temp
        else:
            temp.next = self.front
            self.rear.next = temp
            self.rear = temp

    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_front(data)
            return

        if self.front is None:
            print("Invalid index")
            return

        current = self.front
        position = 0

        while position < index - 1 and current.next != self.front:
            current = current.next
            position += 1

        if position != index - 1:
            print("Invalid index")
            return

        temp = Node(data)
        temp.next = current.next
        current.next = temp

        if current == self.rear:
            self.rear = temp

    def delete_front(self):
        if self.front is None:
            return

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

    def delete_end(self):
        if self.front is None:
            return

        if self.front == self.rear:
            self.front = self.rear = None
            return

        current = self.front

        while current.next != self.rear:
            current = current.next

        current.next = self.front
        self.rear = current

    def delete_at_index(self, index):
        if index < 0 or self.front is None:
            print("Invalid index")
            return

        if index == 0:
            self.delete_front()
            return

        current = self.front
        position = 0

        while position < index - 1 and current.next != self.front:
            current = current.next
            position += 1

        if position != index - 1 or current.next == self.front:
            print("Invalid index")
            return

        target = current.next
        current.next = target.next

        if target == self.rear:
            self.rear = current

        self.rear.next = self.front

    def reverse(self):
        if self.front is None or self.front == self.rear:
            return

        old_front = self.front
        current = self.front
        prev = self.rear

        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

            if current == old_front:
                break

        self.front = self.rear
        self.rear = old_front
        self.rear.next = self.front

    def length(self):
        if self.front is None:
            return 0

        count = 0
        current = self.front

        while True:
            count += 1
            current = current.next

            if current == self.front:
                break

        return count

    def show(self):
        if self.front is None:
            print("Empty list")
            return

        current = self.front

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.front:
                break

        print("(front)")


def main():
    print("1. Singly Linked List")
    print("2. Doubly Linked List")
    print("3. Circular Linked List")

    choice = int(input("Choose linked list: "))

    if choice == 1:
        obj = SLL()
    elif choice == 2:
        obj = DLL()
    elif choice == 3:
        obj = CLL()
    else:
        print("Invalid choice")
        return

    while True:
        print("\n1. Insert at Front")
        print("2. Insert at End")
        print("3. Insert at Index/Position")
        print("4. Delete at Front")
        print("5. Delete at End")
        print("6. Delete at Index/Position")
        print("7. Reversal")
        print("8. Show")
        print("9. Length")
        print("0. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            data = input("Enter data: ")
            obj.insert_front(data)

        elif ch == 2:
            data = input("Enter data: ")
            obj.insert_end(data)

        elif ch == 3:
            data = input("Enter data: ")
            index = int(input("Enter index (0-based): "))
            obj.insert_at_index(data, index)

        elif ch == 4:
            obj.delete_front()

        elif ch == 5:
            obj.delete_end()

        elif ch == 6:
            index = int(input("Enter index (0-based): "))
            obj.delete_at_index(index)

        elif ch == 7:
            obj.reverse()
            print("List reversed successfully!")
            obj.show()

        elif ch == 8:
            obj.show()

        elif ch == 9:
            print("Length:", obj.length())

        elif ch == 0:
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
