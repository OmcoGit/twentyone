from typing import List  # Importerar List för typannotering
import random  # Importerar random för att generera slumpmässiga kort

class TwentyOneGame:
    def __init__(self) -> None:
        self.player_hand: List[int] = []  # Initialiserar spelarens hand som en tom lista
        self.computer_hand: List[int] = []  # Initialiserar datorns hand som en tom lista

    def draw_card(self) -> int:
        return random.randint(1, 13)  # Returnerar ett slumpmässigt kort (1-13)

    def calculate_score(self, hand: List[int]) -> int:
        score: int = 0  # Initialiserar poängen
        aces: int = 0  # Räknare för ess
    
        for card in hand:
            match card:
                case 1:
                    aces += 1  # Räknar antalet ess
                case 11:
                    score += 11  # Knekt
                case 12: 
                    score += 12  # Dam
                case 13:
                    score += 13  # Kung
                case _:
                    score += card  # Vanliga kort (2-10) läggs till direkt 
    
        for _ in range(aces):
            if score + 14 <= 21:
                score += 14  # Lägger till 14 för ess om det inte överstiger 21
            else:
                score += 1  # Annars lägg till 1 för ess
        
        return score  # Returnerar den totala poängen

    def play_game(self) -> None:
        print("Welcome to Twenty-One!")

        self.player_hand = [self.draw_card()]  # Ger spelaren ett startkort
        self.computer_hand = [self.draw_card()]  # Ger datorn ett startkort
        
        print(f"\nYour first card: {self.player_hand[0]}")
        print(f"Computer's first card: {self.computer_hand[0]}")

        while True:
            print(f"\nYour hand: {self.player_hand}")
            print(f"Your score: {self.calculate_score(self.player_hand)}")

            if self.calculate_score(self.player_hand) > 21:
                print("Unlucky! You went over 21. You lose!")
                return  # Avslutar spelet om spelaren går över 21
            
            # Felhantering för användarinput
            while True:
                want_to_draw: str = input("Do you want to draw another card? (yes/no): ").lower()
                if want_to_draw in ['yes', 'y', 'no', 'n']:
                    break  # Bryter loopen om svaret är giltigt
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            
            if want_to_draw in ['yes', 'y']:
                self.player_hand.append(self.draw_card())  # Lägger till ett nytt kort till spelarens hand
                print(f"\nYour hand: {self.player_hand}")
                print(f"Your score: {self.calculate_score(self.player_hand)}")
                print(f"Computer's first card: {self.computer_hand[0]}")
            else:
                break  # Avslutar spelarens tur om de inte vill dra fler kort

        while self.calculate_score(self.computer_hand) < 17:
            self.computer_hand.append(self.draw_card())  # Datorn drar kort tills den har minst 17 poäng
            
        computer_score: int = self.calculate_score(self.computer_hand)  # Beräknar datorns slutpoäng

        # Visar slutresultatet
        print(f"\nYour final hand: {self.player_hand}")
        print(f"Your final score: {self.calculate_score(self.player_hand)}")
        print(f"Computer's final hand: {self.computer_hand}")
        print(f"Computer's final score: {computer_score}")

        player_score: int = self.calculate_score(self.player_hand)  # Beräknar spelarens slutpoäng

        # Avgör vinnaren
        if computer_score > 21 or (player_score <= 21 and player_score > computer_score):
            print("You win!")
        elif player_score == computer_score:
            print("It's a tie!")
        else:
            print("Computer wins!")