class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecture_eval(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_student = (f'Имя: {self.name}\n'
                       f'Фамилия: {self.surname}\n'
                        f'Средняя оценка за домашние задания: {self.grade_average()}\n'
                        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                        f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return some_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return self.grade_average() < other.grade_average()

    def grade_average(self):
        val = self.grades.values()
        val = list(val)
        grade = []
        i = 0
        for x in val[i]:
            grade.append(x)
            i += 1
        grade = list(map(int, grade))
        grade = sum(grade) / len(grade)
        return grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    age = 35
    lect_l = []

    def __str__(self):
        some_lecturer = (f'Имя: {self.name}\n'
                        f'Фамилия: {self.surname}\n'
                        f'Средняя оценка за лекции: {self.grade_average()}')
        return some_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.grade_average() < other.grade_average()

    def grade_average(self):
        val = self.grades.values()
        val = list(val)
        grade = []
        i = 0
        for x in val[i]:
            grade.append(x)
            i += 1
        grade = list(map(int, grade))
        grade = sum(grade) / len(grade)
        return grade


class Reviewer(Mentor):
    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_reviewer

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_rating_stud(stud_l, course):
    stud_course = []
    for st in stud_l:
        if course in st.courses_in_progress:
            stud_course.append(st)
    for obj in stud_course:
        for grade in obj.grades.values():
            grade = list(map(int, grade))
            grade = sum(grade) / len(grade)
    return grade


def average_rating_lect(lect_l, course):
    lec_course = []
    for lec in lect_l:
        if course in lec.courses_attached:
            lec_course.append(lec)
    for obj in lec_course:
        for grade in obj.grades.values():
            grade = list(map(int, grade))
            grade = sum(grade) / len(grade)
    return grade


stud_l= []
lect_l = []

student_1 = Student('Redrick', 'Schuhart', 'male')
student_1.finished_courses += ['Data Scientist', 'Java', 'Product Manager']
student_1.courses_in_progress += ['Python', 'Git']
stud_l.append(student_1)

student_2 = Student('Marina', 'Savchenko', 'female')
student_2.finished_courses += ['C++', 'Product Manager']
student_2.courses_in_progress += ['Python', 'Git', 'SMM-manager']
stud_l.append(student_2)

lecturer_1 = Lecturer('Segrey', 'Gubarev')
lecturer_1.courses_attached = ('Введение в программирование', 'Python', 'Git')
lect_l.append(lecturer_1)
lecturer_2 = Lecturer('Artyom', 'Cherniy')
lecturer_2.courses_attached = ('Git', 'Аналитика', 'Data Scientist', 'Python')
lect_l.append(lecturer_2)

reviewer_1 = Reviewer('Dmitry', 'Serov')
reviewer_1.courses_attached += ['Python', 'Git', 'Аналитика']

reviewer_2 = Reviewer('Victor', 'Vorobey')
reviewer_2.courses_attached += ['Введение в программирование', 'Data Scientist', 'Java']

student_1.lecture_eval(lecturer_1, 'Python', 8)
student_1.lecture_eval(lecturer_2, 'Python', 7)
student_2.lecture_eval(lecturer_1, 'Python', 8)
student_2.lecture_eval(lecturer_2, 'Python', 10)

reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 8)

print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)
print(student_1 < student_2)
print(student_1 > student_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)
print(f'Средняя оценка у студентов на курсе по Python: {average_rating_stud(stud_l, "Python")}')
print(f'Средняя оценка у лектроров на курсе по Python: {average_rating_lect(lect_l, "Python")}')
