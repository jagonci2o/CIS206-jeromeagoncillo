from employeeClass import Employee

member1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
member2 = Employee("Mark Jones", 39119, "IT", "Programmer")
member3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

employees = [member1, member2, member3]

print("\nEMPLOYEE LIST:\n")
print(f"{'Name':<20} {'ID':<20} {'Department':<20} {'Position':<20}")
for emp in employees:
    print(f"{emp.getName():<20} {emp.getIdNumber():<20} {emp.getDepartment():<20} {emp.getPosition():<20}")


