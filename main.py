class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.score = {}
        self.average_rating = 0


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.score:
                lecture.score[course] += [grade]
                lecture._Lecture__counter_score(lecture)
            else:
                lecture.score[course] = [grade]
                lecture._Lecture__counter_score(lecture)
            if lecture not in list_lecturers:
                list_lecturers.append(lecture)
        else:
            return 'Ошибка'

    def __counter_grade(self, student):
        list_1 = [value for value in student.grades.values()]
        list_2 = []
        for var in list_1:
            if type(var) == list:
                list_2.extend(var)
                student.average_grade = sum(list_2) / len(list_2)

    def comparison(self, student_one, student_two):
        if isinstance(student_one, Student) and isinstance(student_two, Student):
            if student_one.average_grade > student_two.average_grade:
                result = f'Лучший студент: \n{student_one.surname} {student_one.name} \nСредний бал за домашние задания: {student_one.average_grade}'
            elif student_one.average_grade < student_two.average_grade:
                result = f'Лучший студент: \n{student_two.surname} {student_two.name} \nСредний бал за домашние задания: {student_two.average_grade}'
            elif student_one.average_grade == student_two.average_grade:
                result = 'Студенты равны'
            else:
                result = 'Ошибка'
        print(result)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы:{self.finished_courses}'
        return res


class Lecture(Mentor):
    def __counter_score(self, lecture):
        list_1 = [value for value in lecture.score.values()]
        list_2 = []
        for var in list_1:
            if type(var) == list:
                list_2.extend(var)
                lecture.average_rating = sum(list_2) / len(list_2)

    def comparison(self, lecturer_one, lecturer_two):
        if isinstance(lecturer_one, Lecture) and isinstance(lecturer_two, Lecture):
            if lecturer_one.average_rating > lecturer_two.average_rating:
                result = f'Лучший лектор: \n{lecturer_one.surname} {lecturer_one.name} \nСредний бал за лекции: {lecturer_one.average_rating}'
            elif lecturer_one.average_rating < lecturer_two.average_rating:
                result = f'Лучший лектор: \n{lecturer_two.surname} {lecturer_two.name} \nСредний бал за лекции: {lecturer_two.average_rating}'
            elif lecturer_one.average_rating == lecturer_two.average_rating:
                result = 'Лекторы равны'
            else:
                result = 'Ошибка'
        print(result)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_rating}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student._Student__counter_grade(student)
            else:
                student.grades[course] = [grade]
                student._Student__counter_grade(student)
            if student not in list_students:
                list_students.append(student)
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


list_students = []


def avr_hw(course):
    list_scores = []
    for var_1 in list_students:
        for var_2 in var_1.grades:
            if var_2 == course:
                for var_3 in var_1.grades[var_2]:
                    list_scores.append(var_3)
    if sum(list_scores) > 0:
        res = print(f'Средняя оценка студентов за курс {course} : {sum(list_scores) / len(list_scores)}')
    else:
        res = print('По данному курсу у студентов нет оценок')

    return res


list_lecturers = []


def avr_lc(course):
    list_scores = []
    for var_1 in list_lecturers:
        for var_2 in var_1.score:
            if var_2 == course:
                for var_3 in var_1.score[var_2]:
                    list_scores.append(var_3)
    if sum(list_scores) > 0:
        res = print(f'Средняя оценка лекторов за курс {course} : {sum(list_scores) / len(list_scores)}')
    else:
        res = print('По данному курсу у лекторов нет оценок')

    return res


Lecturer_1 = Lecture('Иван', 'Петров')
Lecturer_1.courses_attached = ['Математика', 'Физика', 'Информатика']

Lecturer_2 = Lecture('Елисей', 'Иванов')
Lecturer_2.courses_attached = ['Наука', 'География', 'Языки']

rev_1 = Reviewer('Ирина', 'Наумова')
rev_1.courses_attached = ['Черчение', 'Архитектура', 'История', 'Математика', 'Информатика', 'География', 'Наука']

student_1 = Student('Никита', 'Полянский', 'муж')
student_1.courses_in_progress = ['Математика', 'Архитектура', 'Информатика', 'География']

student_2 = Student('Елена', 'Чашникова', 'жен')
student_2.courses_in_progress = ['Информатика', 'История', 'Наука']

student_3 = Student('Ирина', 'Капустина', 'жен')
student_3.courses_in_progress = ['Черчение', 'История', 'Архитектура', 'Наука', 'Информатика']

student_1.rate_lecture(Lecturer_1, 'Информатика', 5)
student_2.rate_lecture(Lecturer_1, 'Информатика', 4)
student_1.rate_lecture(Lecturer_1, 'Математика', 5)
student_2.rate_lecture(Lecturer_2, 'Наука', 1)
student_1.rate_lecture(Lecturer_2, 'География', 4)

rev_1.rate_hw(student_1, 'Математика', 5)
rev_1.rate_hw(student_1, 'Информатика', 4)
rev_1.rate_hw(student_1, 'География', 2)

rev_1.rate_hw(student_2, 'История', 5)
rev_1.rate_hw(student_2, 'Информатика', 5)
rev_1.rate_hw(student_2, 'Наука', 2)

rev_1.rate_hw(student_3, 'История', 2)
rev_1.rate_hw(student_3, 'Информатика', 3)
rev_1.rate_hw(student_3, 'Наука', 5)
rev_1.rate_hw(student_3, 'Архитектура', 4)
rev_1.rate_hw(student_3, 'Черчение', 3)

# print(rev_1)
# print(Lecturer_1)
# print(Lecturer_2)
# print(student_1)
# print(student_2)
# student_1.comparison(student_1, student_2)
# Lecturer_1.comparison(Lecturer_1, Lecturer_2)
#
# avr_hw('Информатика')
# avr_hw('География')
# avr_hw('История')
# avr_hw('Черчение')
# avr_hw('Архитектура')
#
# avr_lc('Информатика')
# avr_lc('География')
# avr_lc('История')
# avr_lc('Черчение')
# avr_lc('Архитектура')