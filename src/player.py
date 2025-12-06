from game_object import GameObject
import pygame

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 50)  # Initialize base GameObject
        self.vy = 0                     # Vertical velocity
        self.gravity = 1600             # Gravity affecting the player
        self.jump_force = -650          # Upward force when jumping
        self.is_crouching = False       # Flag for crouching
        self.on_ground = True           # Check if player is on the ground
        self.ground_y = y + self.h      # Fixed ground position (bottom of player)

    def jump(self):
        if self.on_ground:
            self.vy = self.jump_force   # Apply jump force
            self.on_ground = False      # Player is now in the air

    def crouch(self, active):
        if self.on_ground:
            if active:
                self.h = 30                     # Crouching height
            else:
                self.h = 50                     # Standing height
            self.y = self.ground_y - self.h      # Keep bottom fixed
            self.is_crouching = active

    def update(self, dt):
        self.vy += self.gravity * dt          # Apply gravity
        self.y += self.vy * dt                # Update vertical position

        # Keep player on the ground
        if self.y + self.h >= self.ground_y:
            self.y = self.ground_y - self.h
            self.vy = 0
            self.on_ground = True

    def render(self, screen):
        color = (0, 255, 0)
        pygame.draw.rect(screen, color, (self.x, self.y, self.w, self.h))  # Draw player
