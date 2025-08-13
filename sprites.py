import pygame


pygame.init()


class Cowboy_andando(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cowboy = []
        self.cowboy.append(pygame.image.load('imagens/cowboy/cowboy_andando1.png'))
        self.cowboy.append(pygame.image.load('imagens/cowboy/cowboy_andando2.png'))

        self.atual = 0
        self.image = self.cowboy[self.atual]
        
        self.image = pygame.transform.scale(self.image, (100, 100))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
    #para animar
        self.andar = False

    def iniciar_andar(self):
        self.andar = True

    def update(self):
        if self.andar == True:
            self.atual = self.atual + 1
            if self.atual >= len(self.cowboy):
                self.atual = 0
                self.andar = False
            self.image = pygame.transform.scale(self.cowboy[self.atual], (100, 100))


class Cowboy_atirando(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.atirando = []
        self.atirando.append(pygame.image.load('imagens/cowboy/cowboy_atirando1.png'))
        self.atirando.append(pygame.image.load('imagens/cowboy/cowboy_atirando2.png'))
        self.atirando.append(pygame.image.load('imagens/cowboy/cowboy_atirando3.png'))
        self.atirando.append(pygame.image.load('imagens/cowboy/cowboy_atirando4.png'))
        

        self.atual = 0
        self.image = self.atirando[self.atual]
        
        self.image = pygame.transform.scale(self.image, (100, 100))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 300, 300
    #para animar
        self.atirando_ativo = False

    def iniciar_tiro(self):
        self.atirando_ativo = True

    def update(self):
        if self.atirando_ativo == True:
            self.atual = self.atual + 1
            if self.atual >= len(self.atirando):
                self.atual = 0
                self.atirando_ativo = False
            self.image = pygame.transform.scale(self.atirando[self.atual], (100, 100))

##bandido

class Bandido_andando(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bandido_andando = []
        self.bandido_andando.append(pygame.image.load('imagens/inimigos/bandido_andando1.png'))
        self.bandido_andando.append(pygame.image.load('imagens/inimigos/bandido_andando2.png'))

        self.atual = 0
        self.image = self.bandido_andando[self.atual]
        self.image = pygame.transform.scale(self.image, (100, 150))

        self.rect = self.image.get_rect()
        self.rect.topleft = 450, 90


    def update(self):
            self.atual += 1
            if self.atual >= len(self.bandido_andando):
                self.atual = 0
            self.image = pygame.transform.scale(self.bandido_andando[self.atual], (180, 200))


class Bandido_jogando_tnt(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bandido_tnt = []
        self.bandido_tnt.append(pygame.image.load('imagens/inimigos/bandido_jogando_tnt1.png'))
        self.bandido_tnt.append(pygame.image.load('imagens/inimigos/bandido_jogando_tnt2.png'))
        self.bandido_tnt.append(pygame.image.load('imagens/inimigos/bandido_jogando_tnt3.png'))

        self.atual = 0
        self.image = self.bandido_tnt[self.atual]
        self.image = pygame.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()
        self.rect.topleft = 350, 90

    def update(self):
            self.atual += 1
            if self.atual >= len(self.bandido_tnt):
                self.atual = 0
            self.image = pygame.transform.scale(self.bandido_tnt[self.atual], (200, 200))


#baus


class Bau_dinamite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bau_dinamite = []
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_fechado.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_aberto.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_dinamite_explosao1.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_dinamite_explosao1.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_dinamite_explosao2.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_dinamite_explosao3.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_dinamite_explosao4.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_dinamite_explosao5.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_dinamite_explosao6.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_dinamite_explosao7.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_dinamite_explosao8.png'))
        self.bau_dinamite.append(pygame.image.load('imagens/objetos/bau_dinamite_explosao8.png'))

        
        

        self.atual = 0
        self.image = self.bau_dinamite[self.atual]
        
        self.image = pygame.transform.scale(self.image, (100, 70))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 350, 350
    #para animar

    def update(self):
            self.atual = self.atual + 1
            if self.atual >= len(self.bau_dinamite):
                self.atual = 0
            self.image = pygame.transform.scale(self.bau_dinamite[self.atual], (100, 70))

class Bau_cactoazul(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bau_cactoazul = []
        self.bau_cactoazul.append(pygame.image.load('imagens/objetos/bau_fechado.png'))
        self.bau_cactoazul.append(pygame.image.load('imagens/objetos/bau_aberto.png'))
        self.bau_cactoazul.append(pygame.image.load('imagens/objetos/bau_flor_azul1.png'))
        self.bau_cactoazul.append(pygame.image.load('imagens/objetos/bau_flor_azul2.png'))
        self.bau_cactoazul.append(pygame.image.load('imagens/objetos/bau_flor_azul1.png'))
        self.bau_cactoazul.append(pygame.image.load('imagens/objetos/bau_flor_azul2.png'))

        self.atual = 0
        self.image = self.bau_cactoazul[self.atual]
        
        self.image = pygame.transform.scale(self.image, (100, 70))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400, 360
    #para animar

    def update(self):
            self.atual = self.atual + 1
            if self.atual >= len(self.bau_cactoazul):
                self.atual = 0
            self.image = pygame.transform.scale(self.bau_cactoazul[self.atual], (100, 70))

class Bau_cactovermelho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bau_cactovermelho = []
        self.bau_cactovermelho.append(pygame.image.load('imagens/objetos/bau_fechado.png'))
        self.bau_cactovermelho.append(pygame.image.load('imagens/objetos/bau_aberto.png'))
        self.bau_cactovermelho.append(pygame.image.load('imagens/objetos/bau_flor_vermelha1.png'))
        self.bau_cactovermelho.append(pygame.image.load('imagens/objetos/bau_flor_vermelha2.png'))
        self.bau_cactovermelho.append(pygame.image.load('imagens/objetos/bau_flor_vermelha1.png'))
        self.bau_cactovermelho.append(pygame.image.load('imagens/objetos/bau_flor_vermelha2.png'))

        self.atual = 0
        self.image = self.bau_cactovermelho[self.atual]
        
        self.image = pygame.transform.scale(self.image, (100, 70))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 400, 400
    #para animar

    def update(self):
            self.atual = self.atual + 1
            if self.atual >= len(self.bau_cactovermelho):
                self.atual = 0
            self.image = pygame.transform.scale(self.bau_cactovermelho[self.atual], (100, 70))

class Bau_placa_cin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bau_placa_cin = []
        self.bau_placa_cin.append(pygame.image.load('imagens/objetos/bau_placa_cin0.png'))
        self.bau_placa_cin.append(pygame.image.load('imagens/objetos/bau_placa_cin1.png'))
        self.bau_placa_cin.append(pygame.image.load('imagens/objetos/bau_placa_cin2.png'))
        self.bau_placa_cin.append(pygame.image.load('imagens/objetos/bau_placa_cin3.png'))
        
        self.atual = 0
        self.image = self.bau_placa_cin[self.atual]
        
        self.image = pygame.transform.scale(self.image, (300, 270))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 150, 50
    #para animar

    def update(self):
            self.atual = self.atual + 1
            if self.atual >= len(self.bau_placa_cin):
                self.atual = 0
            self.image = pygame.transform.scale(self.bau_placa_cin[self.atual], (400, 330))


class Bau_ouro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bau_ouro = []
        self.bau_ouro.append(pygame.image.load('imagens/objetos/bau_fechado.png'))
        self.bau_ouro.append(pygame.image.load('imagens/objetos/bau_aberto.png'))
        self.bau_ouro.append(pygame.image.load('imagens/objetos/bau_com_ouro1.png'))
        self.bau_ouro.append(pygame.image.load('imagens/objetos/bau_com_ouro2.png'))
        self.bau_ouro.append(pygame.image.load('imagens/objetos/bau_com_ouro3.png'))
        self.bau_ouro.append(pygame.image.load('imagens/objetos/bau_com_ouro4.png'))


       
        self.atual = 0
        self.image = self.bau_ouro[self.atual]
        
        self.image = pygame.transform.scale(self.image, (100, 70))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 450, 400
    #para animar

    def update(self):
            self.atual = self.atual + 1
            if self.atual >= len(self.bau_ouro):
                self.atual = 0
            self.image = pygame.transform.scale(self.bau_ouro[self.atual], (100, 70))

class Bau_medalha(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bau_medalha = []
        self.bau_medalha.append(pygame.image.load('imagens/objetos/bau_fechado.png'))
        self.bau_medalha.append(pygame.image.load('imagens/objetos/bau_aberto.png'))
        self.bau_medalha.append(pygame.image.load('imagens/objetos/bau_com_medalha1.png'))
        self.bau_medalha.append(pygame.image.load('imagens/objetos/bau_com_medalha2.png'))
        self.bau_medalha.append(pygame.image.load('imagens/objetos/bau_com_medalha3.png'))
        self.bau_medalha.append(pygame.image.load('imagens/objetos/bau_com_medalha4.png'))
        self.bau_medalha.append(pygame.image.load('imagens/objetos/bau_com_medalha5.png'))

        self.atual = 0
        self.image = self.bau_medalha[self.atual]
        
        self.image = pygame.transform.scale(self.image, (100, 70))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 450, 300
    #para animar

    def update(self):
            self.atual = self.atual + 1
            if self.atual >= len(self.bau_medalha):
                self.atual = 0
            self.image = pygame.transform.scale(self.bau_medalha[self.atual], (100, 70))




todas_as_sprites = pygame.sprite.Group()
bau_cactovermelho = Bau_cactovermelho()
bau_cactoazul = Bau_cactoazul()
bau_dinamite = Bau_dinamite()
bau_placacin = Bau_placa_cin()
bau_ouro = Bau_ouro()
bau_medalha = Bau_medalha()
atirando = Cowboy_atirando()
cowboy = Cowboy_andando()
bandido_andando = Bandido_andando()
bandido_tnt = Bandido_jogando_tnt()


todas_as_sprites.add(cowboy)
todas_as_sprites.add(atirando)
todas_as_sprites.add(bandido_andando)
todas_as_sprites.add(bandido_tnt)
todas_as_sprites.add(bau_dinamite)
todas_as_sprites.add(bau_cactoazul)
todas_as_sprites.add(bau_cactovermelho)
todas_as_sprites.add(bau_placacin)
todas_as_sprites.add(bau_ouro)
todas_as_sprites.add(bau_medalha)

