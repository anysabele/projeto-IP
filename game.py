# Importa as bibliotecas necessárias
import pygame  # Biblioteca para criar jogos
from random import randint  # Para gerar números aleatórios
from config import *
from eventos import *

# Inicializa o pygame (prepara para usar seus recursos)
pygame.init()


# ----------------- FUNÇÃO PRINCIPAL -----------------
def main():
    cowboy = Cowboy(100, 100)
    inimigos = [
        Inimigo((255, 0, 0), 2, (1000, 3000)),
        Inimigo((0, 255, 0), 3, (2000, 5000)),
        Inimigo((0, 0, 255), 4, (4000, 8000))
    ]

    drops = []
    tipos_drops = [
    ((255, 255, 0), "vida"),       #Drop amarelo = +1 vida
    ((0, 0, 255), "mais_vel"),    #Drop azul = mais velocidade de tiro
    ((0, 255, 0), "pontos"),      #Drop verde = +5 pontos
    ((255, 0, 0), "menos_vel")  #Drop vermelho = diminui a velocidade do tiro
    ]

    baus = []
    ultimo_spawn_bau = pygame.time.get_ticks()
    intervalo_spawn_bau = randint(5000, 10000)  #entre 5 e 10 segundos
    fim_de_jogo = False

    while not fim_de_jogo:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = True

        teclas = pygame.key.get_pressed()
        cowboy.mover(teclas)
        cowboy.atirar()
        cowboy.atualizar_projeteis()

        # Spawn de baús
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - ultimo_spawn_bau >= intervalo_spawn_bau:
            x = randint(LARGURA // 2, LARGURA - 100)
            y = randint(100, ALTURA - 100)
            baus.append(Bau([x, y]))
            ultimo_spawn_bau = tempo_atual
            intervalo_spawn_bau = randint(2000, 5000)

        # Colisão de tiro com baú
        for bau in baus[:]:
            if bau.ativo:
                for tiro in cowboy.projeteis[:]:
                    if pygame.Rect(tiro[0], tiro[1], 10, 5).colliderect(bau.get_rect()):
                        cowboy.projeteis.remove(tiro)
                        baus.remove(bau)
                        cor, efeito = tipos_drops[randint(0, len(tipos_drops) - 1)]
                        drops.append(Drop(cor, efeito, [bau.posicao[0] + 20, bau.posicao[1] + 20]))

                        break  # para de verificar esse baú
                        

        # Coleta de drops + aplica efeito
        for drop in drops[:]:
            if cowboy.get_rect().colliderect(drop.get_rect()):
                drops.remove(drop)

                if drop.efeito == "vida":
                    cowboy.vidas += 1
                elif drop.efeito == "mais_vel":
                    cowboy.intervalo_tiro = max(100, cowboy.intervalo_tiro - 150)
                elif drop.efeito == "pontos":
                    cowboy.pontos += 5  
                elif drop.efeito == "menos_vel":
                    cowboy.intervalo_tiro += 150


        for inimigo in inimigos:
            inimigo.reaparecer()
            if inimigo.ativo:
                inimigo.mover(cowboy)
                inimigo.atirar()
                inimigo.atualizar_projeteis(cowboy)

                # colisão tiro do cowboy com inimigo
                for tiro in cowboy.projeteis[:]:
                    if pygame.Rect(tiro[0], tiro[1], 10, 5).colliderect(inimigo.get_rect()):
                        inimigo.ativo = False
                        inimigo.projeteis.clear()
                        min_t, max_t = inimigo.intervalo
                        inimigo.respawn = pygame.time.get_ticks() + randint(min_t, max_t)
                        cowboy.pontos += 1
                        cowboy.projeteis.remove(tiro)

        # Desenho
        TELA.blit(fundo_img, (0, 0))
        
        cowboy.desenhar()
        for inimigo in inimigos:
            inimigo.desenhar()
        for bau in baus:
            bau.desenhar()
        pygame.display.flip()
        RELOGIO.tick(60)

        if cowboy.vidas <= 0:
            pygame.mixer.music.load('sons_jogo/game_over.wav')
            pygame.mixer.music.set_volume(0.7)
            tela_game_over()
            return main() 

    pygame.quit()

if __name__ == "__main__":
    main()