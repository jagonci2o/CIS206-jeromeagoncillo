class Patient:
    def __init__(self, firstName, middleName, lastName, address, city, state, zipCode, phone, emergencyContactName, emergencyContactPhone):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.phone = phone
        self.emergencyContactName = emergencyContactName
        self.emergencyContactPhone = emergencyContactPhone

    # Accessors
    def getFullName(self):
        return f"{self.firstName} {self.middleName} {self.lastName}"

    def getAddress(self):
        return f"{self.address}, {self.city}, {self.state} {self.zipCode}"

    def getPhone(self):
        return self.phone

    def getEmergencyContact(self):
        return f"{self.emergencyContactName} {self.emergencyContactPhone}"
