class Student():
    def __init__(self, name, Class, id):
        self.name = name; self.Class = Class; self.id = id

    def __repr__(self): # this is class representation
        return f"name: {self.name}, class : {self.Class} id: {self.id}"

class Teacher():
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) -> str:
        return f"{self.name}, subject: {self.subject} id: {self.id} "
    




class School():
    def __init__(self,  name):
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self,name, subject):
        id   = len(self.teachers) + 101
        new_teacher = Teacher(name,subject, id)
        self.teachers.append(new_teacher)

    def add_student(self, name, Class):
        id = len(self.students) + 1

        new_student = Student(name,Class,id)
        self.students.append(new_student)
    # now representation

    def __repr__(self) -> str:
        print()
        print(f"'''''''Welcome to {self.name} ''''''''")
        print("''''''''' Our teachers are ''''''''''''")
        for teacher in self.teachers:
            print(teacher)

        print("")

        print("''''''''''''Our Students are ''''''''''''")

        for student in self.students:
            print(student)

        return ""
        


Nautara_ABL = School("Nautara ABL High Scholl")
Nautara_ABL.add_teacher("Pulin Bihari", "Bangla Grammar")

Nautara_ABL.add_teacher("Monju_Ara_Begum", "English Grammar and ICT")
Nautara_ABL.add_teacher("Jahangir Alam", "English -1")
Nautara_ABL.add_teacher("Abdur Rohim", "Islam and ")
Nautara_ABL.add_teacher("Jodunath Ray", "Biology")
Nautara_ABL.add_teacher("Jodunath Ray", "Chemistry")
Nautara_ABL.add_teacher("Asaduzzaman Asad", "Physics")
Nautara_ABL.add_teacher("Nasrin Akter", "Bangladesh and Global Studies")
Nautara_ABL.add_teacher("Komir Uddin", "Bangla-1")


Nautara_ABL.add_student("Morsalin Islam", 10)
Nautara_ABL.add_student("Motiur Rahman", 10)
Nautara_ABL.add_student("Rukunuzzaman", 10)
Nautara_ABL.add_student("Abu-Taher", 10)
Nautara_ABL.add_student("Nibir", 10)
Nautara_ABL.add_student("Al-Amin", 10)

print(Nautara_ABL)

