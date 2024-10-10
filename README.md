# Blackjack-With-UI

A Python-based BlackJack game with a graphical user interface (GUI).

## Features

- Play BlackJack against a dealer.
- Simple and intuitive UI.
- Dealer follows standard BlackJack rules.
- Game results displayed at the end of each round.

## Screenshots

![Player Wins](image.png)
![Dealer Wins](image-1.png)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/m4xy07/Blackjack-With-UI.git
   cd Blackjack-With-UI
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the game, execute the following command:

```sh
python blackjack.py
```

## Building the Executable

To build the executable using PyInstaller, run:

```sh
python -m PyInstaller blackjack.spec
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Author

[Aman Shaikh](mailto:hey@m4xy.org)


# Project Report

## Blackjack Game Project Report

##Introduction
Blackjack is a popular casino banking game played with one or more decks of 52 cards. The objective of the game is to have a hand value that is closer to 21 than the dealer's hand without exceeding 21. In this project, we have developed a graphical user interface (GUI) based Blackjack game using Python and the Tkinter library.

# Game Overview
The game starts with the player and the dealer being dealt two cards each. The player's cards are face up, while one of the dealer's cards is face up (the upcard) and the other is face down (the hole card). The player can see their own cards and the dealer's upcard.

The player can choose to either hit (take another card) or stick (keep their current hand). If the player's hand value exceeds 21, they immediately lose the game. If the player chooses to stick, the dealer reveals their hole card and must draw cards until their hand value is 17 or higher. If the dealer's hand value exceeds 21, the player wins.

## Code Structure
The code is structured into several classes and modules to ensure modularity and maintainability.

### Card Class
The Card class represents a single card with a suit and value. It has two attributes: suit and value. The `__init__` method initializes the card with a suit and value, and the __repr__ method returns a string representation of the card.

### Deck Class
The Deck class represents a deck of cards. It has one attribute: cards, which is a list of Card objects. The `__init__` method initializes the deck by creating a list of 52 cards (13 values x 4 suits) and shuffling them. The deal method returns the top card from the deck.

### Hand Class
The Hand class represents a player's or dealer's hand. It has three attributes: dealer, cards, and value. The dealer attribute is a boolean indicating whether the hand belongs to the dealer or not. The cards attribute is a list of Card objects, and the value attribute is the total value of the hand.

The `__init__` method initializes the hand with an optional dealer parameter. The add_card method adds a card to the hand, and the calculate_value method calculates the total value of the hand. The get_value method returns the total value of the hand.

### Game Class
The Game class represents the game itself. It has three attributes: deck, player_hand, and dealer_hand. The deck attribute is a Deck object, and the player_hand and dealer_hand attributes are Hand objects.

The `__init__` method initializes the game by creating a new deck and dealing two cards to the player and dealer. The play method deals the initial cards to the player and dealer. The get_player_hand_value, get_dealer_hand_value, get_player_hand_cards, and get_dealer_hand_cards methods return the values and cards of the player's and dealer's hands, respectively.

### Application Class
The Application class represents the GUI application. It inherits from tk.Frame and has several attributes: master, game, and game_over. The master attribute is the Tkinter root window, and the game attribute is a Game object. The game_over attribute is a boolean indicating whether the game is over or not.

The `__init__` method initializes the application by creating a new game and setting up the GUI widgets. The create_widgets method creates the GUI widgets, and the update_ui method updates the GUI with the current game state.

The hit, stick, new_game, and about methods handle the corresponding button clicks. The hit method adds a card to the player's hand, the stick method ends the player's turn and starts the dealer's turn, the new_game method starts a new game, and the about method opens a web browser with the developer's GitHub page.

## Tkinter GUI
The Tkinter GUI is created using the Application class. It consists of several widgets:

- A title label with the game title
- A player hand label and value label
- A dealer hand label and value label
- A result label to display the game outcome
- A button frame with hit, stick, new game, and about buttons
The GUI is updated dynamically using the update_ui method, which updates the labels and buttons based on the current game state.

Overall, the code structure is designed to separate the game logic from the GUI logic, making it easier to maintain and modify the code.

# Key Functions

# Card Class

```python
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
```
The Card class represents a single card with a suit and value. The __repr__ method returns a string representation of the card.

# Deck Class

```python
class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"]
                      for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
```
The Deck class represents a deck of cards and provides methods for shuffling and dealing cards. The deal method returns the top card from the deck.

# Hand Class
```python
class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value
```
The Hand class represents a player's or dealer's hand and provides methods for adding cards and calculating the hand value. The calculate_value method calculates the hand value based on the cards in the hand.

## Game Class

```python
class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)

    def play(self):
        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

    def get_player_hand_value(self):
        return self.player_hand.get_value()

    def get_dealer_hand_value(self):
        return self.dealer_hand.get_value()

    def get_player_hand_cards(self):
        return self.player_hand.cards

    def get_dealer_hand_cards(self):
        return self.dealer_hand.cards
```
The Game class represents the game itself and provides methods for playing the game. The play method deals the initial cards to the player and dealer.

## Application Class
```python
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.game = Game()
        self.game_over = False
        self.update_ui()

    def create_widgets(self):
        # Create GUI widgets
        pass

    def update_ui(self):
        # Update the GUI with the current game state
        pass

    def hit(self):
        # Handle the hit button click
        pass

    def stick(self):
        # Handle the stick button click
        pass

    def new_game(self):
        # Handle the new game button click
        pass

    def about(self):
        # Handle the about button click
        pass
```
The Application class represents the GUI application and provides methods for creating the GUI and handling user input.

# Conclusion
In this project, we have successfully developed a GUI-based Blackjack game using Python and the Tkinter library. The game provides a user-friendly interface for players to interact with the game, and the code is structured into several classes to ensure modularity and maintainability.


# Future Improvements and Optimizations
While the current implementation provides a basic Blackjack game with a GUI, there are several improvements and optimizations that can be made to enhance the game's functionality and user experience. Here are some suggestions:

## Future Improvements:
- Implement betting system: Add a betting system that allows players to place bets before each round. This can be done by adding a text entry field for the player to input their bet amount.
- Add more game modes: Currently, the game only supports a single-player mode. Consider adding multi-player modes, such as a two-player mode where players can compete against each other.
- Implement card counting: Add a feature that allows players to count cards and adjust their strategy accordingly. This can be done by keeping track of the cards that have been played and adjusting the player's strategy based on the remaining cards in the deck.
- Add more rules and variations: Blackjack has many variations and rules that can be added to the game, such as insurance, surrender, and double down.
- Improve the GUI: Consider using a more modern GUI framework, such as PyQt or wxPython, to improve the game's appearance and user experience.

## Optimizations:
- Optimize the deck shuffling algorithm: The current implementation uses the random.shuffle function to shuffle the deck, which can be slow for large decks. Consider using a more efficient shuffling algorithm, such as the Fisher-Yates shuffle.
- Use a more efficient data structure for the deck: The current implementation uses a list to represent the deck, which can be slow for large decks. Consider using a more efficient data structure, such as a deque or a set.
- Optimize the game logic: The current implementation uses a simple if-else statement to determine the game outcome. Consider using a more efficient algorithm, such as a decision tree or a state machine.
- Use caching: Consider using caching to store the results of expensive function calls, such as the calculate_value method.
- Profile and optimize the code: Use a profiling tool, such as cProfile, to identify performance bottlenecks in the code and optimize them accordingly.

## Additional Features:
- Add sound effects and music: Consider adding sound effects and music to enhance the game's atmosphere and user experience.
- Add animations: Consider adding animations to enhance the game's visual appeal and user experience.
- Add a high score system: Consider adding a high score system that allows players to track their progress and compete with others.
- Add a tutorial or help system: Consider adding a tutorial or help system that teaches players the rules and strategies of Blackjack.
