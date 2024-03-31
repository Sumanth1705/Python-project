print("Welcome to my Computer quiz")
User_name = input("Enter your Name: ").upper()
playing = input("Do you want to play?\n")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("Which built-in function is used to sort a list in Python? ")
if answer.lower() == "sorted":
    print('Correct!')
    score +=1
else:
    print("Incorrect")

answer = input("Which statement is used to terminate the loop in Python?")
if answer.lower() == "break":
    print('Correct!')
    score +=1
else:
    print("Incorrect")
    
answer = input("What method is used to add an element to the end of a list in Python? ")
if answer.lower() == "append":
    print('Correct!')
    score +=1
else:
    print("Incorrect")
    
answer = input("What is the data structure used to store key-value pairs in Python? ")
if answer.lower() == "dictionary":
    print('Correct!')
    score +=1
else:
    print("Incorrect")
    
answer = input("What keyword is used to define a function in Python? ")
if answer.lower() == "def":
    print('Correct!')
    score +=1
else:
    print("Incorrect")
    
answer =input("What type of loop is used when the number of iterations is known?")
if answer.lower() == "for":
    print('Correct!')
    score +=1
else:
    print("Incorrect")
    
print("You got "+ str(score) + " questions Correct")
print("You got "+ str((score /6)*100) +"%.")
    