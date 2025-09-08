import random

# Hangman stages
stages = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]

# Word list
word_list = ["apple", "beautiful", "potato"]
chosen_word = random.choice(word_list)
display = ['_' for _ in chosen_word]

lives = 6
game_over = False

while not game_over:
    print(' '.join(display))
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = guess
    else:
        lives -= 1
        print("Wrong guess!")
    
    print(stages[lives])

    if '_' not in display:
        game_over = True
        print("You win!")
    elif lives == 0:
        game_over = True
        print(f"You lose! The word was '{chosen_word}'")
