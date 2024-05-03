class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = [0]

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0.0
        else:
            return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Студент: {self.name} {self.surname}nОценки: {self.grades}nСредний балл: {self.calculate_average_grade()}"


#Создаем обьект класса
student1 = Student("Антон, Петров")
student2 = Student("Владимир, Иванов")





