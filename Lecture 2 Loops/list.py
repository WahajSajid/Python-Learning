
#we can create dictionary of data in the list like created below.  
#dictionary is a variable in the python which let us store data in the table form by providing them a key. 
students = [
    {"name":"Wahaj","profession":"Android Developer","language": "English"},
    {"name":"Haroon", "profession": "Web Developer", "language": "Urdu"},
    {"name": "basit","profession":None,"language":"Urdu"}
]
for student in students:
    print(student["name"], student["profession"], student["language"], sep=", " )