import pygame
from random import choice

pygame.init()

class Label(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        self.text = "Kills : "
        self.center = (500, 50)
        self.color = (0, 0, 0)

    def update(self):
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.center



class Duck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("d1.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 615
        self.rect.y = choice(range(222))
        self.dead = False
        self.duck_speed = 5

    def update(self):
        self.rect.x -= self.duck_speed
        
        self.rect.x -= self.duck_speed
        if self.rect.x < 0 or self.dead:
            self.remove(self.groups())

class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("sh1.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.center = (301.5, 222)

    def update(self):
        self.image = pygame.image.load("sh1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()



screen = pygame.display.set_mode((603, 444))
pygame.display.set_caption("dia de caca")

bg1 = pygame.Surface(screen.get_size())
bg1 = pygame.image.load("bg1.png")


clock = pygame.time.Clock()

label = Label()

ducks = pygame.sprite.Group()

kills = 0

cacador_grp = pygame.sprite.Group()
shoot = Shoot()
cacador_grp.add(shoot, label)


pygame.mouse.set_visible(False)

keepGoing = True


def validar_shoot():
    global kills
    deads = False
    for duck in ducks:
        if pygame.mouse.get_pressed()[0]:
            if pygame.sprite.collide_mask(shoot, duck):
                if not duck.dead:
                    duck.dead = True
                    kills += 1
                    label.text = "Kills: %d" %(kills)


    if ducks.__len__() < 1:
        criar_patos()


def criar_patos():
    for i in range(1):
        ducks.add(Duck())



def main():
    global keepGoing

    criar_patos()


    while keepGoing:
        clock.tick(30)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False


        screen.blit(bg1, (0, 0))
        ducks.clear(screen, bg1)
        shoot.update()
        cacador_grp.clear(screen, bg1)
        ducks.update()
        cacador_grp.update()
        ducks.draw(screen)
        cacador_grp.draw(screen)
        pygame.display.update()
        validar_shoot()



if __name__ == "__main__":
    main()
