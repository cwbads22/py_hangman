# -- Coding: utf-8 --
# HangMan - Jogo da Forca
# Programação Orientada a Objetos - Curso Fundamentos em Análise de Dasos 3.0 DSA
# https://www.datascienceacademy.com.br

# importar biblioteca Random para fazer a seleção aleatória das palavras do banco txt.
import random

# lista com as parted do boneco acrescentadas após cada erro.
body_parts = [" ","cabeca", "corpo", "braco esquerdo", "braco direito", "perna esquerda", "perna direita", "MORREU!"]

# Classe
class Hangman:

  def __init__(self, word):          # Construtor
    self.word = word
    self.missed_letters = []
    self.guessed_letters = []
    
  def guess(self, letter):           # Adivinhar a letra
    if letter in self.word and letter not in self.guessed_letters:
      self.guessed_letters.append(letter)
    elif letter not in self.word and letter not in self.missed_letters:
      self.missed_letters.append(letter)
    else:
      return False
    return True
  
  def hangman_over(self):            # Verificar se o jogo acabou
    return self.hangman_won() or (len(self.missed_letters) == 7)
    
  def hangman_won(self):             # Verificar se o jogador venceu
    if '_' not in self.hide_word():
      return True
    return False
  
  def hide_word(self):               # Não mostrar a letra no tabuleiro
    rtn = ''
    for letter in self.word:
      if letter not in self.guessed_letters:
        rtn += '_'
      else:
        rtn += letter
    return rtn
  
  def print_game_status(self):       # checar o status e imprimir o board
    print(body_parts[len(self.missed_letters)])
    print("\n Palavras: " + self.hide_word())
    print("\n Letras erradas: ",)
    for letter in self.missed_letters:
      print(letter,)
    print()
    print("Letras corretas: ",)
    for letter in self.guessed_letters:
      print(letter,)
    print()
    
def rand_word():
  with open("words.txt", "rt") as f:
    bank = f.readlines()
  return bank[random.randint(0, len(bank))].strip()

# print(rand_word())
def main():
  
  game = Hangman(rand_word())          # Objeto

  while not game.hangman_over():       # printa status, pede letra e leitura
    game.print_game_status()
    user_input = input("\n Digite uma letra: ")
    game.guess(user_input)

  game.print_game_status()             # Verifica o status

  if game.hangman_won():               # imprime msg conforme status 
    print("\nParabéns, você venceu!")
  else:
    print("\nGame Over - Você morreu!")
    print("A palavra era: " + game.word)

  print("\nFoi bom jogar com você! Agora vá estudar!!!")

# Executa o programa
if __name__ == "__main__":
  main()
