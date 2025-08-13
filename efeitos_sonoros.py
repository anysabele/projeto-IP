import pygame

pygame.init()
pygame.mixer.init()

tiro_som = pygame.mixer.Sound('sons_jogo/um_tiro_so_2.wav')

sequencia_tiro_som = pygame.mixer.Sound('sons_jogo/sequencia_tiro_som.wav')

dano_som = pygame.mixer.Sound('sons_jogo/dano_som.wav')

game_over_som = pygame.mixer.Sound('sons_jogo/game_over.wav')

#musica padrao
pygame.mixer.music.load('sons_jogo/country_som.mp3')