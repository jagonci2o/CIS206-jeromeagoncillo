from employeeClass import Employee

# Inherits from Employee Class
class basketballScout(Employee):
    def __init__(self, name="", idNumber=0, department="", position="", location=None, yearsExperience=0):
        super().__init__(name, idNumber, department, position)
        self.location = [str(r) for r in location] if isinstance(location, list) else ([str(location)] if location else [])
        self.yearsExperience = yearsExperience
        self.prospects = []

    # Overrides the 'getPosition' from Employee Class
    def getPosition(self): 
        return self.position

    # New Getters
    def getlocation(self):
        return self.location

    def getYearsExperience(self):
        return self.yearsExperience

    def getProspects(self):
        return self.prospects

    # 2 new methods that use methods from Employee
    def addProspect(self, player):
        self.prospects.append(player)

    def makeReport(self):
        report = f"\nHello Scout!\n"
        report += f"\nScouting Report done by {self.getName()} (ID: {self.getIdNumber()})\n"
        report += f"Department: {self.getDepartment()} \nPosition: {self.getPosition()}\n"
        report += f"Location: {', '.join(str(r) for r in self.getlocation())}\n"
        report += f"Years in the NBA: {self.getYearsExperience()}\n"
        report += "\nProspect Evaluation:\n"

        if not self.prospects:
            report += " No prospects evaluated.\n"
            return report
        
        report += "\n" + ("-" * 148)
        report += f"\n|{'Name':<20}|{'Position':<20}|{'Age':<20}|{'Athleticism':<20}|{'Jumpshot':<20}|{'NBA Readiness':<20}|{'Rating':<20}|"
        report += "\n" + ("-" * 148)

        for p in self.getProspects():
            rating = (p["athleticism"] + p["jumpshot"] + p["nbaReadiness"]) / 3
            report += f"\n|{p['name']:<20}|{p['position']:<20}|{p['age']:<20}|{p['athleticism']:<20}|{p['jumpshot']:<20}|{p['nbaReadiness']:<20}|{round(rating, 1):<20}|"
            report += "\n" + ("-" * 148)
                
        return report
