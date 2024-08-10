import random

values = {
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'jack': 11,
            'queen': 12,
            'king': 13,
            'ace': 14
        }
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')

class Card():

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank.lower()]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():

    def __init__(self):
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)
    
class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.has_won = False

    def remove_card(self):
        return self.hand.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.hand)} cards."
    
def game():
    player1 = Player("1")
    player2 = Player("2")

    deck = Deck()
    deck.shuffle_deck()

    for _ in range(26):
        player1.add_cards(deck.deal_card())
        player2.add_cards(deck.deal_card())

    game_on = True
    round_count = 0

    while game_on:
        round_count += 1
        print(f"\nRound {round_count} :\n")

        player1_table = []
        player2_table = []

        player1_table.append(player1.remove_card())
        player2_table.append(player2.remove_card())

        at_war = True

        while at_war:
            print(f"Player {player1.name} : {player1_table[-1]} vs Player {player2.name} : {player2_table[-1]} !!!")

            if player1_table[-1].value < player2_table[-1].value:
                print(f"Player {player2.name} has won Round {round_count} !!!")
                player2_table.extend(player1_table)
                player1_table = []
                at_war = False
            elif player1_table[-1].value > player2_table[-1].value:
                print(f"Player {player1.name} has won Round {round_count} !!!")
                player1_table.extend(player2_table)
                player2_table = []
                at_war = False
            else:
                print("WAR !!!!!!")

                if len(player1.hand) < 4 or len(player2.hand) < 4:
                    at_war = game_on = False
                    if len(player1.hand) < 4:
                        player2.has_won = True
                    else:
                        player1.has_won = True
                    break
                else:
                    for _ in range(4):
                        player1_table.append(player1.remove_card())
                        player2_table.append(player2.remove_card())

            if not at_war and game_on:
                player1.add_cards(player1_table)
                player2.add_cards(player2_table)
        
        if player1.has_won or len(player2.hand) == 0:
            print(f"\n\nPlayer {player1.name} has won !!!!!")
            break
        elif player2.has_won or len(player1.hand) == 0:
            print(f"\n\nPlayer {player2.name} has won !!!!!")
            break

if __name__ == "__main__":
    game()