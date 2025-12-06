import random
from enemy import Enemy

class EnemySpawner:
    def __init__(self, world):
        self.world = world            # Reference to the game world
        self.timer = 0                # Timer to control spawn intervals
        self.spawn_interval = 1.2     # Time between spawns in seconds

    def update(self, dt):
        self.timer += dt              # Increase timer by delta time

        if self.timer > self.spawn_interval:
            self.timer = 0            # Reset timer

            # Randomly choose enemy type
            if random.random() < 0.7:
                # Ground enemy (player must jump over)
                y = 300
                w = h = random.choice([40, 50])
            else:
                # Crouch obstacle (player must crouch to avoid)
                h = 20
                w = random.choice([40, 60])
                player_standing_top = 300   # top of player when standing
                y = player_standing_top - 0 # obstacle aligns with head

            # Create enemy and add it to the world
            e = Enemy(600, y, w, h, speed=-350 * self.world.speed_multiplier)
            self.world.add(e)

            # Gradually increase game speed/difficulty
            self.world.speed_multiplier += 0.008
