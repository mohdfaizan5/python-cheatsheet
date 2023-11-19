#PLATFORM THAT CONNECTS TEACHER STUDENTS SENIERS ALUMINIES AND PROMOTES TEAM WORK

class Student:
    def __init__(self, name, std, dob) -> None:
        self.name = name
        self.std = std
        self.dob = dob
    
    def __str__(self) -> str:
        return self