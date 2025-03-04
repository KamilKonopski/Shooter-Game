import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter Game")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# player action variables
moving_left = False
moving_right = False

# define colors
BG = (134, 214, 145)

def draw_bg():
    screen.fill(BG)


class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, char_type, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("assets/img/player/Idle/0.png")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False

    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        self.rect.x += dx
        self.rect.y += dy 

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Soldier(200, 200, "player", 3, 5)





run = True
while run:

    clock.tick(FPS)

    draw_bg()

    player.draw()

    player.move(moving_left, moving_right)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        #keyboard button presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    pygame.display.update()

pygame.quit()