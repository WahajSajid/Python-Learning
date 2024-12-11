import csv
def main():
    loop = True
    while(loop):
      print("1) Write")
      print("2) Read")
      userChoise = input("What do you want? Enter choice number: ")
      if userChoise == "1":
          writeData()
          break
      elif userChoise == "2":
          ReadData()
          break
      else: 
         print("Invalid Choise! Try again")
         continue

def writeData():
   while True:
      name = input("What's your name? ")
      profession = input("What's your profession? ")
      with open("data.csv","a") as file:
         file_data = csv.DictWriter(file, fieldnames=["Name","Profession"])
         file_data.writerow({"Name":name,"Profession":profession})
      choice = input("you want to add another entry? y/n ")
      if choice == "n": break

def ReadData():
   data = []
   with open("data.csv") as file:
      file_data = csv.DictReader(file,fieldnames=["Name","Profession"])
      
      for row in file_data:
        data.append({"name":row['Name'],"profession":row['Profession']})

      for entity in sorted(data,key=lambda data: data["name"]):
        print(f"{entity['name']} is a {entity['profession']}")

main()
      