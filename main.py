import random
from utility import gameWin
while True:
 print("Computer Turn: Snake(s) Water(w) or Gun(g)")
 randNo = random.randint(1,3)
 if randNo == 1:
     computer = 's'
 elif randNo == 2:
    computer ='w'
 elif randNo == 3:
    computer ='g'

 name = input("Your Turn: Snake(s) Water(w) or Gun(g)?  ")
 a = gameWin(computer, name)

 print(f"Computer choose {computer}")
 print(f"you choose {name}")

 if a == None:
    print("The game is a tie!")
 elif a:
    print("You Win!")
 else:
    print("You Lose!")
 print("Type enter to continue with another game")
 option = input("Wanna quit? Enter q: ")
 if option == "q":
    break