# openining the file so that I can write the data in this. Syntax open(name_of_the_file, instruction).
# here instruction means what you want to do with the file.
import sys

def main():
   print("1) Read")
   print("2) Write")
   question = input("What do you want? Enter option number: ")
   if(question == "1"):
    Read()
   elif(question == "2"):
    Write()
   else:
     print("Invalid option selection. Try again! ") 

def Write():
  while True:
    name = input("What's your name? ")
    with open("names.txt","a") as file:
      file.write(f"{name}\n")
    again = input("continue? y/n: ")
    if(again == "n"):
      break
    else: continue
def Read():
  with open("names.txt","r") as file:
    lines = file.readlines()
  for line in lines:
    print(line,end= "")

if __name__ == "__main__":
  main()
