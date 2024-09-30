from twenty_one_game import TwentyOneGame  # Importerar TwentyOneGame klassen från twenty_one_game modulen

def main() -> None:  # Definierar huvudfunktionen som inte returnerar något (None)
    game: TwentyOneGame = TwentyOneGame()  # Skapar en ny instans av TwentyOneGame
    game.play_game()  # Startar det första spelet
    
    while True:  # Startar en oändlig loop för att möjliggöra flera spelomgångar
        while True:  # Inre loop för att hantera användarinput
            play_again: str = input("Do you want to play again? (yes/no): ").lower()  # Frågar användaren och konverterar svaret till små bokstäver
            if play_again in ['yes', 'y', 'no', 'n']:  # Kontrollerar om svaret är giltigt
                break  # Avslutar den inre loopen om svaret är giltigt
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")  # Felmeddelande vid ogiltigt svar
        
        if play_again in ['yes', 'y']:  # Kontrollerar om användaren vill spela igen
            game = TwentyOneGame()  # Skapar en ny spelinstans
            game.play_game()  # Startar en ny spelomgång
        else:
            break  # Avslutar den yttre loopen om användaren inte vill spela mer

    print("Thanks for playing!")  # Avslutsmeddelande när spelet är över

if __name__ == "__main__":  # Kontrollerar om skriptet körs direkt (inte importeras)
    main()  # Anropar huvudfunktionen om skriptet körs direkt