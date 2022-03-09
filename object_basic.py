students = [
    {"name":"윤인성", "korean":87, "math":98, "english":88, "science":95},
    {"name":"연하진", "korean":92, "math":98, "english":96, "science":98},
    {"name":"구지연", "korean":76, "math":96, "english":94, "science":90},
    {"name":"나선주", "korean":98, "math":92, "english":96, "science":92},
    {"name":"윤아린", "korean":95, "math":98, "english":98, "science":98},
    {"name":"윤명월", "korean":64, "math":88, "english":92, "science":92}
    ]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_avg = score_sum / 4
    print(student["name"], score_sum, score_avg, sep="\t")
print()

def create_student(name, korean, math, english, science):
    return {
        "name" : name, "korean" : korean, "math" : math,\
            "english" : english, "science" : science
    }
students = [
    create_student("윤인성", 87, 98, 88, 95),    
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]
print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_avg = score_sum / 4
    print(student["name"], score_sum, score_avg, sep="\t")
print()

def create_student2(name, korean, math, english, science):
    return {
        "name" : name, "korean" : korean, "math" : math,\
            "english" : english, "science" : science
    }
def student_get_sum(student):
    return student["korean"] + student["math"] +\
        student["english"] + student["science"]
def student_get_avg(student):
    return student_get_sum(student) / 4
def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_avg(student)
    )
students2 = [
    create_student2("윤인성", 87, 98, 88, 95),    
    create_student2("연하진", 92, 98, 96, 98),
    create_student2("구지연", 76, 96, 94, 90),
    create_student2("나선주", 98, 92, 96, 92),
    create_student2("윤아린", 95, 98, 98, 98),
    create_student2("윤명월", 64, 88, 92, 92)
]
print("이름", "총점", "평균", sep="\t")
for student in students2:
    print(student_to_string(student))