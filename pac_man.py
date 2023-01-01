import pygame

class PacMan (pygame.sprite.Sprite):

    def __init__ (self):
        super(PacMan, self).__init__()

        self.image = pygame.image.load("gfx/pacman_idle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20,20))
        
        self.rect = self.image.get_rect()

        self.coordinate = [600, 300]

    def show (self, screen: pygame.Surface) -> None:
        self.rect = self.image.get_rect(center=(self.coordinate))
        screen.blit(self.image, self.rect)
        pygame.display.flip()

    def refresh (self, move: str) -> None:
        if move == "UP":
            self.coordinate[1] += 5
        elif move == "DOWN":
            self.coordinate[1] -= 5
        elif move == "LEFT":
            pass
        elif move == "RIGHT":
            pass