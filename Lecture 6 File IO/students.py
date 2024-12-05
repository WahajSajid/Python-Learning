import csv
def main():
  
  students = []
  with open("students.csv") as file:
    reader = csv.reader(file)
    for name,profession in reader:
      students.append({"name":name,"profession":profession})
  for student in sorted(students,key = lambda student:student["name"]):
    print(f"{student['name']} is a {student['profession']}")

main()