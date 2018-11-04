import random

class DealHand():

#   max_total = 21
#       moved max_total to CheckBust class
    forced_hit = 16
    turn = ''
    full_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,'10','10','10','10','J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
    
    p_card = []
    d_card = []
    p_total_count = 0
    d_total_count = 0

    def __init__(self):
#        self.full_deck = fulldeck.full_deck
       
        self.d_card = []
#        self.p_total_count = 0


    def PlayersHand(self):
        random_card = random.choice(DealHand.full_deck)
        DealHand.full_deck.remove(random_card)
        DealHand.p_card.append(random_card)
        print(f"You've been dealt a {random_card}.")
        if random_card in DealHand.full_deck[0:31]:
            DealHand.p_total_count += int(random_card)
        elif random_card == 'T' or random_card == 'J' or random_card == 'Q' or random_card == 'K':
            DealHand.p_total_count += 10
        elif random_card == 'A':
            pick_ace = int(input("Would you like your A to be worth 1 or 11? "))
            if pick_ace == 1:
                DealHand.p_total_count += 1
            elif pick_ace == 11:
                DealHand.p_total_count += 11   

    def DealersHand(self):
        print("This is running")
        random_card = random.choice(DealHand.full_deck)
        DealHand.full_deck.remove(random_card)
        DealHand.d_card.append(random_card)
        if len(DealHand.d_card) < 2 or len(DealHand.d_card) > 2 :
            print(f"The dealer's been dealt a {random_card}.")
        if random_card in DealHand.full_deck[0:31]:
            DealHand.d_total_count += int(random_card)
        elif random_card == 'T' or 'J' or 'Q' or 'K':
            DealHand.d_total_count += 10
        elif random_card == 'A':
            DealHand.d_total_count += 1
class Player(DealHand):

    win = ""
    stack_size = int()
    p_bet_size = int()

    def __init__(self,p_bet_size):
        self.p_bet_size = p_bet_size
#      self.p_hand = sum(self.p_card)
        
    def p_decision(self):       
        while True:
            hit_or_stay = str(input("Would you like to hit or stay? "))
            if hit_or_stay.capitalize() == "Hit":
                DealHand.PlayersHand(self)
                print(f"You have a total of {DealHand.p_total_count}.")
                Dealer.p_bust_check(self)
#                if DealHand.p_total_count >= 21:
#                    break
            elif hit_or_stay.capitalize() == "Stay":
                print("Player stays. Good Luck!")
                Dealer.p_bust_check(self)
                break
            elif DealHand.p_total_count >= 21:
                break
            else:
                break
    def adjust_stack(self):
        if Player.win == "True":
            Player.stack_size += Player.p_bet_size
            print(f"Your stack is ${Player.stack_size}")
        elif Player.win == "False":
            Player.stack_size -= Player.p_bet_size
            print(f"Your stack is ${Player.stack_size}")
        else:
            print(f"You haven't lost, nor won. Your stack is still at ${Player.stack_size}")
        

#    def p_bust_check(self):
#        if p_total_count > 21:
#            print(f"You've busted, with a total of {p_total_count}. You lose.")

class Dealer(Player):

    def __init__(self):
        pass

    def d_decision(self):
        while True:
            if DealHand.d_total_count < 17:
                DealHand.DealersHand(self)
                print(f"The Dealer has a total of {DealHand.d_total_count}.")
 #               Dealer.d_decision(self)

            elif DealHand.d_total_count >= 17 and DealHand.d_total_count <= 21:
                if DealHand.d_total_count > DealHand.p_total_count:
                    print("You LOSE sucka! This is a Casino, you think you in Las Vegas Vacation or somethin?")
                    print(f"The dealer has {DealHand.d_total_count}")
                    Player.win = "False"
                    Player.adjust_stack(self)
                    break
                elif DealHand.d_total_count == DealHand.p_total_count:
                    print("IT'S A TIE. You and the Casino are besties.")
                    print(f"The dealer has {DealHand.d_total_count}")
                    Player.adjust_stack(self)
                    break
            elif DealHand.d_total_count > 21:
                print("The Casino Loses....for now sucka")
                print(f"The dealer has {DealHand.d_total_count}")
                Player.win = "True"
                Player.adjust_stack(self)
                break
 #           elif DealHand.d_total_count > 21:
 #               print( "Dealer BUSTS")
 #               break

    def p_bust_check(self):
        if DealHand.p_total_count > 21:
            print(f"You've busted, with a total of {DealHand.p_total_count}. You lose.")
            Player.win = "False"
            Player.adjust_stack(self)
        elif DealHand.p_total_count == 21:
            print(f"HOLY SHIT SUCKA. 21! YOU WIN!")
            Player.win = "True"
            Player.adjust_stack(self)         

if __name__ == '__main__':
     
    p_name = str(input("Hey there hot shot. What's your name? "))
    p_stack_size = int(input(f"Greetings {p_name}. How much would you like to buy-in for? "))
    Player.stack_size = p_stack_size
    print(f"Thanks {p_name} here's ${p_stack_size} in chips.")
    bet_size = int(input(f"How much do you want to bet? "))
    if bet_size > p_stack_size:
        int(input("Who do you think you're dealing with. We'll break your hot damn legs. Bet lower."))
    else:
        Player.p_bet_size = bet_size
    if bet_size >= (p_stack_size*.8):
        print("\n\n\n\n\nB-B-b-baller!!\n\n\n\n\n")
    else:
        print("\n\n\n\n\nNo risk, no reward puss-ay. ...Anways, good luck\n\n\n\n\n")

while True:    

    full_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,'10','10','10','10','J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
    DealHand.p_total_count = 0
    DealHand.d_total_count = 0
    DealHand.d_card = []

    print("***shuffle shuffle shuffle***   ***deal deal deal***\n\n\n")
    player1 = Player(bet_size)

    p_deal_hand = DealHand()
    p_deal_hand.PlayersHand()
    p_deal_hand.PlayersHand()
    p_deal_hand.DealersHand()
    p_deal_hand.DealersHand()
    print(f"The dealer is showing a {DealHand.d_card[(0)]}.\n")
    print(f"You have a total of {DealHand.p_total_count}.\n")
    player1.p_decision()
    print(f"You have a total of {DealHand.p_total_count}.\n")
    dealer1 = Dealer()
    dealer1.d_decision()

  
 #   dealer1 = Dealer()
 #   dealer1.d_decision()

    rematch = str(input("Would you like to play again? (Y/N) "))
    if rematch.capitalize() == "Y" or rematch.capitalize() ==  "Yes":
        print(f"You're stack is ${Player.stack_size}")
        new_bet = int(input("You've chosen a rematch, how much do you want to bet? \n"))
        while True:
            if new_bet > Player.stack_size:
                new_bet = int(input((f"This ain't no bank. You have ${Player.stack_size} left...bet lower.")))
                Player.p_bet_size = new_bet
            else:
                Player.p_bet_size = new_bet
                break
        print("\n\n\n\n\nNo more good luck...here are your cards. **THROWS CARDS IN DISGUST AT PATRON**\n\n\n\n\n")
    elif rematch.capitalize() == "N" or rematch.capitalize() == "No":
        break


