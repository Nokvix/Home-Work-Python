class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, elem):
        self.elements.append(elem)

    def pop(self):
        if self.is_empty():
            raise IndexError('Стек пуст')
        else:
            self.elements.pop()


class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((task, priority))

    def remove_task(self, cur_task):
        self.tasks.elements = list(filter(lambda task: task[0] != cur_task, self.tasks.elements))

    def __str__(self):
        sorted_tasks = sorted(self.tasks.elements, key=lambda task: task[1])
        result = ''

        for priority in range(sorted_tasks[0][1], sorted_tasks[-1][1] + 1):
            tasks_with_priority = [task for task, cur_priority in sorted_tasks if cur_priority == priority]

            if tasks_with_priority:
                result += f'{priority} - {"; ".join(tasks_with_priority)}\n'

        return result


def main():
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать ДЗ", 2)

    print(manager)

    manager.remove_task('поесть')
    manager.remove_task('отдохнуть')
    print(manager)


if __name__ == '__main__':
    main()
