class Student:
    def __init__(self,name,home):
        self.name = name
        self.home = home

    def __str__(self):
        return f"{self.name} is from {self.home}"
    
    @property
    def home(self):
        return self._home
    
    @home.setter
    def home(self,home):
        if home  != "Big home":
            raise ValueError("Invalid Home")
        self._home = home





def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    home = input("Home: ")
    try: 
      return Student(name,home)
    except:
        return Student("Wahaj","Big home")

if __name__ == "__main__":
    main()