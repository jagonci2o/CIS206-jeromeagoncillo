import tkinter as tk
from tkinter import simpledialog, messagebox

class EmployeeGUI:
    def __init__(self, name="", id=0, department="", position=""):
        self.name = name
        self.id = id
        self.department = department
        self.position = position

    @classmethod
    def nameAndId(cls, name, id):
        return cls(name, id, "", "")

    @classmethod
    def default(cls):
        return cls("", 0, "", "")

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getDepartment(self):
        return self.department

    def getPosition(self):
        return self.position

    def setName(self, name):
        self.name = name

    def setId(self, id):
        self.id = id

    def setDepartment(self, department):
        self.department = department

    def setPosition(self, position):
        self.position = position


# Begin GUI App
def main():
    emp = EmployeeGUI.default()
    employees = []  # List to store added employees

    def enterName():
        name = simpledialog.askstring("Input", "Enter employee name:")
        if name is not None:
            emp.setName(name)

    def enterId():
        id = simpledialog.askstring("Input", "Enter employee ID:")
        if id and id.isdigit():
            emp.setId(int(id))

    def enterDepartment():
        dept = simpledialog.askstring("Input", "Enter employee department:")
        if dept is not None:
            emp.setDepartment(dept)

    def enterPosition():
        position = simpledialog.askstring("Input", "Enter employee position:")
        if position is not None:
            emp.setPosition(position)

    def displayInfo():
        # Show current employee info
        info = (
            f"Name: {emp.getName()}\n"
            f"ID: {emp.getId()}\n"
            f"Department: {emp.getDepartment()}\n"
            f"Position: {emp.getPosition()}\n"
        )
        messagebox.showinfo("Employee Information", info)

    def addEmployeeToList():
        # Add current employee to the list and display name in the visual list of employees
        if emp.getName() == "" or emp.getId() == 0:
            messagebox.showwarning("Missing Info", "Please enter at least Name and ID.")
            return
        new_emp = EmployeeGUI(emp.getName(), emp.getId(), emp.getDepartment(), emp.getPosition())
        employees.append(new_emp)
        # Show employee names in the visual list of employees
        listbox.insert(
            tk.END,
            f"{new_emp.getName()}"
        )

    def resetEmployee():
        # Clear current employee data
        emp.setName("")
        emp.setId(0)
        emp.setDepartment("")
        emp.setPosition("")
        messagebox.showinfo("Reset", "Current employee info has been cleared.")

    def showSelectedEmployee():
        # Show full info when selecting from the visual list of employees
        selection = listbox.curselection()
        if not selection:
            return
        index = selection[0]
        selected_emp = employees[index]
        info = (
            f"Name: {selected_emp.getName()}\n"
            f"ID: {selected_emp.getId()}\n"
            f"Department: {selected_emp.getDepartment()}\n"
            f"Position: {selected_emp.getPosition()}\n"
        )
        messagebox.showinfo("Selected Employee", info)

    root = tk.Tk()
    root.title("Employee Database")

    
    tk.Button(root, text="Enter Name", command=enterName).pack(pady=5)
    tk.Button(root, text="Enter ID", command=enterId).pack(pady=5)
    tk.Button(root, text="Enter Department", command=enterDepartment).pack(pady=5)
    tk.Button(root, text="Enter Position", command=enterPosition).pack(pady=5)
    tk.Button(root, text="Display Employee Information", command=displayInfo).pack(pady=5)

    
    tk.Button(root, text="Add to Employee List", command=addEmployeeToList).pack(pady=5)
    tk.Button(root, text="Reset Current Employee", command=resetEmployee).pack(pady=5)

    # Visual list of employees to display employee list
    listbox = tk.Listbox(root, width=80)
    listbox.pack(pady=10)

    tk.Button(root, text="Show Selected Employee Info", command=showSelectedEmployee).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
