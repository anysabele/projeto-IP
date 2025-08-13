# Importa as bibliotecas necessárias
import pygame  # Biblioteca para criar jogos
from random import randint  # Para gerar números aleatórios
import sprites  # Arquivo com imagens do jogo

# Inicializa o pygame (prepara para usar seus recursos)
pygame.init()

# ----------------- CONFIGURAÇÕES GERAIS -----------------
LARGURA, ALTURA = 800, 600  # Tamanho da tela do jogo
TELA = pygame.display.set_mode((LARGURA, ALTURA))  # Cria a janela do jogo
pygame.display.set_caption("Seis Tiros no Oeste")  # Título da janela
RELOGIO = pygame.time.Clock()  # Controla a velocidade do jogo
FONTE = pygame.font.SysFont("arial", 40)  # Fonte para textos
ABATES = 0  # Contador de abates (não usado diretamente)
VIDAS = 3  # Vidas iniciais (não usado diretamente)

# Carrega e redimensiona a imagem do coração (vida)
coracao_img = pygame.image.load("imagens/objetos/medalha_xerif.png").convert_alpha()
coracao_img = pygame.transform.scale(coracao_img, (30, 30))

# ----------------- CLASSES -----------------
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
        self.vidas = 3  # Quantidade de vidas
        self.abates = 0  # Contador de inimigos derrotados
        self.ultimo_dano = 0  # Quando levou dano pela última vez
        self.invencibilidade = 1000  # Tempo imune após levar dano (ms)
        self.cowboy_andando_img = sprites.cowboy  # Imagem andando
        self.cowboy_atirando_img = sprites.atirando  # Imagem atirando

    def mover(self, teclas):
        # Move o cowboy baseado nas teclas pressionadas
        # Setas ou WASD para movimentação
        if teclas[pygame.K_UP] and self.y > 0:  # Move para cima
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.y < ALTURA - self.altura:  # Move para baixo
            self.y += self.velocidade
        if teclas[pygame.K_LEFT] and self.x > 0:  # Move para esquerda
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.x < LARGURA - self.largura:  # Move para direita
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
            self.vidas -= 1  # Perde uma vida
            self.ultimo_dano = agora  # Marca o momento do dano

    def atirar(self):
        # Dispara um novo projétil se o intervalo entre tiros foi respeitado
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_tiro >= self.intervalo_tiro:
            self.projeteis.append([self.x + self.largura, self.y + self.altura // 2])  # Adiciona novo tiro
            self.ultimo_tiro = tempo_atual  # Marca o momento do tiro

    def atualizar_projeteis(self):
        # Move os tiros e remove os que saíram da tela
        nova_lista = []
        for tiro in self.projeteis:
            tiro[0] += self.velocidade_tiro  # Move o tiro para frente
            if tiro[0] < LARGURA:  # Se ainda está na tela
                nova_lista.append(tiro)
        self.projeteis = nova_lista  # Atualiza a lista de tiros

    def desenhar(self):
        # Desenha o cowboy, seus tiros, vidas e contador de abates
        self.cowboy_atirando_img.update()
        TELA.blit(self.cowboy_atirando_img.image, (self.x, self.y))  # Imagem do cowboy
        for tiro in self.projeteis:  # Desenha todos os tiros
            pygame.draw.rect(TELA, (0, 0, 0), (tiro[0] + 10, tiro[1] + 22, 10, 5))
        for v in range(self.vidas):  # Desenha as vidas (corações)
            TELA.blit(coracao_img, (10 + v * 35, 10))
        
        # Mostra quantos inimigos foram abatidos
        texto = FONTE.render(f"Abates: {self.abates}", True, (0, 0, 0))
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
        self.largura = 40  # Largura do inimigo
        self.altura = 40  # Altura do inimigo
        self.bandido_andando_img = sprites.bandido_andando  # Imagem andando
        self.bandido_atacando_img = sprites.bandido_tnt  # Imagem atacando

    def reaparecer(self):
        # Faz o inimigo aparecer se for a hora
        tempo_atual = pygame.time.get_ticks()
        if not self.ativo and tempo_atual >= self.respawn:
            self.posicao = [randint(800, 900), randint(50, 550)]  # Posição aleatória
            self.velocidade_y = randint(-2, 2) or 1  # Velocidade vertical aleatória
            self.ativo = True  # Agora está ativo

    def mover(self, cowboy):
        # Move o inimigo e verifica colisões com bordas
        if self.ativo:
            # Movimento horizontal (para esquerda)
            self.posicao[0] -= self.velocidade_x
            
            # Movimento vertical (quica nas bordas)
            self.posicao[1] += self.velocidade_y
            if self.posicao[1] <= 0 or self.posicao[1] >= ALTURA - self.altura:
                self.velocidade_y *= -1  # Inverte a direção

            # Se sair pela esquerda, causa dano ao cowboy
            if self.posicao[0] <= 0:
                cowboy.vidas -= 1  # Cowboy perde vida
                self.ativo = False  # Inimigo desaparece
                self.projeteis.clear()  # Limpa seus tiros
                min_t, max_t = self.intervalo
                self.respawn = pygame.time.get_ticks() + randint(min_t, max_t)  # Marca novo respawn

    def atirar(self):
        # Inimigo dispara tiros
        tempo_atual = pygame.time.get_ticks()
        if self.posicao and self.posicao[0] < LARGURA - 40:  # Se está na tela
            if tempo_atual - self.ultimo_tiro >= self.intervalo_tiro:  # Se pode atirar
                self.projeteis.append([self.posicao[0], self.posicao[1] + self.altura // 2])  # Novo tiro
                self.ultimo_tiro = tempo_atual  # Marca o momento do tiro

    def atualizar_projeteis(self, cowboy):
        # Move e verifica colisões dos tiros do inimigo
        nova_lista = []
        for tiro in self.projeteis:
            tiro[0] -= self.velocidade_tiro  # Move o tiro (para esquerda)
            if tiro[0] > 0:  # Se ainda está na tela
                nova_lista.append(tiro)
            # Verifica se acertou o cowboy
            if pygame.Rect(tiro[0], tiro[1], 10, 5).colliderect(cowboy.get_rect()):
                cowboy.levar_dano()  # Cowboy leva dano
        self.projeteis = nova_lista  # Atualiza lista de tiros

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
   
class Drop:
    def __init__(self, cor, posicao):
        # Itens que podem ser coletados (power-ups)
        self.cor = cor  # Cor do drop
        self.posicao = posicao  # Posição na tela
        self.raio = 8  # Tamanho do drop

    def desenhar(self):
        # Desenha o drop como um círculo
        pygame.draw.circle(TELA, self.cor, (self.posicao[0], self.posicao[1]), self.raio)

    def get_rect(self):
        # Retorna retângulo para colisões
        return pygame.Rect(self.posicao[0] - self.raio, self.posicao[1] - self.raio, self.raio*2, self.raio*2)

def tela_game_over():
    # Mostra a tela de fim de jogo
    fonte_titulo = pygame.font.Font(None, 80)  # Fonte grande
    fonte_botao = pygame.font.Font(None, 50)  # Fonte menor
    jogando = True
    
    fundo_original = pygame.image.load('imagens/tela/game_over.jpg').convert()
    fundo_game_over = pygame.transform.scale(fundo_original, (LARGURA, ALTURA))
    
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
   
# ----------------- FUNÇÃO PRINCIPAL -----------------
def main():
    # Configuração inicial do jogo
    cowboy = Cowboy(100, 100)  # Cria o cowboy
    # Cria 3 tipos de inimigos com características diferentes
    inimigos = [
        Inimigo((255, 0, 0), 2, (1000, 3000)),  # Vermelho - mais rápido
        Inimigo((0, 255, 0), 3, (2000, 5000)),  # Verde - velocidade média
        Inimigo((0, 0, 255), 4, (4000, 8000))   # Azul - mais lento
    ]
    drops = []  # Lista de power-ups
    tipos_drops = [(255, 0, 0), (0, 0, 255)]  # Tipos de power-ups
    fim_de_jogo = False  # Controla o loop do jogo

    # Loop principal do jogo
    while not fim_de_jogo:
        # Verifica eventos (como fechar a janela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = True

        # Movimentação e ações do cowboy
        teclas = pygame.key.get_pressed()  # Teclas pressionadas
        cowboy.mover(teclas)  # Move o cowboy
        cowboy.atirar()  # Verifica se atira
        cowboy.atualizar_projeteis()  # Atualiza tiros do cowboy

        # Atualiza todos os inimigos
        for inimigo in inimigos:
            inimigo.reaparecer()  # Faz aparecer se for hora
            if inimigo.ativo:  # Se está ativo
                inimigo.mover(cowboy)  # Move o inimigo
                inimigo.atirar()  # Inimigo atira
                inimigo.atualizar_projeteis(cowboy)  # Atualiza tiros do inimigo

                # Verifica colisão dos tiros do cowboy com inimigos
                for tiro in cowboy.projeteis[:]:
                    if pygame.Rect(tiro[0], tiro[1], 10, 5).colliderect(inimigo.get_rect()):
                        # Inimigo é atingido
                        inimigo.ativo = False
                        inimigo.projeteis.clear()
                        min_t, max_t = inimigo.intervalo
                        inimigo.respawn = pygame.time.get_ticks() + randint(min_t, max_t)
                        cowboy.abates += 1  # Aumenta contador de abates
                        cowboy.projeteis.remove(tiro)  # Remove o tiro
                        
                        # Chance de 10% de dropar um power-up
                        if randint(1, 100) <= 10:
                            cor = tipos_drops[randint(0, len(tipos_drops) - 1)]
                            drops.append(Drop(cor, inimigo.posicao[:]))

        # Atualiza power-ups
        for drop in drops[:]:
            drop.desenhar()  # Desenha o power-up
            # Verifica se o cowboy pegou
            if cowboy.get_rect().colliderect(drop.get_rect()):
                drops.remove(drop)  # Remove o power-up
                # Melhora a taxa de tiro do cowboy
                cowboy.intervalo_tiro = max(100, cowboy.intervalo_tiro - 150)

        # Desenha tudo na tela
        TELA.fill((255, 255, 255))  # Fundo branco
        cowboy.desenhar()  # Desenha o cowboy
        for inimigo in inimigos:  # Desenha todos os inimigos
            inimigo.desenhar()

        pygame.display.flip()  # Atualiza a tela
        RELOGIO.tick(60)  # Mantém 60 FPS

        # Verifica se o cowboy perdeu todas as vidas
        if cowboy.vidas <= 0:
            tela_game_over()  # Mostra tela de game over
            return main()  # Reinicia o jogo

    pygame.quit()  # Fecha o jogo

# Inicia o jogo quando o arquivo é executado
if __name__ == "__main__":
    main()