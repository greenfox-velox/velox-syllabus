students = [
		        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
			        {'name': 'Gerzson', 'age': 10, 'candies': 1},
				        {'name': 'Aurel', 'age': 7, 'candies': 3},
					        {'name': 'Zsombor', 'age': 12, 'candies': 5},
						        {'name': 'Olaf', 'age': 12, 'candies': 7},
							        {'name': 'Teodor', 'age': 3, 'candies': 2}
								]


def get_rich_kid_count(students):
    rich_students = 0
    for student in students:
        if student['candies'] > 4:
            rich_students += 1
    return rich_students

print(get_rich_kid_count(students))






