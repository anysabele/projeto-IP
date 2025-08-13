import pygame 
pygame.init()

LARGURA, ALTURA = 800, 600  # Tamanho da tela do jogo
fundo_img = pygame.image.load('imagens/tela/fundo_jogo.png')
fundo_img = pygame.transform.scale(fundo_img, (LARGURA, ALTURA))
TELA = pygame.display.set_mode((LARGURA, ALTURA))  # Cria a janela do jogo
pygame.display.set_caption("Seis Tiros no Oeste")  # Título da janela
RELOGIO = pygame.time.Clock()  # Controla a velocidade do jogo
FONTE = pygame.font.SysFont("arial", 40)  # Fonte para textos
PONTOS = 0  # Contador de Pontos
VIDAS = 3  # Vidas iniciais (não usado diretamente)

# Carrega e redimensiona a imagem do coração (vida)
coracao_img = pygame.image.load("imagens/objetos/medalha_xerif.png").convert_alpha()
coracao_img = pygame.transform.scale(coracao_img, (30, 30))