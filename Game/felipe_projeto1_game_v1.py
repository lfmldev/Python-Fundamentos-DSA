# Projeto 01 - Desenvolvimento de Game em Python - V1

# Importando pacotes

import random # utilizado para escolher a palavra de maneira aleatória
from os import system, name # serve para identificar o sistema operacional

# Função para limpar a tela de execução

def limpa_tela():

	# Windows
	if name == 'nt': 
		_= system('cls') # o underline serve para liberar o return da função system, 
						 # não precisamos do return só do resultado
	# Mac ou Linux
	else:
		-=system('clear')

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
	tentativas = 6

	# Lista para as letras erradas
	letras_erradas = []

	# Loop enquanto para definir o limite de tentativas
	while tentativas > 0:
		# Prints de tela para o usuário
		print(" ".)
		pass











