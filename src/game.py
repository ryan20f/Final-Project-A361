import pygame
import time
from world import GameWorld
from player import Player
from enemy_spawner import EnemySpawner

pygame.init()
screen = pygame.display.set_mode((640, 400))  # Create game window
clock = pygame.time.Clock()                    # For controlling FPS
pygame.display.set_caption("Cactus Runner")   # Window title

def main():
    world = GameWorld()            # Create the game world
    player = Player(80, 300)       # Create the player
    world.add(player)               # Add player to the world
    spawner = EnemySpawner(world)   # Create enemy spawner

    running = True
    last_time = time.time()

    while running:
        dt = clock.tick(60) / 1000  # Delta time in seconds

        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # INPUT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            player.jump()            # Jump if up or space pressed
        player.crouch(keys[pygame.K_DOWN])  # Crouch if down pressed

        # UPDATE
        spawner.update(dt)          # Spawn enemies as needed
        world.updateAll(dt)         # Update all objects
        world.checkCollisions(player)  # Check for collisions
        world.cleanup()             # Remove inactive objects

        # SCORING
        world.score += dt * 60      # Increase score over time

        # RENDER
        screen.fill((30, 30, 30))   # Clear screen
        world.renderAll(screen)     # Draw all objects

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {int(world.score)}", True, (255,255,255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()     # Update display

        # Check if game is over
        if world.game_over:
            time.sleep(1)
            running = False

    pygame.quit()                  # Exit pygame

if __name__ == "__main__":
    main()
