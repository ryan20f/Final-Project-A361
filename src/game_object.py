import itertools
import pygame

class GameObject:
    _ids = itertools.count()  # Unique ID generator for each object

    def __init__(self, x, y, w, h):
        self.id = next(GameObject._ids)  # Assign a unique ID
        self.x = x                        # X position
        self.y = y                        # Y position
        self.w = w                        # Width
        self.h = h                        # Height
        self.active = True                # Flag to check if object is active

    def update(self, dt):
        pass  # Base update method (to be overridden in subclasses)

    def render(self, screen):
        # Draw the object as a white rectangle by default
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.w, self.h))

    def intersects(self, other):
        # Check if this object intersects/collides with another
        return (
            self.x < other.x + other.w and
            self.x + self.w > other.x and
            self.y < other.y + other.h and
            self.y + self.h > other.y
        )
