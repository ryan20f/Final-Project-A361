from game_object import GameObject
import pygame

class Enemy(GameObject):
    def __init__(self, x, y, w, h, speed=-350):
        super().__init__(x, y, w, h)  # Initialize base GameObject
        self.speed = speed            # Horizontal speed of the enemy

    def update(self, dt):
        self.x += self.speed * dt      # Move enemy left each frame
        if self.x + self.w < 0:
            self.active = False        # Deactivate when off-screen

    def render(self, screen):
        # Draw enemy as a red rectangle
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.w, self.h))
