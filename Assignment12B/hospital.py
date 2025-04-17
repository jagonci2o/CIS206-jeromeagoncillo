from patientClass import Patient 
from procedureClass import Procedure 

patient = Patient(
   "Lebron", "Raymone", "James",
   "623 Lakeshow Dr", "Akron", "OH", "49137",
   "777-573-8124", "Luka Doncic", "303-547-9382"
)

procedure1 = Procedure("Physical Exam", "Today's date", "Dr. Irvine", 250.00)
procedure2 = Procedure("X-ray", "Today's date", "Dr. Jamison", 500.00)
procedure3 = Procedure("Blood test", "Today's date", "Dr. Smith", 200.00)

procedures = [procedure1, procedure2, procedure3]

print("\nPATIENT INFO:\n")
print("Name:", patient.getFullName())
print("Address:", patient.getAddress())
print("Phone:", patient.getPhone())
print("Emergency Contact:", patient.getEmergencyContact())

print("\nPROCEDURES:\n")
totalCharge = 0
for index, proc in enumerate(procedures, start=1):
   print(f"Procedure #{index}:")
   print(f"Procedure name: {proc.getProcedureName()}")
   print(f"Date: {proc.getDate()}")
   print(f"Practitioner: {proc.getPractitioner()}")
   print(f"Charge: ${proc.getCharge():.2f}\n")
   totalCharge += proc.getCharge()

print(f"Total Charge: ${totalCharge:.2f}\n")

