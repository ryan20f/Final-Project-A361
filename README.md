# Final-Project
This project is a mini game engine made in Python using Pygame. It shows how to use object-oriented programming with classes, inheritance, and polymorphism. The game is similar to the offline Google Chrome dinosaur game. The player can jump and crouch to avoid obstacles while the game keeps score and increases in difficulty.

The engine has a base GameObject class with update and render methods. Player, Enemy, and Item classes are derived from GameObject. The game uses a GameWorld class to manage all objects and an EnemySpawner class to create new enemies over time. Collisions are detected between the player and enemies to end the game if the player hits an obstacle.

To run the game, make sure Python and Pygame are installed. Pygame can be installed with pip install pygame. All files should be in the same folder. Run the game by typing python main.py in the terminal. Use the Up Arrow or Spacebar to jump and the Down Arrow to crouch. Avoid obstacles to keep playing.

The game loop updates and draws all objects every frame, handles input, and checks collisions. This makes the game run smoothly and feel responsive. The game works well with a few objects and runs at about 60 frames per second.

The code is designed to be simple and easy to understand. Each class has its own responsibility, and the update and render methods are called on all objects using polymorphism. The EnemySpawner uses a simple factory pattern to create enemies dynamically. The project could be improved with sprites, sound, more items, or optimized collision detection if needed.
