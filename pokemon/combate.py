import pygame
from os import path
import random


music_dir = path.join(path.dirname(__file__), 'music')
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
img_dir = path.join(path.dirname(__file__), 'img')



# Dados gerais do jogo.
W, H = 800, 447
FPS = 30 # Frames por segundo

QUIT = 2

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Blastoise(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "9.png"))
        self.image = blastoise_img
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        
        self.hp = 155

def combate(screen):
    #font = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
        
    # Carrega o fundo do jogo
    background = pygame.image.load(path.join(img_dir, 'luta.jpg')).convert()
    background = pygame.transform.scale(background,(W,H))
    background_x = 0
    background_y = 0

    blastoise = Blastoise()    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(blastoise)

    inicio = pygame.time.get_ticks()

    # Loop principal.
    running = True
    MUSICA = True
    while running:
        if MUSICA:
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.load(path.join(music_dir, "musica_luta.mp3"))
            pygame.mixer.music.play()
            MUSICA = False
        # Ajusta a velocidade do jogo.
        clock.tick(FPS) 

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[0]:
                x = pygame.mouse.get_pos()[0]
                y =  pygame.mouse.get_pos()[1]
                if x > 404 and x < 576 and  y > 352 and y < 385  :
                    ataque = random.randint(0,100)
                    if ataque >= 90:
                        print('ataque crítico')
                        blastoise.hp -= 50
                    elif ataque >=5:
                        blastoise.hp -= 20
                    else :
                        print('Errrrou')
                        
                    
                    

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, (background_x, background_y))  # draws our first bg image
        all_sprites.draw(screen)
        
        # Desenha o power bar do blastoise.
        hp= blastoise.hp
        if blastoise.hp < 0:
            hp = 0
            running = False
            pygame.mixer.music.stop()
            pygame.mixer.music.load(path.join(music_dir, "route 209.mp3"))
            pygame.mixer.music.play()

        bar = pygame.Surface((hp, 9))
        bar.fill(GREEN)
        screen.blit(bar, (157, 88))
        
        #agora = pygame.time.get_ticks()
        #if (agora - inicio) > 500:
            #inicio = agora
            #blastoise.hp -= 10
            #if blastoise.hp <= 0:
             #   running = False
        
        #text_img = font.render("Oi", True, BLUE)
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
    return 42


#if __name__ == "__main__":
    
    # Inicialização do Pygame.
    #pygame.init()
    #pygame.mixer.init()
    
    # Tamanho da tela.
    #screen = pygame.display.set_mode((W, H))
    
    # Nome do jogo
    #pygame.display.set_caption("Pokemon")
    
    #try:
        #combate(screen)    
    #finally:
        #pygame.quit()
    
