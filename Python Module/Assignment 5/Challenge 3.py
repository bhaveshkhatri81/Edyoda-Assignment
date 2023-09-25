# Challenge 3: Implement the Complete Student Class

class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getRollNumber(self):
        return self.__rollNumber
    
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

# Example usage:

student1 = Student()
student1.setName("Bhavesh")
student1.setRollNumber("86776")

print("Student Name:", student1.getName())
print("Student Roll Number:", student1.getRollNumber())
