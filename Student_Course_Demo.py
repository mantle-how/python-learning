class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self,course):
        self.courses.append(course)

    def list_courses(self):
        #print(self.courses) 這樣輸出會產生 [<__main__.Course object at 0x000001F7B36FCED0>]
        print(f"學生{self.name}選的課程是: \n")
        for course in self.courses:
            print(f"{course.name},{course.teacher}\n") #能使用course.name的關係是 後面測試時生成math_course裡存著Course物件
            #而這個物件在後面會被丟進來Student中的add_course中 所以可以合法使用Course中的變數了
        print("---------------------")




class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def list_students(self):
        #print(self.students) 這樣輸出會產生 [<__main__.Course object at 0x000001F7B36FCED0>]
        print(f"{self.name}的學生名單\n")
        for student in self.students:
            print(f"{student.name}(學號:{student.student_id})\n")
        print("---------------------")

    

# 建立課程
course_math = Course("數學", "林老師")
course_cs = Course("計算機概論", "蔡老師")

# 建立學生
student_amy = Student("Amy", "S001")
student_ben = Student("Ben", "S002")

# 學生選課
student_amy.add_course(course_math)
student_amy.add_course(course_cs)

student_ben.add_course(course_math)

# 課程加入學生
course_math.add_student(student_amy)
course_math.add_student(student_ben)

course_cs.add_student(student_amy)

# 查看學生的課表
student_amy.list_courses()
student_ben.list_courses()

# 查看課程的學生名單
course_math.list_students()
course_cs.list_students()