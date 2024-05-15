import tkinter as tk
from random import shuffle
import webbrowser
import PIL
from PIL import Image, ImageTk, ImageDraw

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"]
                      for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

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

        image = Image.open("icon.png")
        photo_image = ImageTk.PhotoImage(image.resize((70, 70)))
        title_image = tk.Button(self, command=self.title, image=photo_image)
        title_image.image = photo_image 
        title_image.pack(padx=20, pady=20)

        # self.title_label = tk.Label(self, text="Blackjack", font=("Impact", 24, "bold"), fg="#125488")
        # self.title_label.pack(padx=20,pady=20)

        self.player_hand_label = tk.Label(self, text="Player's Hand:", font=("Arial", 14), fg="#666")
        self.player_hand_label.pack()

        self.player_hand_value_label = tk.Label(self, text="Value: 0", font=("Corbel", 12), fg="#666", wraplength=300)
        self.player_hand_value_label.pack()

        self.dealer_hand_label = tk.Label(self, text="Dealer's Hand:", font=("Arial", 14), fg="#666")
        self.dealer_hand_label.pack()

        self.dealer_hand_value_label = tk.Label(self, text="Value: 0", font=("Corbel", 12), fg="#666", wraplength=300)
        self.dealer_hand_value_label.pack()


        self.result_label = tk.Label(self, text="", font=("Candara", 15, "bold"), fg="#333")
        self.result_label.pack(pady=10)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack()

        self.hit_button = tk.Button(self.button_frame, text="Hit", command=self.hit, font=("Corbel", 12), bg="#4C23C2", fg="#fff", activebackground="#483DF6")
        self.hit_button.pack(side=tk.LEFT, padx=10)

        self.stick_button = tk.Button(self.button_frame, text="Stick", command=self.stick, font=("Corbel", 12), bg="#4C23C2", fg="#fff", activebackground="#483DF6")
        self.stick_button.pack(side=tk.LEFT, padx=10)

        self.new_game_button = tk.Button(self.button_frame, text="New Game", command=self.new_game, font=("Corbel", 12), bg="#4C23C2", fg="#fff", activebackground="#483DF6")
        self.new_game_button.pack(side=tk.LEFT, padx=10)

        self.about_button = tk.Button(self.button_frame, text="About", command=self.about, font=("Corbel", 12), bg="#4C23C2", fg="#fff", activebackground="#483DF6")
        self.about_button.pack(side=tk.LEFT, padx=10)

    def update_label(self, label, value, cards):
        label.config(text=f"Value: {value} \n Cards: {', '.join([str(card) for card in cards])}")

    def update_ui(self):
        player_hand_value = self.game.get_player_hand_value()
        dealer_hand_value = self.game.get_dealer_hand_value()

        self.update_label(self.player_hand_value_label, player_hand_value, self.game.get_player_hand_cards())
        self.update_label(self.dealer_hand_value_label, dealer_hand_value, self.game.get_dealer_hand_cards())
        
        

    def hit(self):
        #self.hit_button.config(bg="lightgreen")
        #self.after(80, lambda: self.hit_button.config(bg="#4CAF50"))
        if not self.game_over:
            self.game.player_hand.add_card(self.game.deck.deal())
            self.update_ui()

            if self.game.get_player_hand_value() > 21:
                self.stick()

    def stick(self):
        #self.stick_button.config(bg="lightblue")
        #self.after(80, lambda: self.stick_button.config(bg="#2196F3"))
        if not self.game_over:
            player_hand_value = self.game.get_player_hand_value()
            dealer_hand_value = self.game.get_dealer_hand_value()

            while dealer_hand_value < 17:
                self.game.dealer_hand.add_card(self.game.deck.deal())
                dealer_hand_value = self.game.get_dealer_hand_value()
                self.update_ui()  # Update the dealer's hand value in the UI

            if player_hand_value > 21:
                result = "Busted! Dealer wins."
            elif dealer_hand_value > 21:
                result = "You Win! Dealer Busted."
            elif player_hand_value > dealer_hand_value:
                result = "You win!"
            elif player_hand_value == dealer_hand_value:
                result = "Tie!"
            else:
                result = "Dealer wins!"

            self.result_label.config(text=result, fg="#3868D9" if result.startswith("You") else "red")
            self.game_over = True

            # Update the UI with the final hands
            self.update_label(self.player_hand_value_label, player_hand_value, self.game.get_player_hand_cards())
            self.update_label(self.dealer_hand_value_label, dealer_hand_value, self.game.get_dealer_hand_cards())

    def new_game(self):
        self.game = Game()
        self.game_over = False
        self.update_ui()
        self.result_label.config(text="")

        # Re-enable the buttons on new game
        self.hit_button.config(state="normal")
        self.stick_button.config(state="normal")

    def about(self):
        webbrowser.open("https://github.com/m4xy07")

    def title(self):
        webbrowser.open("https://github.com/m4xy07/BlackJack-With-UI")

root = tk.Tk()
root.title("Blackjack")
root.iconbitmap("icon.ico")
root.geometry("360x450")
root.resizable(False, True)
app = Application(master=root)
app.mainloop()