class Student:
    count = 0
    students = []
    @classmethod
    def print(cls):
        print("------학생 목록------")
        print("이름", "총점", "평균", sep = "\t")
        for student in cls.students:
            print(str(student))
        print()

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        Student.students.append(self)
        print("{}번쨰 학생이 생성되었습니다.".format(Student.count))

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    def get_avg(self):
        return self.get_sum() / 4
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_avg())

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __ele__(self, value):
        return self.get_sum() <= value.get_sum()

Student("윤인성", 87, 98, 88, 95),    
Student("연하진", 92, 98, 96, 98),
Student("구지연", 76, 96, 94, 90),
Student("나선주", 98, 92, 96, 92),
Student("윤아린", 95, 98, 98, 98),
Student("윤명월", 64, 88, 92, 92)

student_a = Student("윤인성", 87, 98, 88, 95)
student_b = Student("연하진", 92, 98, 96, 98)

Student.print()
print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a > student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a < student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)
print()
print("현재 생성된 총 학생 수는 {} 명입니다.".format(Student.count))