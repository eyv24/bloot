msharie_san = {'sera': '4', 'hundred':'20', 'fifty': '10','four hundred':'40'} #save value of msharie of san
msharie_hokm = {'sera': '2', 'hundred':'10', 'fifty': '5','bloot':'2'} #save value of msharie

import matplotlib.pyplot as pyplot
while True: #to continue the program and didnt close 
    mode=input("Enter the mode 'Rules' or 'Calculator': ") #there is two mode in this program and you have ti chose
    if mode =='Rules':
        Type=input("Enter what you want 'Rules of Bloot' or 'Rules of Msharie': ") #two type of rules
        if Type =='Rules of Msharie':
            game = input("Enter the type of game 'san' or 'hokm':") # to type of game san and hokm
            if game == "hokm":
                class card:
                    def __init__(self, name, point):
                            self.name = name
                            self.point = point
                    def get_description(self):
                         return f" {self.name}   |   {self.point}  "
                        
                card1 = card("A",  11)   #the value of the cards
                card2 = card("K",  4)
                card3 = card("Q",  3 )
                card4 = card("J",  20 )
                card5 = card("10",10)
                card6 = card("9",  14 )
                card7 = card("8",  0 )
                card8 = card("7",  0)
                print("name | point")
                print(card1.get_description())
                print(card2.get_description())
                print(card3.get_description())
                print(card4.get_description())
                print(card5.get_description())
                print(card6.get_description())
                print(card7.get_description())
                print(card8.get_description())
                x = input("Enter the msharie you want to know its points in hokm : ") #to know the value of msharie
                if x in msharie_hokm  :
                      print(f"{x} = {msharie_hokm[x]} point")
            elif game == "san":
                class card:
                    def __init__(self, name, point):
                            self.name = name
                            self.point = point
                    def get_description(self):
                         return f"{self.name}    |   {self.point}  "
                card1 = card("A", 11)
                card2 = card("K", 4)
                card3 = card("Q", 3 )
                card4 = card("J", 2 )
                card5 = card("10", 10)
                card6 = card("9", 0)
                card7 = card("8", 0 )
                card8 = card("7", 0)
                print("name | point")
                print(card1.get_description())
                print(card2.get_description())
                print(card3.get_description())
                print(card4.get_description())
                print(card5.get_description())
                print(card6.get_description())
                print(card7.get_description())
                print(card8.get_description())
                x = input("Enter the msharie you want to know its points in san: ")
                if x in msharie_san  :
                        print(f"{x} = {msharie_san[x]} point")
            else : #the rules
                print("type of game incorrect")
        elif Type =='Rules of Bloot':
            print("#Rules of Baloot:")
            print("\n*Playing cards from seven to ace of each suit")
            print("*All players are entitled to choose either San or Hokm")
            print("*San is worth 26 points (without masharie)")
            print("*Hokm is worth 16 points (without masharie)")
            print("*The order of San cards is (ace, ten, king, queen, jack, nine, eight, seven)")
            print("*The order of Hokm cards is (jack, nine, ace, ten, king, queen, eight, seven)")
            print("*The player to the left of the dealer has the right to arrange the cards three times")
            print("*The dealer distributes three cards in the first round, then two cards in the second round, and then reveals the first card of the cards he distributes")
            print("*The buyer picks up the card on the ground")
            print("*The dealer distributes cards in the same order he started with: three cards to each player except two cards to the buyer")
            print("*Thus, each player has eight cards")
            print("*The game starts from the right of the dealer")
            print("\n#infringement: ")
            print("*If a player plays a different card when they have one of the same suit")
            print("*If they showed us a wrong masharie")
            print("*If you make the playnig obvious")
            print("*In Hokm, you must play a higher card than the one played if you have one")
            print("*In Hokm, if you do not have a card of the same suit as the one played, you must play a Hakem card unless: ")
            print(".1- if your teammate said an ace when he play the card")
            print(".2- if your teamate plays an ace and no one played a Hokm card")
            print("\n*If the dealer makes a mistake in distribution")
            print("*If you play and it is not your turn to play")
    elif mode == 'Calculator': #mode 2
        import math
        total1 = 0 #to add the value each to others for team1 
        total2 = 0 #to add the value each to others for team2
        while True:
            if total1 >= 152: #to finish the game and announce the winner "the limit of game is 152"
                print("Congratulations to team1 they are the winners ")
                break
            elif total2 >= 152:
                print("Congratulations to team2 they are the winners ")
                break
            game = input("Enter the type of game 'san' or 'hokm':")
            if game == "san":
                num = 26  #the value of san
                kbouts = 44 #when you get all the cards and the other team it didn't have a card it's called kbout
                teams = int(input("Which team is the buyer (Enter 1 for team1 or 2 for team2): ")) 
                if teams == 1:
                    team2 = int(input("Enter the bant for team2: ")) #to enter the value of cards with team 2
                    msharie = input("Does anyone have a msharie? ")
                    if msharie == "yes":
                        msharie1, msharie2 = eval(input("Enter the msharie for team1 and team2: ")) #to add msharie to the 
                        bant = team2 / 10
                        calc = math.ceil(bant) * 2 if team2 % 5 == 0 else round(bant) * 2 #in san when the value of cards =45 it's mean 10 you have to round up and x2
                        if calc + msharie2 <=(14  +msharie2+ msharie1) or not (team2 ==152,-152): #solving
                            if team2>0:
                                t1 = num + msharie1 - calc
                                t2 = calc + msharie2
                            else:
                                t1 = kbouts + msharie1
                                t2 = 0
                                
                        elif team2==152: #to add kbout for the team who enter
                            t1 = 0
                            t2 = kbouts + msharie2
                        else: #if the cards reach number that make other team lose 
                            t1 = 0
                            t2 = num + msharie1 + msharie2
                    elif msharie == "no":
                        bant = team2 / 10
                        calc = math.ceil(bant) * 2 if team2 % 5 == 0 else round(bant) * 2
                        if calc <= 14 or not (team2 ==152,-152):
                            if team2>0:
                                t1 = num - calc
                                t2 = calc
                            else:
                                t1 = kbouts
                                t2 = 0
                        elif team2==152:
                              t1 = 0
                              t2 = kbouts 
                        else:
                            t1 = 0
                            t2 = num
                elif teams == 2:
                    team1 = int(input("Enter the bant for team1: "))
                    msharie = input("Does anyone have a msharie? ")
                    if msharie == "yes":
                        msharie1, msharie2 = eval(input("Enter the msharie for team1 and team2: "))
                        bant = team1 / 10
                        calc = math.ceil(bant) * 2 if team1 % 5 == 0 else round(bant) * 2
                        if calc + msharie1 <= (14 +msharie1+ msharie2) or not (team1 ==152,-152):
                            if team1>0:
                                t2 = num + msharie2 - calc
                                t1 = calc + msharie1
                            else:
                                t2 = kbouts + msharie2
                                t1 = 0
                        elif team1==152:
                                t2 = 0
                                t1 = kbouts + msharie1
                        else:
                            t2 = 0
                            t1 = num + msharie1 + msharie2
                    elif msharie == "no":
                            bant = team1 / 10
                            calc = math.ceil(bant) * 2 if team1 % 5 == 0 else round(bant) * 2
                            if calc <= 14 or not (team1 == 152,-152):
                                if team1>0:
                                       t2 = num - calc
                                       t1 = calc
                                else:
                                    t2 = kbouts 
                                    t1 = 0
                            elif team1==152:
                                       t2 = 0
                                       t1 = kbouts 
                            else:
                                    t2 = 0
                                    t1 = num
            if game == "hokm":
                num = 16 #value of hokm
                kbouth=25 #kbout of hokm 
                teams = int(input("Wich team is the buyer (Enter 1 for team1 or 2 for team2): "))
                if teams == 1:
                    team2 = int(input("Enter the bant for team2: "))
                    msharie = input("Does anyone have a msharie? ")
                    if msharie == "yes":
                        msharie1, msharie2 = eval(input("Enter the msharie for team1 and team2: "))
                        bant = team2 / 10
                        calc = math.floor(bant) if team2 % 5 == 0 else round(bant)  #in hokm when the value of cards =45 it's mean 4 you have to round down 
                        if calc + msharie2 <= (num  +msharie2+ msharie1)/ 2 or not (team1 == 152 , -152)  :
                            if team2>0:
                                t1 = num + msharie1 - calc
                                t2 = calc + msharie2
                            else:
                                t1 = msharie1 + kbouth
                            t2 = 0
                        elif team2 == 152 :
                            t1 = 0
                            t2 = kbouth + msharie2
                        else:
                            t1 = 0
                            t2 = num + msharie1 + msharie2
                    elif msharie == "no":
                        bant = team2 / 10
                        calc = math.floor(bant) if team2 % 5 == 0 else round(bant)
                        if calc <= num / 2 or not (team2 == 152 , -152):
                            if team2>0:
                                t1 = num - calc
                                t2 = calc
                            else:
                                t2 = 0
                                t1 =kbouth 
                        elif team2 == 152:
                            t2=kbouth
                            t1 = 0
                        else:
                            t1 = 0
                            t2 = num
                elif teams == 2:
                    team1 = int(input("Enter the bant for team1: "))
                    msharie = input("Does anyone have a msharie? ")
                    if msharie == "yes":
                        msharie1, msharie2 = eval(input("Enter the msharie for team1 and team2: "))
                        bant = team1 / 10
                        calc = math.floor(bant) if team1 % 5 == 0 else round(bant) 
                        if calc + msharie1 <= (num +msharie1+ msharie2)/ 2  or not (team1 == 152 , -152):
                            if team1>0:
                                t2 = num + msharie2 - calc
                                t1 = calc + msharie1
                            else:
                                t2 = msharie2 + kbouth
                            t1 = 0
                        elif team1 == 152 :
                            t2 = 0
                            t1 = kbouth + msharie1 
                        else:
                            t2 = 0
                            t1 = num + msharie1 + msharie2
                    elif msharie == "no":
                        bant = team1 / 10
                        calc = math.floor(bant) if team1 % 5 == 0 else round(bant)
                        if calc <= num / 2 or not (team1 == 152 , -152):
                            if team1>0:
                                t2 = num - calc
                                t1 = calc
                            else:
                                t1 = 0
                            t2 =kbouth
                        elif team1 == 152:
                            t1=kbouth
                            t2 = 0
                        else:
                            t2 = 0
                            t1 = num
            total1 += t1 #to add the values
            total2 += t2
            print("team1 | team2")
            print(total1,"\t", total2)
            C = ["team1","team2"]
            index = [1,2]
            point = [total1,total2]
            pyplot.xlabel("teams")
            pyplot.ylabel("point of team")
            pyplot.bar(index,point,tick_label=C)
            pyplot.show()

            

        
    





