print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okey! let play quiz")

score = 0

answer = input("What is stand for CPU? " )

if answer.lower() == "central processing unit":
    print("Correct!")
    score = score + 1

else:
    print("Incorrect!")

answer = input("What is stand for GPU? " )

if answer.lower() == "graphical processing unit":
    print("Correct!")
    score = score + 1

else:
    print("Incorrect!")

answer = input ("What is stand for RAM? ")

if answer.lower() == "random accessing memory":
    print("Correct!")
    score = score + 1

else:
    print("Incorrect!")

answer = input("What is stand for ROM? ")

if answer.lower() == "read only memory":
    print("Correct!")
    score = score + 1

else:
    print("Incorrect")

print("You got "+str(score)+" in this quiz computition ")
print("You got "+str((score/4)*100)+"%")
