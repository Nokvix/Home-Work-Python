class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def get(self, index: int) -> int:
        current_node = self.head
        counter = 0
        while current_node:
            if counter == index:
                return current_node.data
            current_node = current_node.next_node
            counter += 1
        raise IndexError("Index out of range")

    def remove(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next_node
                return
            else:
                raise IndexError("Index out of range")

        current_node = self.head
        counter = 0
        while current_node and counter < index - 1:
            current_node = current_node.next_node
            counter += 1

        if current_node and current_node.next_node:
            current_node.next_node = current_node.next_node.next_node
        else:
            raise IndexError("Index out of range")

    def __str__(self) -> str:
        result = "["
        current_node = self.head
        while current_node:
            result += str(current_node.data)
            if current_node.next_node:
                result += " "
            current_node = current_node.next_node
        result += "]"
        return result


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
