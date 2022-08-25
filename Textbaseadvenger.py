from time import sleep

yes_no = ["yes", "no"]
guard = ["Run", "Fight", "Bribe", "Goback", "Explore"]
res = " "

intro = """Welcome to my Hall complex or Mystery Hall.
Just hearing the name might not be challenging.
Each room doesn't look like anything.
However; don't give me the wrong answer
If you're wrong, you might lose without even realizing it.
Or may not be able to leave this room anymore."""
print(intro + "\n")

name = input("Please input your name before challenging: ")
print('\n')
sleep(1)
print("Yo !!!, " + name + ". Let's win in mystery room")
print("You find yourself on the edge of a dark room.")
print("Can you find your way through?\n")

while res not in yes_no:
    res = input("Ready to find way out?\n" + "yes / no >> ")
    if res == 'yes':
        print("Wow !!! Courageous, let's head into ROOM.")
    elif res == 'no':
        print("Ha ha ha, Cowardly, get stuck in this hall")
        quit()
    else:
        print("I misunderstand you. What do you mean? " + name)

while res not in guard:
    print("ENTRANCE HALL")
    print("They have a choice of two doors to go through.")
    res = input("What direction do you go?\n" + "Left / Right >> ")
    print(" ")
    if res == 'Left':
        print("GUARD ROOM")
        res = input("Meet a troll. Bribe him fight or run him\n" + "Run / Fight / Bribe >> ")
        print(" ")
        if res == 'Run':
            res = ""
            print("Oh no, return again !!!")
        elif res == 'Fight':
            print("LOSE THE FIGHT")
            print("They are smashed on the head and die.")
            print("LOSE")
            res = input("Replay or not\n" "Press 1 (yes) / 2 (no) >> ")
            print(" ")
            if res == "1":
                res = ""
            elif res == "2":
                print("Hahaaahaaaaa !!! See you again" + name + "\n")
                quit()

        elif res == 'Bribe':
            print("CHOICE OF CHESTS")
            res = input("The troll wandom off. There are two chests: one gold; one silver\n" + "Gold / Silver >> ")
            print(" ")
            if res == 'Gold':
                print("ACID TRAP")
                print("The player was greedy! Sprayed in the face with acid and dies horribly.")
                print("LOSE")
                res = input("Replay or not\n" "Press 1 (yes) / 2 (no) >> ")
                print(" ")
                if res == 1:
                    res = ""
                elif res == 2:
                    print("Hahaaahaaaaa !!! See you again" + name + "\n")
                    quit()

            elif res == 'Silver': 
                print("TREASURE")
                print("They find all of the shiny treasure!")
                print("Win")
                while res not in yes_no:
                    res = input("Enjoy? " + name + " : yes / no >> ")
                    print(" ")
                    if res == 'yes':
                        print("Thanks for playing " + name)
                    elif res == 'no':
                        print("Yeah I know, it just simple game thank you")
                    else:
                        print("I misunderstand you. What do you mean? " + name)
                    quit()

    elif res == 'Right':
        print("KITCHEN")
        res = input("Explore or go back the way you came\n" + "Explore / Goback >> ")
        print(" ")
        if res == 'Goback':
            res = ""
            print("Oh no, return again !!!")
        elif res == 'Explore':
            print("CAKE?")
            res = input("You find a cake. Do you wish to eat it?\n" + "Yes / No >> ")
            print(" ")
            if res == 'Yes':
                print("THE CAKE IS A LIFE")
                print("The cake was poisoned, but you die happy!")
                print("LOSE")
                res = input("Replay or not\n" "Press 1 (yes) / 2 (no) >> ")
                print(" ")
                if res == 1:
                    res = ""
                elif res == 2:
                    print("Hahaaahaaaaa !!! See you again" + name + "\n")
                    quit()
            else:
                res = ""
                print("Oh no, return again !!!")
    else:
        print("I misunderstand you. What do you mean? " + name)

