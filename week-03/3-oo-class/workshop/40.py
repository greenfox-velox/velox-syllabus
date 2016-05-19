the_infamous_godies = [
                {'name': 'Rezso', 'age': 9.5, 'candies': 2},
                        {'name': 'Gerzson', 'age': 10, 'candies': 1},
                                {'name': 'Aurel', 'age': 7, 'candies': 3},
                                        {'name': 'Zsombor', 'age': 12, 'candies': 5}
                                        ]

def get_all_candies_of_under_10(students):
    total_candies = 0
    for student in students:
        if student['age'] < 10:
           total_candies += student['candies']
    return total_candies


print(get_all_candies_of_under_10(the_infamous_godies))









