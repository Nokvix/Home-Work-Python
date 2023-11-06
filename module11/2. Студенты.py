from random import randint


class Student:

    def __init__(self, full_name, group_number, academic_performance):
        self.full_name = full_name
        self.group_number = group_number
        self.academic_performance = academic_performance[::]
        self.average_score = sum(academic_performance) / len(academic_performance)

    def print_info(self):
        print(
            self.full_name,
            self.academic_performance,
            self.average_score
        )


def get_average_score(student):
    return student.average_score


students = []
for _ in range(3):
    full_name = input('Введите фамилию и имя через пробел (Иванов Иван): ')
    group_number = input('Введите номер группы: ')
    academic_performance = [int(input(f'Введите оценку за {i}-й предмет: ')) for i in range(5)]
    # academic_performance = [randint(2, 5) for i in range(5)]
    students.append(Student(full_name, group_number, academic_performance))

sorted_students = sorted(students, key=get_average_score)

for stud in students:
    stud.print_info()

print()

for stud in sorted_students:
    stud.print_info()
