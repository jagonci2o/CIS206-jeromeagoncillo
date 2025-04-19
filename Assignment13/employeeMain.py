from employeeClass import Employee
from bballHeadScout import basketballScout

member1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
member2 = Employee("Mark Jones", 39119, "IT", "Programmer")
member3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

employees = [member1, member2, member3]

print("\nEMPLOYEE LIST:\n")
print("-" * 85)
print(f"|{'Name':<20}|{'ID':<20}|{'Department':<20}|{'Position':<20}|")
print("-" * 85)
for emp in employees:
    print(f"|{emp.getName():<20}|{emp.getIdNumber():<20}|{emp.getDepartment():<20}|{emp.getPosition():<20}|")
    print("-" * 85)

"""
The following shows the inherited class works properly by instantiating
that class, adding data to it and displaying the data using the 
class methods
"""

name = "Mike Stauffer"
idNumber = 442237
department = "Chicago Bulls"
position = "College Scout"
city = "Fort Lauderdale"
state = "Florida"
location = f"{city}, {state}"
yearsExperience = 23

scout = basketballScout(name, idNumber, department, position, location, yearsExperience)

players = [
    {
        "name": "Asa Newell",
        "position": "Forward",
        "age": 19,
        "athleticism": 9,
        "jumpshot": 7,
        "nbaReadiness": 9
    },
    {
        "name": "Tahaad Pettiford",
        "position": "Guard",
        "age": 20,
        "athleticism": 7,
        "jumpshot": 8,
        "nbaReadiness": 8
    },
    {
        "name": "Walter Clayton Jr.",
        "position": "Guard",
        "age": 22,
        "athleticism": 8,
        "jumpshot": 9,
        "nbaReadiness": 7
    }
]

# Adds all the players
for player in players:
    scout.addProspect(player)

# Prints the final report
print(scout.makeReport() + "\n")
