from game_object import GameObject
import pygame

class Item(GameObject):
    def render(self, screen):
        # Draw the item as a blue rectangle
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.w, self.h))
