import random 

prizedoor = random.randint(1, 3)

listofdoors = [1, 2, 3]
print("winning door is " + str(prizedoor))
print("what door do you want to chose. 1, 2 or 3?")
playerdoor = int(input())
print("you chose door " + str(playerdoor))

listofdoors.remove(playerdoor)

if playerdoor == prizedoor:
    otherdoor = random.choice(listofdoors)
    listofdoors.remove(otherdoor)
    print("door " + str(listofdoors[0]) + " has nothing behind it")
    print("do you want to stick with door " + str(playerdoor) + " or swap to door " + str(otherdoor))
    answer = input()

    if answer == "stay":
        print("YOU WIN")
    else:
        print("YOU LOSE")

else:
   listofdoors.remove(prizedoor)
   print("door " + str(listofdoors[0]) + " has nothing behind it")
   print("do you want to stick with door " + str(playerdoor) + " or swap to door " + str(prizedoor))
   answer = input()

   if answer == "stay":
       print("YOU LOSE")
   else:
       print("YOU WIN")
