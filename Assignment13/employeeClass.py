class Employee:
    def __init__(self, name="", idNumber=0, department="", position=""):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.position = position

    # Setters
    def setName(self, name):
        self.name = name

    def setIdNumber(self, idNumber):
        self.idNumber = idNumber

    def setDepartment(self, department):
        self.department = department

    def setPosition(self, position):
        self.position = position

    # Getters
    def getName(self):
        return self.name

    def getIdNumber(self):
        return self.idNumber

    def getDepartment(self):
        return self.department

    def getPosition(self):
        return self.position
