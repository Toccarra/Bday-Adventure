name = input("Type your name: ")
print("Welcome", name, "to the adventure!")
print(" ")
answer = input("It's your birthday and your bestie has organized and exciting day for you! You bestie "
               "has given you very little information on what your day will be. Your bestie "
               "tells you to get dressed and meet outside. You don't know where you're going. Do you "
               "dress down with your favorite street style and sneakers? Or do you dress to impress, "
               "styling in your best gear? Type street for street style or impress for impressive style. ").lower()
print(" ")
if answer == "street":
    answer = input("Your bestie surprises you with tickets to today's music festival. You jump in the front"
                   "seat where you see your other good friend has already found a comfortable spot in the "
                   "back seat. Your good friend in the back suggests getting some breakfast before heading "
                   "to the festival. Do you head out to get breakfast or head straight to the festival. "
                   "Type breakfast to get breakfast or festival to head to the festival. ").lower()
    print(" ")
    if answer == "festival":
        answer = input("You and the crew made it just in time to get a front row spot to see the headliner "
                       "band. After the festival, you notice that your stomach is loudly grumbling. Your "
                       "bestie is anxious to take you to your next surprise. Do you insist on getting "
                       "some lunch at a new restaurant or do you cross your fingers hoping the next surprise "
                       "leads you to some real grub? Type lunch to go eat now or surprise to get taken to "
                       "your next surprise. ").lower()
        print(" ")
        if answer == "surprise":
            print("You and the crew pull up to your bestie's house. When your bestie unlocks the door, you "
                  "all go in together to be greeted by the surprise. A room full of your closest friends "
                  "jump out to yell 'surprise'. The surprise party is a hit and you enjoy your exciting "
                  "day after all.")

        elif answer == "lunch":
            print("You and the crew all get food poisoning. You head back home and are in bed with "
                  "the chunks for the rest of the day. You lose!")
        else:
            print("Not valid option. You Lose!")

    elif answer == "breakfast":
        print("You and the crew all get food poisoning. You head back home and are in bed with the "
              "chunks for the rest of the day. You lose! ")
    else:
        print("Not valid option. You Lose!")

elif answer == "impress":
    answer = input("You jump in the front seat where you see your other good friend has already found "
                   "a comfortable spot in the back seat. As you all are leaving, your bestie surprises "
                   "you with tickets to today's music festival. You look down at your feet and you are "
                   "wearing 4 inch heels to match your outfit. Do you decide to grin and bare it or tell "
                   "your bestie you must head back to change clothes? Type grin to grin and bare it or "
                   "back to head back. ").lower()
    print(" ")
    if answer == "grin":
        answer = input("You and the crew made it just in time to get a front row spot to see the headliner "
                       "band. You decide to take off and dance bare foot while holding your 4 inch heels. "
                       "After the festival, you notice that your stomach is loudly grumbling. Your bestie "
                       "is anxious to take you to your next surprise. Do you insist on getting some lunch "
                       "at a new restaurant or do you cross your fingers hoping the next surprise leads you "
                       "to some real grub? Type lunch to go eat now or surprise to get taken to your next surprise. ").lower()
        print(" ")
        if answer == "surprise":
            print("You and the crew pull up to your bestie's house. When your bestie unlocks the door, you all go in "
                  "together to be greeted by the surprise. A room full of your closest friends jump out to yell "
                  "'surprise'. The surprise party is a hit and you enjoy your exciting day after all.")

        elif answer == "lunch":
            print("You and the crew all get food poisoning. You head back home and are in bed with the chunks for the "
                  "rest of the day. You lose! ")
        else:
            print("Not valid option. You lose!")

    elif answer == "back":
        print("You and your bestie end up in a verbal fight because of timeliness and causing everyone to be late to "
              "the festival. Your bestie decides to drop you off home and leaves with your other friend to enjoy "
              "the festival without you.")
    else:
        print("Not valid option. You lose!")
else:
    print("Not valid option. You lose!")
