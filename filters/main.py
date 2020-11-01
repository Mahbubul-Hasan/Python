grades = ['A', 'B', 'C', 'D', 'F']
filter_grades = []


def remove_fails(grade):
    return grade != 'F'


# ------------------------
for grade in grades:
    if grade != 'F':
        filter_grades.append(grade)
print(filter_grades)
# ------------------------
print(list(grade for grade in grades if grade != 'F'))
# -----------filter-------------
print(list(filter(remove_fails, grades)))
# -----------filter-------------
