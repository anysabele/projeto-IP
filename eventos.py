import pygame
from pygame.locals import *
from sprites import *
from config import *
from random import randint
import math
pygame.init()

class Cowboy:
    def __init__(self, x, y, cor=(255, 0, 0)):
        # Configurações iniciais do cowboy
        self.x = x  # Posição X inicial
        self.y = y  # Posição Y inicial
        self.velocidade = 15  # Quão rápido ele se move
        self.cor = cor  # Cor (não usado com imagens)
        self.largura = 50  # Largura do cowboy
        self.altura = 50  # Altura do cowboy
        self.projeteis = []  # Lista de tiros disparados
        self.velocidade_tiro = 30  # Velocidade dos tiros
        self.intervalo_tiro = 300  # Tempo entre tiros (ms)
        self.ultimo_tiro = 0  # Quando atirou pela última vez
        self.pontos = 0
        self.vidas = 3  # Quantidade de vidas
        self.abates = 0  # Contador de inimigos derrotados
        self.ultimo_dano = 0  # Quando levou dano pela última vez
        self.invencibilidade = 1000  # Tempo imune após levar dano (ms)
        self.cowboy_andando_img = cowboy  # Imagem andando
        self.cowboy_atirando_img = atirando  # Imagem atirando

    def mover(self, teclas):
        # Move o cowboy baseado nas teclas pressionadas
        # Setas ou WASD para movimentação
        if teclas[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.y < ALTURA - self.altura:
            self.y += self.velocidade
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.x < LARGURA - self.largura:
            self.x += self.velocidade

        # Teclas WASD (alternativas)
        if teclas[pygame.K_w] and self.y > 0:
            self.y -= self.velocidade
        if teclas[pygame.K_s] and self.y < ALTURA - self.altura:
            self.y += self.velocidade
        if teclas[pygame.K_a] and self.x > 0:
            self.x -= self.velocidade
        if teclas[pygame.K_d] and self.x < LARGURA - self.largura:
            self.x += self.velocidade

    def levar_dano(self):
        # Verifica se pode levar dano (não está no tempo de invencibilidade)
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_dano >= self.invencibilidade:
            self.vidas -= 1
            self.ultimo_dano = agora

    def atirar(self):
        # Dispara um novo projétil se o intervalo entre tiros foi respeitado
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_tiro >= self.intervalo_tiro:
            self.projeteis.append([self.x + self.largura, self.y + self.altura // 2])
            self.ultimo_tiro = tempo_atual

    def atualizar_projeteis(self):
        # Move os tiros e remove os que saíram da tela
        nova_lista = []
        for tiro in self.projeteis:
            tiro[0] += self.velocidade_tiro
            if tiro[0] < LARGURA:
                nova_lista.append(tiro)
        self.projeteis = nova_lista

    def desenhar(self):
        # Desenha o cowboy, seus tiros, vidas e contador de abates
        self.cowboy_atirando_img.update()
        TELA.blit(self.cowboy_atirando_img.image, (self.x, self.y))  # Imagem do cowboy
        for tiro in self.projeteis:
            pygame.draw.rect(TELA, (0, 0, 0), (tiro[0], tiro[1], 10, 5))
            pygame.mixer.music.load('sons_jogo/sequencia_tiro_som.wav')
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(loops=-1)
        for v in range(self.vidas):
            TELA.blit(coracao_img, (10 + v * 35, 10))

        # Mostra a quantidade de pontos
        texto = FONTE.render(f"Pontos: {self.pontos}", True, (0, 0, 0))
        TELA.blit(texto, (600, 0))

    def get_rect(self):
        # Retorna um retângulo que representa a área do cowboy (para colisões)
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
    
class Inimigo:
    def __init__(self, cor, velocidade_x, intervalo_respawn):
        # Configurações iniciais do inimigo
        self.cor = cor  # Cor do inimigo
        self.posicao = None  # Posição atual (começa inexistente)
        self.ativo = False  # Se está na tela ou não
        self.respawn = pygame.time.get_ticks() + intervalo_respawn[0]  # Quando vai aparecer
        self.intervalo = intervalo_respawn  # Intervalo entre aparições
        self.velocidade_x = velocidade_x  # Velocidade horizontal
        self.velocidade_y = randint(-2, 2) or 1  # Velocidade vertical (aleatória)
        self.projeteis = []  # Lista de tiros do inimigo
        self.velocidade_tiro = 10  # Velocidade dos tiros
        self.intervalo_tiro = 200  # Tempo entre tiros
        self.ultimo_tiro = 0  # Quando atirou pela última vez
        self.largura = 50  # Largura do inimigo
        self.altura = 50  # Altura do inimigo
        self.bandido_andando_img = bandido_andando  # Imagem andando
        self.bandido_atacando_img = bandido_tnt  # Imagem atacando

    def reaparecer(self):
        # Faz o inimigo aparecer se for a hora
        tempo_atual = pygame.time.get_ticks()
        if not self.ativo and tempo_atual >= self.respawn:
            self.posicao = [randint(800, 900), randint(50, 550)] # Posição aleatória
            self.velocidade_y = randint(-2, 2) or 1 # Velocidade vertical aleatória
            self.ativo = True

    def mover(self, cowboy):
        # Move o inimigo e verifica colisões com bordas
        if self.ativo:
            # Movimento X (horizontal)
            self.posicao[0] -= self.velocidade_x

            # Movimento Y com ricochete
            self.posicao[1] += self.velocidade_y
            if self.posicao[1] <= 0 or self.posicao[1] >= ALTURA - self.altura:
                self.velocidade_y *= -1

            # Se encostar na borda esquerda
            if self.posicao[0] <= 0:
                self.ativo = False
                self.projeteis.clear()
                min_t, max_t = self.intervalo
                self.respawn = pygame.time.get_ticks() + randint(min_t, max_t)

    def atirar(self):
        # Inimigo dispara tiros
        tempo_atual = pygame.time.get_ticks()
        if self.posicao and self.posicao[0] < LARGURA - 40:
            if tempo_atual - self.ultimo_tiro >= self.intervalo_tiro:
                self.projeteis.append([self.posicao[0], self.posicao[1] + self.altura // 2])
                self.ultimo_tiro = tempo_atual

    def atualizar_projeteis(self, cowboy):
        nova_lista = []
        for tiro in self.projeteis:
            tiro[0] -= self.velocidade_tiro
            if tiro[0] > 0:
                nova_lista.append(tiro)
            if pygame.Rect(tiro[0], tiro[1], 10, 5).colliderect(cowboy.get_rect()):
                pygame.mixer.music.load('sons_jogo/dano_som.wav')
                pygame.mixer.music.set_volume(20)
                pygame.mixer.music.play(loops=-1)
                cowboy.levar_dano()
                self.projeteis.remove(tiro) #apaga o tiro depois de atingir o cowboy

        self.projeteis = nova_lista

    def desenhar(self):
        # Desenha o inimigo e seus tiros
        if self.ativo:
            self.bandido_atacando_img.update()
            TELA.blit(self.bandido_atacando_img.image, (self.posicao[0], self.posicao[1]))
            for tiro in self.projeteis:
                pygame.draw.rect(TELA, (255, 0, 0), (tiro[0] , tiro[1] + 25, 10, 5))

    def get_rect(self):
        # Retorna retângulo para colisões
        return pygame.Rect(self.posicao[0], self.posicao[1], self.largura, self.altura)

class Bau:
    def __init__(self, posicao):
        self.largura = 100
        self.altura = 80
        self.posicao = posicao
        self.ativo = True
        self.bau_img = pygame.image.load('imagens/objetos/bau_fechado.png')

    def desenhar(self):
        if self.ativo:
            pulsar = 1 + 0.05 * math.sin(pygame.time.get_ticks() * 0.005)
            img = pygame.transform.scale(self.bau_img, 
                           (int(self.largura * pulsar), 
                            int(self.altura * pulsar)))
            TELA.blit(img, (self.posicao[0]-5*pulsar, self.posicao[1]-5*pulsar))

    def get_rect(self):
        return pygame.Rect(self.posicao[0], self.posicao[1], self.largura, self.altura)

class Drop:
    def __init__(self, cor, efeito, posicao):
        self.cor = cor
        self.efeito = efeito
        self.posicao = posicao
        self.raio = 8


    def get_rect(self):
        return pygame.Rect(self.posicao[0] - self.raio, self.posicao[1] - self.raio, self.raio*2, self.raio*2)

    

def tela_game_over():
    # Mostra a tela de fim de jogo
    fonte_titulo = pygame.font.Font(None, 80)  # Fonte grande
    fonte_botao = pygame.font.Font(None, 50)  # Fonte menor
    
    fundo_original = pygame.image.load('imagens/tela/game_over.jpg').convert()
    fundo_game_over = pygame.transform.scale(fundo_original, (LARGURA, ALTURA))
    #som
    pygame.mixer.music.load('sons_jogo/country_som.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=-1)

    jogando = True
    while jogando:
        TELA.blit(fundo_game_over, (0,0))

       # Texto "GAME OVER"
        texto = fonte_titulo.render("GAME OVER", True, (255, 0, 0))
        rect_texto = texto.get_rect(center=(LARGURA // 2, ALTURA // 3))
        
        TELA.blit(texto, rect_texto)

        # Botão "Jogar Novamente"
        texto_botao = fonte_botao.render("Jogar Novamente", True, (255, 255, 255))
        rect_botao = texto_botao.get_rect(center=(LARGURA // 2, ALTURA // 2))
        pygame.draw.rect(TELA, (0, 128, 0), rect_botao.inflate(20, 10))  # Desenha botão
        TELA.blit(texto_botao, rect_botao)

        # Verifica eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Se clicar para fechar
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Se clicar no botão
                if rect_botao.collidepoint(event.pos):
                    return  # Volta para o jogo

        pygame.display.flip()  # Atualiza a tela
        RELOGIO.tick(60)  # 60 FPS
    