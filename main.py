print("Welcome to the Quiz!")
playing = input("Do you want to play? ")
if playing.lower() == "yes":
    print("Let's Start!")
    score = 0
else:
    quit()

answer = input("What Is the Capital of India? ")
if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What Is the Financial Capital of India? ")
if answer.lower() == "mumbai":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("National Animal of India? ")
if answer.lower() == "tiger":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("National Bird of India? ")
if answer.lower() == "peacock":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is India's currency called? ")
if answer.lower() == "rupee":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your Final Score is " + str(score))
print("You got " +str((score/5)*100)+"% in your quiz.")

