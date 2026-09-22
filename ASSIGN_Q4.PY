students = [
	("Arun", 82),
	("Bala", 65),
	("Chitra", 91),
	("Divya", 74),
	("Esha", 88),
]


# Straightforward solution
def highest_mark_basic(students):
	"""Find the highest mark by sorting a copy of the list first."""
	if not students:
		return None
	sorted_students = sorted(students, key=lambda student: student[1])
	return sorted_students[-1]


def sort_students_basic(students):
	"""Return students sorted from lowest to highest mark."""
	return sorted(students, key=lambda student: student[1])


def search_student_basic(students, name):
	"""Search for a student using a linear scan."""
	for student_name, mark in students:
		if student_name == name:
			return (student_name, mark)
	return None


# Improved solution after removing unnecessary work
def highest_mark_improved(students):
	"""Find the highest-mark student in one pass, without sorting."""
	if not students:
		return None
	return max(students, key=lambda student: student[1])


def sort_students_improved(students):
	"""Use Python's efficient built-in sort implementation."""
	return sorted(students, key=lambda student: student[1])


def build_student_index(students):
	"""Build a dictionary for fast repeated searches by name."""
	return {name: mark for name, mark in students}


def search_student_improved(student_index, name):
	"""Look up a student by name in constant average time."""
	if name not in student_index:
		return None
	return (name, student_index[name])


if __name__ == "__main__":
	student_index = build_student_index(students)

	print("Basic highest mark:", highest_mark_basic(students))
	print("Improved highest mark:", highest_mark_improved(students))
	print("Sorted students:", sort_students_improved(students))
	print("Basic search for Divya:", search_student_basic(students, "Divya"))
	print("Improved search for Divya:", search_student_improved(student_index, "Divya"))

	print("\nTime complexity comparison:")
	print("Highest mark - basic: O(n log n), improved: O(n)")
	print("Sorting - basic and improved: O(n log n)")
	print("Name search - basic: O(n) per search")
	print("Name search - improved: O(n) to build the index, then O(1) average per search")
