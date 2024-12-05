import csv

name = input("What's your name? ")
profession = input("What'your profession? ")
with open("students.csv","a") as file:
    writer  = csv.DictWriter(file,fieldnames=["Name","Profession"])
    writer.writerow({"Name":name,"Profession":profession})
