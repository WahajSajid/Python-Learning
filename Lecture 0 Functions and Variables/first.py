#print your name
name = input("Enter your name: ").strip().title() #"strip()" will remove the spaces from beginning and ending of string and "title()" will captilize the first letters of all the words in the string 
#Split the user's name into first and second name
firstName, secondName = name.split(" ")
print("Hello" , firstName )



