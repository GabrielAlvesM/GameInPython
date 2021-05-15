import random

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:

  def __init__(self, word):
    self.word = word
    self.missed_letters = []
    self.guessed_letters = []
      
  def guess(self, letter):
    if letter in self.word and letter not in self.guessed_letters:
      self.guessed_letters.append(letter)
    elif letter not in self.word and letter not in self.missed_letters:
      self.missed_letters.append(letter)
    else:
      return False
    return True

  def hangman_over(self):
    return self.hangman_won() or (len(self.missed_letters) == 6)
  
  def hangman_won(self):
    if '_' not in self.hide_word():
      return True
    return False
  
  def hide_word(self):
    rtn = ''
    for letter in self.word:
      if letter not in self.guessed_letters:
        rtn += '_'
      else:
        rtn += letter
    return rtn
  
  def print_game(self):
    print(board[len(self.missed_letters)])
    print('\nPalavra: '+ self.hide_word())
    print('\nErros: ',)
    for letter in self.missed_letters:
      print(letter, )
    print()
    print('Acertos: ',)
    for letter in self.guessed_letters:
      print(letter,)
    print()
  
def rand_word():
  with open('palavras.txt', "rt") as f:
    bank = f.readlines()
  return bank[random.randint(0,len(bank))].strip()

def main():

  game = Hangman(rand_word())

  while not game.hangman_over():
    game.print_game()
    user_input = input('\nEntre com uma letra: ')
    game.guess(user_input)

  game.print_game()

  if game.hangman_won():
    print('\nParabens! Vc ganhou!!')
  else:
    print('\nGame Over!!!')
    print('Palavra certa: '+ game.word)

if __name__ == '__main__':
  main()