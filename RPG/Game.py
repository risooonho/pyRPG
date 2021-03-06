import pygame

from RPG.Scene import Scene
from RPG.Player import Player
from RPG.AnimatedSprite import AnimatedSprite

# code from http://www.gamedev.net/topic/444490-pygame-easy-as-py/
class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Gems Pygame RPG")

        self.clock = pygame.time.Clock()


        sprite = AnimatedSprite(self.clock, 'data/sprites/player/player.png')
        self.player = Player('test', sprite)

        self.scene = Scene('wedding')
        self.scene.add_player(self.player)

    def MainLoop(self):
        keepGoing = True
        direction = ''
        while keepGoing:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                # may want to look at pygame.key.set_repeat
                if event.type == pygame.KEYDOWN:
                    keyName = pygame.key.name(event.key)
                    if keyName in ('up','down','left','right'):
                        direction = keyName
                    #other button presses
                    #print keyName + ' pressed'
                elif event.type == pygame.KEYUP:
                    if pygame.key.name(event.key) == direction:
                        direction = ''
                        self.player.stop()
                    #print keyName + ' released'

            if direction == 'up':
               self.player.go_up()
            elif direction == 'down':
               self.player.go_down()
            elif direction == 'left':
               self.player.go_left()
            elif direction == 'right':
               self.player.go_right()

            if self.scene.detect_collision():
                self.player.resolve_collision()
                font = pygame.font.Font(None, 36)
                text = font.render("collision" , 1, (255, 0, 0))
                self.screen.blit(text, (0,0))

            self.scene.render_background(self.screen)
            self.scene.render_mask(self.screen) #debug
            self.player.render_mask(self.screen) #debug
            self.player.render(self.screen)
            self.scene.render_foreground(self.screen)

            #draw dialog boxes
            pygame.display.flip()
