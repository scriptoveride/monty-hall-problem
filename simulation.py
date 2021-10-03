import random 

win = 0
lose = 0
i = 1

while i < 100:
    prizedoor = random.randint(1, 3)

    listofdoors = [1, 2, 3]
    print("winning door is " + str(prizedoor))
    print("what door do you want to chose. 1, 2 or 3?")
    playerdoor = random.randint(1, 3)
    print("you chose door " + str(playerdoor))

    listofdoors.remove(playerdoor)

    if playerdoor == prizedoor:
        otherdoor = random.choice(listofdoors)
        listofdoors.remove(otherdoor)
        print("door " + str(listofdoors[0]) + " has nothing behind it")
        print("do you want to stick with door " + str(playerdoor) + " or swap to door " + str(otherdoor))
        answer = "stay"

        if answer == "stay":
            print("YOU WIN")
            win+=1
        else:
            print("YOU LOSE")
            lose+=1

    else:
        listofdoors.remove(prizedoor)
        print("door " + str(listofdoors[0]) + " has nothing behind it")
        print("do you want to stick with door " + str(playerdoor) + " or swap to door " + str(prizedoor))
        answer = "stay"

        if answer == "stay":
            print("YOU LOSE")
            lose+=1
        else:
            print("YOU WIN")
            win+=1

    i += 1
    print("wins = " + str(win))
    print("losses = " + str(lose))
