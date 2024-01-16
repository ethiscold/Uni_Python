import random
MY
life = 7
x = []

for i in range(5):
    x.append(random.randint(1,3))

print(MY)
for i in range(len(x)):
    Guess = input("Guess a number in the array x between \n")    
    if(Guess == x[i]):
        print("You guessed the number at position" + i)
        break
    else:
        print("WRONG")
        life = life-1
    if (life == 0):
        break
        
