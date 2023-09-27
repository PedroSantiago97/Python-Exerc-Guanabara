import pygame

pygame.init() # INICIA o pugame
pygame.mixer.music.load('ex01.mp3') # Carrega o arquivo de audio .mp3
pygame.mixer.music.play() # Inicia a reprodução do arquivo
input()
pygame.event.wait() # Espera após finalizar a reprodução

# Estudo da biblioteca pygame
# Artificio de reprodução de Audio
