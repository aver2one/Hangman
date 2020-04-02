import random

words = [
    "ship",
    "pirate",
    "baseball",
    "gate",
    "dog",
    "frog",
    "computer",
    "tent",
    "keyboard",
    "mouse",
    "pen",
    "game",
    "internet",
    "football",
    "door",
    "tooth",
]

word = random.choice(words)
word_list = [letter for letter in word]
guesses = 6
correct = []
incorrect = []


def correct_guess(guess):
    while guess in word_list:
        correct.append(guess)
        word_list.remove(guess)


def incorrect_guess(guess):
    incorrect.append(guess)
    global guesses
    guesses -= 1
    print("\n\nSorry, the letter {} is not in the word.".format(guess))


def status():
    print(
        f"""\nThe word has {len(word_list)} unguessed letter(s).
        * Remaining incorrect guesses: {guesses}
        * Correct letters guessed: {correct}
        * Wrong letters guessed: {incorrect}"""
    )


def get_guess():
    while True:
        try:
            guess = input("Guess a letter: ")
            guess = guess.lower()
            if len(guess) != 1:
                raise ValueError
                break
            else:
                return guess
        except ValueError:
            print("\n\nSorry one letter is the only acceptable input")


def play_game():
    guess = get_guess()
    while guesses >= 0:
        if guess in word_list:
            correct_guess(guess)
            print(
                "\n\nYou guessed correct, the letter "
                "{} appears {} time(s).".format(guess, correct.count(guess))
            )
            if len(word_list) != 0:
                status()
                guess = get_guess()
            else:
                print("\n\nYou won!!!!! The word was: {}".format(word))
                exit()
        else:
            if guesses > 0:
                incorrect_guess(guess)
                status()
                guess = get_guess()
            else:
                print(
                    "\n\nGame Over, try again! You were so close,"
                    " the word was {}.".format(word)
                )
                exit()


if __name__ == "__main__":
    status()
    play_game()
