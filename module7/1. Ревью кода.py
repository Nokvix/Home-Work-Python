students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def get_data_interests_surnames(student_dictionary):
    student_interests = set()
    total_length_surnames = 0
    for i_student in student_dictionary:
        student_interests.update(student_dictionary[i_student]['interests'])
        total_length_surnames += len(student_dictionary[i_student]['surname'])
    return student_interests, total_length_surnames


list_pairs_id_age = [
    (student_id, student_data["age"])
    for student_id, student_data in students.items()
]
print("Список пар «ID студента — возраст»: {0}".format(list_pairs_id_age))

interests, length_surnames = get_data_interests_surnames(students)
print("Полный список интересов всех студентов: {0}".format(interests))
print("Общая длина фамилий студентов: {0}".format(length_surnames))
