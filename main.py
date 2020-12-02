# Hashriya-Undergrounds
# Intro
choice = input("Welcome to the land of the rising sun,Do you wish to start?(yes/no)").lower().strip()
if choice.lower().strip() == "yes":
    print("IKUZO, LETS BEGIN")
else:
    print("Too bad. Welcome to the wangan sen ;)")

playa = input("Quick question.... What is your name?")

# Selecting a Japanese car Manufactuer.  I'll add some European cars in a future update.  Time of Day(TOD)
JDM = input("Okay "+playa+"! Please select a Japanese Car Manufactuer(Honda/Mazda/Mistubushi/Nissan/Subaru/Toyota)")
if JDM == "Honda":
    JDM = input("Please select which Honda  model you wish to select. Honda( S2000, Nsx(NC1),EK9)")
elif JDM == "Toyota":
    JDM = input("Please select which Toyota you wish to select. Toyota(Supra 2.5 GT TT,Supra RZ,Soarer 2.5 GT TT,MR2)")
if JDM == "Mazda":
    JDM = input("Please select which Mazda model  you wish to select. Mazda(RX 7 FD35,RX 7 FC35,Miata mx5 NA,Miata mx5 NB,RX 8) ")
elif JDM == "Mistubushi":
    JDM = input("Please select which Mistubushi model you wish to select. Mistubushi(GTO TT, FTO, Lance Evo iii, Lance evo VI, Lance Evo VIII)")
if JDM == "Nissan":
    JDM = input("Please select which Nissan model you wish to select. Nissan(Skyline R34, Skyline R33, Skyline R32, Silvia S15, Fairlady Z 300ZX, Fairlady Z.L, Fairlady Z 350Z)")
elif JDM == "Subaru":
    JDM = input("Please select which Subaru model you wish to select. Subaru(Impreza WRX STI, Impreza WRX STI Version VI, Subarau BRZ)")

TOD = input("Select the time of day you wish to drive.  (Dawn, AfterNoon, Evening, Midnight)")
# The beggining of the game.  First choices(Well not really ;)
# City/course selection
city = input(" Wonderful choice "+playa+". I see you got style..Proceed to select a course(C1 outer,Bayshore route) ")
if city == "C1 outer":
    city = input("You have just left Fujiwaera's Tuning shop in Yokohama, and is now on the way to Daikoku parking lot. You arrive and meet the bois. Your homie hiroshi ask,"
     "hey "+playa+", wanna go for a midnight run?(Stay/Go)")
if city == "Go":
    city = input("Bet. But which route should we take tho. Either the(Bayshore route/Daikoku route)?")


# To those who chose the Bayshore route option
else:
    city = input("You are now on the infamous Bayshore route, known for the legendary Midnight Club. While cruising in your "+JDM+" , you see another Hashiriya.  Do you wish to challenge him?(yes/no)")
if city.lower().strip() == "yes":
    print("ITS ON, the last one to Yokohama bay bridge loses. Ikuzo")

else:
    print("Its still on, the Hashiriya still flickers his headlights. Challenge still stands, last one to Yokohama bay bridge loses.")


# Next part of the game
choice = input("A intense head to head in the Haneda North tunnel at almost 300 kmh, but once you exit, you see a r34 police car! Do you wanna(pull over/speed away)")
if choice.lower().strip() == "speed away":
    print("You hear, Unit 4, possible street racers, requesting backup.  Stop your vehicle.  Ah shit, the chase is on.")
    choice = input("You are now being chased by the police, but you see two exits,exit 7 & 8.  Exit 7 leads to Yokohama bay bridge. Exit 8 leads to Haneda airport. I choose(exit 7/exit 8)")
    if choice.lower().strip() == "exit 7":
        print("Ehhh, he gave me the slip. I've lost him, breaking pursuit.  You cross yokohama bay bridge, and evade arrest, Noice..")
    else:
        print("Turn off you car, stay where you are!  You're busted.  Never go to a airport in a chase.  Game over..")

# Had to put this here, in order for game to end properly for this specific choice.
elif choice.lower().strip() == "pull over":
    print("You recieve a ticket of ¥10000 for speeding.  At least you still have your liscense.  Game over..")

# Asking user if they wish to restart the game(Adding feature that will automaticlly restart if you select yes)
choice = input("Do you wish to play again?(yes/no)")
if choice.lower().strip() == "yes":
    print("Just hit play ;)")
else:
    print("Thank you for playing my game.  Have a wonderful day:). Sayonara!!")

