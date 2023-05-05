# Projeto 01 - Desenvolvimento de Game em Python - V1

# Importando pacotes

import random 								# utilizado para escolher a palavra de maneira aleatória
from os import system, name 				# serve para identificar o sistema operacional

# Função para limpar a tela de execução

def limpa_tela():

	# Windows
	if name == 'nt': 
		_= system('cls') 					# o underline serve para liberar o return da função system, 
						 					# não precisamos do return só do resultado
	# Mac ou Linux
	else:
		_= system('clear')

# Função para o Game

def game():

	limpa_tela()

	print("\n Bem-vindo ao jogo da forca, João!")
	print("Duvido você conseguir adivinhar a palavra abaixo:\n")

	# Lista de palavras para o jogo
	palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

	# Escolha aleatória de palavras
	palavra = random.choice(palavras)

	# Exibir o underline de acordo com o tamanho da palavra
	letras_descobertas = ['_' for letras in palavra]

	# Número de tentativas
	chances = 6

	# Lista para as letras erradas
	letras_erradas = []

	# Loop enquanto o número de chances for maior que zero
	while chances > 0:
		# Prints de tela para o usuário
		print(" ".join(letras_descobertas)) 				# junção, vai juntar o espaço as letras descobertas
		print("\nTentativas restantes: ", chances) 			# n° de chances
		print("Letras erradas:", " ".join(letras_erradas)) 	# junção das letras erradas

		# Tentativas
		tentativa = input("\nDigite uma letra: ").lower() 	# Recebo o input do usuário e defino como minúsculo

		# Condicional para verificar a existência da letra na palavra

		if tentativa in palavra: 							# se a letra estiver na palavra
			index = 0  										# cria um index zerado
			for letra in palavra: 							# para cada letra na palavra
				if tentativa == letra:  					# se a letra ecolhida for igual a letra da palavra
					letras_descobertas[index] = letra 		# coloco a letra descoberta no índice da letra e retiro o "_"
				index += 1									# incremento o índice a cada loop

		else: 												# Se não estiver na palavra
			chances -= 1  									# Decremento das chances
			letras_erradas.append(tentativa)				# e faço um append na lista criada para as letras erradas

		# Condicional para terminar o game
		if "_" not in letras_descobertas:					# se não tiver mais underscore nas letras descobertas
			print("\nVocê venceu, a palavra é: ", palavra)  # Print
			break											# Break, para o programa
	
	# Condicional caso o número de chances excedida
	if "_" in letras_descobertas:
		print("\nVocê perdeu, a palavra era:", palavra)


# Bloco main, serve para dizer ao interpretador que isso é um programa, um módulo python
if __name__ == "__main__":
	game()
	print("\nParabéns. Você está aprendendo ao programar!! :)\n")
