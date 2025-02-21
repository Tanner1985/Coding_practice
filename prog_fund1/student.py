class Student:
    
    def __init__(self, name, ID, GPA, expectGrade,fullOrPart):
        self.__name = name
        self.__ID = ID
        self.__GPA = GPA
        self.__expectGrade = expectGrade
        self.__fullOrPart = fullOrPart

    def setName(self):
        self.__name = input('Please enter the students name: ')
    def setID(self):
        self.__ID = input('Please enter the students ID: ')
    def setGPA(self):
        self.__GPA = input('Please enter the students GPA: ')
    def setExpecGrade(self):
        self.__expectGrade = input('Please enter the students expected grade: ')
    def setFullorPart(self):
        self.__fullOrPart = input('Please enter if the student is full or part time: ')
    def getName(self):
        return self.__name
    def getID(self):
        return self.__ID
    def getGPA(self):
        return self.__GPA
    def getExpecGrade(self):
        return self.__expectGrade
    def getFullorPart(self):
        return self.__fullOrPart

    