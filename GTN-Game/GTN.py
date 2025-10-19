import random

class GuessTheNumber:
    def __init__(self):        
        self.num = random.randint(1, 10)
        self.__chances = 3
        self.__instructions()
        self.play()
    
    def __instructions(self):
        print('''~~ Guess The Number Game ~~
You have to choose a number between 1 and 10.
If your guess is correct, you win!
You have 3 chances to guess correctly — or you lose.

Enjoy!!! 🎮\n''')

    def user_input(self):
        """Safely get and validate user input"""
        while True:
            try:
                print(f'You have {self.__chances} chances left.\n')
                guess = int(input('Guess The Number: '))
                if guess not in range(1, 11):
                    print('⚠️ Please choose a number between 1 and 10.\n')
                    continue
                return guess
            except ValueError:
                print('❌ Invalid input! Please enter an integer.\n')

    def play(self):
        while self.__chances > 0:
            guess = self.user_input()
            if guess == self.num:
                print(f"🎉 You Won!! The number was {self.num}")
                break
            else:
                self.__chances -= 1
                print('❌ Incorrect Guess!')
                if self.__chances > 0:
                    if self.num > guess:
                        print('💡 Hint: The number is GREATER than your guess.\n')
                    else:
                        print('💡 Hint: The number is SMALLER than your guess.\n')
                else:
                    print(f"💀 Game Over! The number was {self.num}.\n")
                    break
                