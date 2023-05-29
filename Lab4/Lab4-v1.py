# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Função para limar a tela a cada execução, podemos criar funções fora das classes em python!!!
# Pois ela pode ser uma atividade separada ou específica das principais funções da classe

def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# Board (tabuleiro) uma lista em python

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


# Classe, como um template que diz o que o nosso programa deve fazer
class Hangman:

	# Método Construtor
     # 
     def __init__(self, palavra):
          self.palavra = palavra
          self.letras_erradas = []
          self.letras_escolhidas = []


	# Método para adivinhar a letra

     def guess(self, letra):

          if letra in self.palavra and letra not in self.letras_escolhidas:
               self.letras_escolhidas.append(letra)
          elif letra not in self.palavra and letra not in self.letras_erradas:
               self.letras_erradas.append(letra)
          else:
               return False
          return True

	# Método para verificar se o jogo terminou
     # Ele irá chamar outro método da mesma classe

     def hangman_over(self):
          return self.hangman_won() or (len(self.letras_erradas) == 6) # 6 tentativas erradas!!


	# Método para verificar se o jogador venceu
     # verifica se há ainda na palavra o underline

     def hangman_won(self):

          if '_' not in self.hide_palavra():
               return True
          return False

	# Método para não mostrar a letra no board
     def hide_palavra(self):
          rtn = ''

          for letra in self.palavra:
               if letra not in self.letras_escolhidas:
                    rtn += '_'
               else:
                    rtn += letra
          return rtn

     
	# Método para checar o status do game e imprimir o board na tela

     def print_game_status(self):
          print(board[len(self.letras_erradas)]) # Imprime o tabuleiro de acordo com o n° de tentativas seguindo o index

          print('\nPalavra ' + self.hide_palavra()) # Vai nos mostrar a palavra escondida

          print('\nLetras erradas', ) # Vai nos mostrar as letras erradas

          for letra in self.letras_erradas: # Se estiver em letras erradas ele imprimirá este loop
               print(letra,)

          print()

          print('Letras corretas: ',)

          for letra in self.letras_escolhidas: # Se estiver em letras certas ele imprimirá este loop
               print(letra,)

          print()


# Método para ler de forma ramdomica um conjunto de palavras
def rand_palavra():
     # Lista de palavras para o jogo
     palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

     # Escolhe uma palavra de forma aleatória
     palavra = random.choice(palavras) # Choose a random element from a non-empty sequence.(ramdom package)

     return palavra

# Main é o método que vais executar o nosso programa
# É nele que são chamadas as funções e métodos da classe criada
def main():

     limpa_tela()

     # Cria o objeto e seleciona uma palavra de forma ramdomica
     # Neste caso criou-se uma instância da classe que solicita como parâmentro uma palavra no método construtor
     # Recebe a palavra e cria duas listas vazias

     game = Hangman(rand_palavra())

     # Enquanto o jogo não estiver terminado, faz-se print do status, solicita uma letra e faz a leitura do caractere

     while not game.hangman_over(): # Enquanto hangman_over não for veradeiro eu continuo o loop while

          # Status do game
          game.print_game_status()

          # Recebe o input do terminal
          user_input = input('\nDigite uma letra: ')

          # verifica se a letra digitada faz parte da palavra
          game.guess(user_input)

     # Verifica o status do jogo
     game.print_game_status()

     # De acordo com o status imprime uma mensagem na tela:

     if game.hangman_won():
          print('\nParabéns! Você venceu!!')
     else:
          print('\nGame Over! Você perdeu!')
          print('A palavra era '+ game.palavra)
     print('\nFoi bom jogar com você, agora volte a estudar!!\n')

# Executa o programa:

if __name__ =="__main__":
     main()

