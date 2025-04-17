class Procedure:
    def __init__(self, procedureName, date, practitioner, charge):
        self.procedureName = procedureName
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    # Accessors
    def getProcedureName(self):
        return self.procedureName

    def getDate(self):
        return self.date

    def getPractitioner(self):
        return self.practitioner

    def getCharge(self):
        return self.charge
