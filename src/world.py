class GameWorld:
    def __init__(self):
        self.objects = []       # List of all game objects
        self.score = 0          # Player score
        self.game_over = False  # Game over flag
        self.speed_multiplier = 1.0  # Used to increase difficulty

    def add(self, obj):
        self.objects.append(obj)  # Add a new object to the world

    def updateAll(self, dt):
        if self.game_over:
            return
        for obj in self.objects:
            if obj.active:
                obj.update(dt)  # Update all active objects

    def renderAll(self, screen):
        for obj in self.objects:
            if obj.active:
                obj.render(screen)  # Draw all active objects

    def checkCollisions(self, player):
        if self.game_over:
            return
        for obj in self.objects:
            if obj is player or not obj.active:
                continue
            if obj.intersects(player):
                print("GAME OVER!")
                self.game_over = True  # End game if player collides

    def cleanup(self):
        self.objects = [obj for obj in self.objects if obj.active]  # Remove inactive objects

