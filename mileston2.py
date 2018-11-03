import random
import math

class Deck():


    def __init__(self):
        '''
        Builds a deck
        '''
        self.cards_in_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
        self.dealt_card = []
        self.running_total = 0
        
    def randompick(self):
        '''
        Picks a random card from a deck
        '''
        random_card = random.choice(self.cards_in_deck)
        self.cards_in_deck.remove(random_card)


        if random_card == 'J':
            self.dealt_card = 10
            return self.running_total + 10
        elif random_card == 'Q':
            self.dealt_card = 10
            return self.running_total + 10
        elif random_card == 'K':
            self.dealt_card = 10
            return self.running_total + 10
        elif random_card == 'A':
            self.dealt_card = int(input("Do you want your card to be worth 1 or 11? "))
            if random_card == 1:
                self.dealt_card = 1
                return self.running_total + 1
            elif random_card == 11:
                self.dealt_card = 11
                return self.running_total + 11
        else:
            self.dealt_card = random_card
            return self.running_total + int(self.dealt_card)

        print(self.dealt_card) 
        print(f"Running total is: {self.running_total}")




class Player(Deck):
    """docstring for Player"""
    def __init__(self, name, stack_size):
        self.name = name
        self.stack_size = stack_size

    def official_stack_size(self):
        print(f"You've bought in for ${self.stack_size}.")

    def player_running_total(self):
        print(f"You're running total is: {self.running_total}")

class Dealer(Deck):

    def __init__(self):
        self.running_total = 0

    def dealer_running_total(self):
        pass    

class PlayersBet(Player):

    def __init__(self,bet):
        self.bet = bet

    def bet_check(self):
        if self.bet > self.stack_size:
            print(f"Sorry, you don't have that much to bet. Pick an amount lower than {self.stack_size}")


#class Dealer():
    """docstring for Dealer"""
  #  def __init__(self):
     #   dealers_hand = []



class DealtHand(Dealer):
   
    
    def __init__(self):       
        Deck.__init__(self)
        self.players_hand = []
        self.dealers_hand = []
       # self.dealers_hand = []
        self.players_total = sum(self.players_hand)
       # dealers_hand = []
      #  players_hand = []

    def dealers_cards(self):


        Dealer_Card1_SHOWN = Deck.randompick(self)
        Dealer_Card2 = Deck.randompick(self)
        return self.dealers_hand.extend([Dealer_Card1_SHOWN, Dealer_Card2])

    def print_dealers_hand(self):
        print(f"Dealer's hand: {self.running_total}")

        

    def players_cards(self, players_hand):

        self.players_hand = players_hand

  #      self.Player_Card1 = []
  #      self.Player_Card2 = []

 #       players_hand = []

        self.Player_Card1 = Deck.randompick(self)
        self.players_hand.append(self.Player_Card1)  
        self.Player_Card2 = Deck.randompick(self)
        self.players_hand.append(self.Player_Card2)

        print(f"players hand {self.players_hand}") 

class NextMove(DealtHand,Deck):

    def __init__(self):
        Deck.__init__(self)
        DealtHand.__init__(self)

    def deal_next_card(self):

  #      players_total = sum(self.players_hand)
        print(self.players_total)
        
        while True:
            card_request = str(input(f"Your total is {self.players_total}. Would you like to Hit or Stay? "))
            if card_request.capitalize() == 'Hit' and self.players_total <= 21:
                Player_Card3 = Deck.randompick(self)
                self.players_hand.append(Player_Card3)
                
            elif self.players_total > 21:
                "YOU'VE BUSTED, YOU LOSE!"
                break
            else:
                break

        return card_request
        #   players_total = players_total + dealt_card
        #elif card_request.capitalize() == 'Stay':  
        
     
class CheckBust(DealtHand):

    def __init__(self):
        DealtHand.__init__(self)
    #    DealtHand.dealers_cards(self)
    #    DealtHand.players_cards(self)
    
    def player_bust_check(self):
  #      players_total = sum(self.players_hand)

        if self.players_total > 21:
            print("YOU'VE BUSTED, YOU LOSE!")
            self.stack_size -= self.bet

    def dealer_bust_check(self):
        dealers_total = sum(DealtHand.dealers_hand)

        if dealers_total > 21:
            print("THE DEALER HAS BUSTED, YOU WIN!")
            self.stack_size += self.bet
'''
new class to test out git branching/commits
'''
class NewClassAppears():

    def __init__(self,number):
        self.number = number

    def do_something(self):
        print(f"Do something with {self.number}")

if __name__ == '__main__':
    
        players_name = str(input("Hello there, what's your name? "))
        players_stack = int(input("How much would you like to bring to the table? "))

        the_deck = Deck()
        the_deck.__init__()
        player = Player(players_name,players_stack)
        player.official_stack_size()

        this_rounds_hand = DealtHand()
        this_rounds_hand.dealers_cards()
        this_rounds_hand.print_dealers_hand()
        this_rounds_hand.players_cards(players_hand = [])

        next_move = NextMove()
        next_move.deal_next_card()

        bust = CheckBust()
        bust.player_bust_check()
        bust.dealer_bust_check()
        
  #      while True:
   #         if sum(this_rounds_hand.players_hand) > 21:
  #              CheckBust.player_bust_check()
  #              break
  #          elif sum(this_rounds_hand.dealers_hand) > 21: 
  #              CheckBust.dealer_bust_check()
  #              break
  #          elif next_move.card_request == 'Hit':
  #              next_move.deal_next_card()
  #              continue
  #          else:
  #              break



