class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # Создание метода оценки лекторов для текущего класса (Задание № 2)
    def rate_lc(self, lecturer, course, grade): # Функция принимает на вход экземпляр класса Lecturer (т.е. оцениваемого лектора),
        # оцениваемыйф курс и оценку.

        # Условие ниже проверяет, принадлежит ли параметр lecturer классу Lecturer, записан ли экземпляр текущего класса на оцениваемый курс (т.е.
        # записан ли студент на курс, который он собирается оценить), закреплен ли курс за экземпляром класса Lecturer (т.е. преподает ли лектор
        # на курсе, который собирается оценить студент), а также является ли выставляемая оценка валидной (т.е. находится в пределах от 0 до 10)
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 0 <= grade <= 10:
            # вложенное условие сообщает программе, что в случае, если курс уже есть в списке тех, по которым лектор получил оценку,
            # тогда мы добавляем к списку оценок еще одну; в противном случае создаем новую запись в словаре оценок в формает {курс: оценка}
            if course in lecturer.grade_dict:
                lecturer.grade_dict[course] += [grade]
            else:
                lecturer.grade_dict[course] = [grade]
        else:
            return 'Ошибка'

    # Создаем метод, считающий среднюю оценку за домашние задания для экземпляров текущего класса (Задание № 3)
    def avg_grade_count(self):
        sum_grade = 0  # В данную переменную будем накапливать сумму оценок
        count = 0  # Счетчик количества полученных оценок
        for values in self.grades.values():
            for value in values:
                sum_grade += value
                count += 1
        self.avg_grade = sum_grade / count
        return self.avg_grade

    # Создаем метод сравнения средних оценок у лекторов. Метод будет вызван корректно в случае, если перед этим вызван метод, считающий средннюю оценку за лекции
    # При этом стоит учесть, что мы не должны иметь возможность сравнивать между собой представителей разных классов (Student и Lecturer). Учтем это в условии
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка - попытка сравнить разные классы!'
        else:
            return self.avg_grade < other.avg_grade

    # Создаем метод, меняющий print() в текущем классе. В нем используем циклы для подсчета средней оценки за ДЗ, а также выводим элементы списков как строки, эл-ты
    # которых разделены запятой (Задание № 3)
    def __str__(self):
        sum_grade = 0  # В данную переменную будем накапливать сумму оценок
        count = 0  # Счетчик количества полученных оценок
        for values in self.grades.values():
            for value in values:
                sum_grade += value
                count += 1
        avg_grade = sum_grade / count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    # Cоздаем метод, который позволит добавлять экземпляры класса Student в список, который понадобится для подсчета средней оценки за домашние задания по всем
    # студентам в рамках конкретного курса (Задание № 4)
    def add_to_students_list(self):
        students_list.append(self)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor): # Создаем дочерний класс (Задание № 1)
    # При помощи магического метода super() добавляем данному классу атрибуты родительского класса и собственный атрибут - словарь оценок (Задание № 2)
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_dict = {}

    # Создаем метод, считающий среднюю оценку за лекции для экземпляров текущего класса (Задание № 3)
    def avg_grade_count(self):
        sum_grade = 0  # В данную переменную будем накапливать сумму оценок
        count = 0  # Счетчик количества полученных оценок
        for values in self.grade_dict.values():
            for value in values:
                sum_grade += value
                count += 1
        self.avg_grade = sum_grade / count
        return self.avg_grade

    # Создаем метод, меняющий print() в текущем классе (Задание № 3)
    def __str__(self):
        sum_grade = 0  # В данную переменную будем накапливать сумму оценок
        count = 0  # Счетчик количества полученных оценок
        for values in self.grade_dict.values():
            for value in values:
                sum_grade += value
                count += 1
        avg_grade = sum_grade / count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {avg_grade}'
        return res

    # Создаем метод сравнения средних оценок у лекторов. Метод будет вызван корректно в случае, если перед этим вызван метод, считающий средннюю оценку за лекции
    # При этом стоит учесть, что мы не должны иметь возможность сравнивать между собой представителей разных классов (Lecturer и Student). Учтем это в условии (Задание № 3)
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка - попытка сравнить разные классы!'
        else:
            return self.avg_grade < other.avg_grade

    # Cоздаем метод, который позволит добавлять экземпляры класса Lecturer в список, который понадобится для подсчета средней оценки за лекции по всем
    # лекторам в рамках конкретного курса (Задание № 4)
    def add_to_lecturers_list(self):
        lecturers_list.append(self)

class Reviewer(Mentor): # Cоздаем дочерний класс (Задание № 1)

    # Создание метода оценки студентов для текущего класса (Задание № 2)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 0 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Создаем метод, меняющий print() в текущем классе (Задание № 3)
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

# Создаем функцию, которая будет использоваться для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (Задание № 4)

def count_course_avg_grade(students, course):
    all_course_grades = []
    for student in students:
        if course in student.grades.keys():
            all_course_grades += student.grades[course]

    sum_grade = 0
    count = 0

    for grade in all_course_grades:
        sum_grade += grade
        count += 1
    course_avg_grade = sum_grade / count

    print(course_avg_grade)

# Создаем функцию, которая будет использоваться для подсчета средней оценки за лекции по всем лекторам в рамках конкретного курса (Задание № 4)

def count_course_avg_grade(lecturers, course):
    all_course_grades = []
    for lecturer in lecturers:
        if course in lecturer.grade_dict.keys():
            all_course_grades += lecturer.grade_dict[course]

    sum_grade = 0
    count = 0

    for grade in all_course_grades:
        sum_grade += grade
        count += 1
    course_avg_grade = sum_grade / count

    print(course_avg_grade)

# Полевые испытания

some_student_1 = Student('Amir', 'Sadaqa', 'male') # создаем первого студента
some_student_1.courses_in_progress.append('Python') # добавляем первый курс в список курсов, которые проходит студент
some_student_1.courses_in_progress.append('Git') # добавляем второй курс в список курсов, которые проходит студент
# print(some_student_1.courses_in_progress) # посмотрим, как выглядит список курсов, которые проходит студент
# print()
some_student_1.finished_courses.append('Введение в программирование') # добавляем курс в завершенные студентом
# print(some_student_1.finished_courses) # посмотрим, как выглядит список курсов, которые завершил студент
# print()

some_reviewer_1 = Reviewer('Oleg', 'Byligin') # cоздаем первого проверяющего
some_reviewer_1.courses_attached.append('Python') # добавляем первый курс в список курсов, которые закреплены за проверяющим
some_reviewer_1.courses_attached.append('Git') # добавляем второй курс в список курсов, которые закреплены за проверяющим
# print(some_reviewer_1.courses_attached)  # посмотрим, как выглядит список курсов, которые проверяет проверяющий
# print()

some_reviewer_1.rate_hw(some_student_1, 'Python', 9) # поставим первую оценку студенту за ДЗ в рамках курса Python
# print(some_student_1.grades) # проверим, как выглядит словарь студента со списком оценок за ДЗ
# print()
some_reviewer_1.rate_hw(some_student_1, 'Python', 8)
# print(some_student_1.grades) # проверим, как теперь выглядит словарь студента со списком оценок за ДЗ
# print()
# some_reviewer_1.rate_hw(some_student_1, 'Python', 11) # проверим, что будет если выставить студенту невалидную оценку
# print(some_student_1.grades) # увидим, что словарь оценок студента за ДЗ не изменился
# print()

# Далее выполним действия по аналогии
some_reviewer_1.rate_hw(some_student_1, 'Git', 10)
some_reviewer_1.rate_hw(some_student_1, 'Git', 9)
# print(some_student_1.grades)
# print()

# Посчитаем среднюю оценку за ДЗ у студента и выведем ее на экран для удобства
# print(some_student_1.avg_grade_count())
# print()

# Выведем на экран студента
# print(some_student_1)
# print()

# Выведем на экран проверящего
# print(some_reviewer_1)
# print()

# Теперь проверим, работает ли сравнение среднего балла студентов. Для этого создадим несколько аналогичных действий

some_student_2 = Student('Ekaterina', 'Moshcheva', 'female')
some_student_2.courses_in_progress.append('Python')
some_student_2.courses_in_progress.append('Spanish')
# print(some_student_2.courses_in_progress)
# print()

some_reviewer_1.rate_hw(some_student_2, 'Python', 8)
some_reviewer_1.rate_hw(some_student_2, 'Python', 7)
# print(some_student_2.grades)
# print()

some_reviewer_2 = Reviewer('Irina', 'Victorova')
some_reviewer_2.courses_attached.append('Spanish')
some_reviewer_2.rate_hw(some_student_2, 'Spanish', 10)
some_reviewer_2.rate_hw(some_student_2, 'Spanish', 9)
# print(some_student_2.grades)
# print()

# Проверим, может ли второй проверяющий поставить первому студенту оценку по курсу Spanish
# print(some_reviewer_2.rate_hw(some_student_1, 'Spanish', 5))
# print()
# print(some_student_1.grades)
# print()
# print() # видим, что метод вернул ошибку, т.к. испанский не входит в список курсов, которые проходит первый студент, а словарь с оценками студента остался без изменений
# print()

# Посчитаем средний балл за ДЗ для второго студента и для удобства вызовем его на экран
# print(some_student_2.avg_grade_count())
# print()

# Выведем на экран второго студента и второго проверяющего
# print(some_student_2)
# print()
# print(some_reviewer_2)
# print()

# А теперь сделаем сравнение средней оценки за ДЗ для студента_1 и студента_2. Чтобы метод сработал корректно, необходимо посчитать средний балл для обоих (выедем его на экран для удобства)

# print(some_student_1.avg_grade_count())
# print()
# print(some_student_2.avg_grade_count())
# print()
# print(some_student_1 < some_student_2)

# Теперь создадим экземпляры класса Lector

some_lecturer_1 = Lecturer('Oleg', 'Byligin')
some_lecturer_2 = Lecturer('Alena', 'Batitskaya')

some_lecturer_1.courses_attached.append('Python')
some_lecturer_2.courses_attached.append('Git')
some_lecturer_2.courses_attached.append('Spanish')

# Студенты ставят оценки лекторам

some_student_1.rate_lc(some_lecturer_1, 'Python', 10)
some_student_1.rate_lc(some_lecturer_2, 'Git', 10)
some_student_2.rate_lc(some_lecturer_2, 'Spanish', 9)

# Посмотрим, как выглядят словари с оценками преподавателей

# print(some_lecturer_1.grade_dict)
# print()
# print(some_lecturer_2.grade_dict)
# print()

# Попробуем выполнить бессмысленное с точки зрения програаммы действие: например, пусть студент_1 попробует поставить лектору_2 оцену по испанскому

# print(some_student_1.rate_lc(some_lecturer_2, 'Spanish', 5)) # видим, что метод вернет ошибку, т.к. студент_1 не изучает испанский
# print()

# Выедем на экран лекторов
# print(some_lecturer_1)
# print()
# print(some_lecturer_2)
# print()

# Теперь сравним лекторов по средней оценке. Чтобы метод сработал корректно, необходимо посчитать средний балл для обоих (выедем его на экран для удобства)
# print(some_lecturer_1.avg_grade_count())
# print()
# print(some_lecturer_2.avg_grade_count())
# print()
# print(some_lecturer_1 < some_lecturer_2)
# print()

# А теперь попробуем сравнить эземпляры разных классов, т.е. студентов с лекторами, по средней оценке

# print(some_student_1 < some_lecturer_2)
# print()
# print(some_student_2 < some_lecturer_1)
# print()
# print() # увидим, что метод вернет ошибку, т.к. мы запретили программе делать подобные сравнения

# Теперь посчитаем среднюю оценку за домашние задания по всем студентам в рамках конкретного курса
# Для этого инициализируем пустой список students_list и вызовем нужный метод для добавления в него студентов

students_list = []

some_student_1.add_to_students_list()
some_student_2.add_to_students_list()
# print(students_list)
# print()

# Теперь вызовем ф-цию для расчета среднюю оценку для всех лекторов по конкретному курсу
# Для этого инициализируем пустой список lecturers_list и вызовем нужный метод для добавления в него лекторов

lecturers_list = []

some_lecturer_1.add_to_lecturers_list()
some_lecturer_2.add_to_lecturers_list()

# some_student_2.rate_lc(some_lecturer_1, 'Python', 2) # добавим еще одну оценку лектору для наглядности

# print(some_lecturer_1.grade_dict)
# print()
# print(some_lecturer_2.grade_dict)
# print()

# count_course_avg_grade(lecturers_list, 'Python')
# count_course_avg_grade(lecturers_list, 'Git')
# count_course_avg_grade(lecturers_list, 'Spanish')

# Теперь посчитаем среднюю оценки за домашние задания по всем студентам в рамках конкретного курса
# Для этого инициализируем пустой список students_list и вызовем нужный метод для добавления в него студентов

