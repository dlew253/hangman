import random
#set word list
def get_word():
  words = [
    "kitty",
    "baseball",
    "poop",
    "apple",
    "coffee",
    "draco",
    "sharpen",
    "gourd",
    "noodle",
    "sharpie",
    "hoarse"]
  return random.choice(words)
# set up game field
def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 7
  print("Let's play hangman!")
  print(display_hangman(tries))
  print("\n")

  #guess funtionality
  while not guessed and tries > 0:
    guess = input("Please guess a letter or word: ").upper()
    if len(guess) == 1 and guess.isalpha():
#letter already guessed
        if guess in guessed_letters:
          print("You already guessed the letter", guess) 
        elif guess not in word:
#wrong letter
          print(guess, "is not in the word.")
          tries -= 1
          guessed_letters.append(guess)
        else:
#correct guess              
          print(guess, "is correct")
          guessed_letters.append(guess)
          word_as_list = list(word_completion)
          indices = [i for i, letter in enumerate(word) if letter == guess]
          print(indices)
          for index in indices:
            word_as_list[index] = guess
          word_completion = "".join(word_as_list)
          if "_" not in word_completion:
            guessed = True
#same char guess
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("you already tried that one", guess)
#incorrect word guess
      elif guess != word:
        print(guess, "isnt the word")  
        tries -= 1
        guessed_words.append(guess)
#word is true
      else:
        guessed = True
        word_completion = word   
#invalid guess     
    else: 
      print("Not a valid guess")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
#win
  if guessed:
    print("WOOOOOOO!, you guessed it, YOU WIN")
#lose
  else:
    print("Sorry old chap, you've died. The word was " + word + ". Maybe next time!")

#game board
def display_hangman(tries):
    board = ['''

       |=====|
       0     |
      \\|/    |
       |     |
      / \\    |
         ____|____''','''

       |=====|
       0     |
      \\|/    |
       |     |
      /      |
         ____|____''','''

       |=====|
       0     |
      \\|/    |
       |     |
             |
         ____|____
         ''','''

       |=====|
       0     |
      \\|/    |
             |
             |
         ____|____
         ''','''

       |=====|
       0     |
      \\|     |
             |
             |
         ____|____
         ''','''

       |=====|
       0     |
       |     |
             |
             |
         ____|____
         ''','''

       |=====|
       0     |
             |
             |
             |
         ____|____
         ''','''

       |=====|
             |
             |
             |
             |
         ____|____
         ''']
    return board[tries]

#restart function
def main():
  word = get_word()
  play(word)
  while input("Play Again (Y/N) ").upper() == "Y":
    word = get_word()
    play(word)

if __name__ == "__main__":
  main()

# shoutout to this vid for the guide https://www.youtube.com/watch?v=m4nEnsavl6w