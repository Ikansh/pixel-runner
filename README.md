# PIXEL RUNNER

#### Video Demo:  https://youtu.be/c7P1RvPwQ3s
#### Description:

> *"Where are all these flies coming from???"*

Welcome to my final project for the Python course: a 2D scrolling platformer runner game inspired by the Chrome dinosaur game. This game involves a player character who runs continuously across a landscape, avoiding obstacles in the form of a fly and a snail. The goal is to survive as long as possible while the game speeds up over time.

## Project Structure

The project is organized into several directories and files, each serving a specific purpose to ensure the game's functionality and maintainability.

### Directories and Files

- **audio/**: This folder contains all the audio files used in the game. This includes background music and sound effect for jumping. The audio enhances the player's experience by providing auditory feedback for their actions.

- **fonts/**: This directory includes font files used to display the game title and other text elements in the game. Using a custom pixelated font helps to create a unique and engaging visual style for the game.

- **graphics/**: This folder holds all the graphical assets used in the game. This includes images for the player character, the fly, the snail, the sky, and the ground. High-quality graphics are essential for creating an immersive gaming experience.

- **project.py**: This is the main executable file of the game. It initializes the game, sets up the game loop, and handles user inputs, game logic, and rendering. This ties together all the other components of the game.

- **test_project.py**: This file contains unit tests for some logical functions in project.py. Testing is crucial to ensure that the game functions correctly and to catch any bugs or issues early in development. The tests cover different aspects of the game logic, such as character movement, collision detection, and scoring.

- **requirements.txt**: This file lists all the pip-installable packages required to run the game. It ensures that anyone who wants to play or modify the game has the necessary dependencies installed. 

## Design Choices

When developing this game, I faced several design choices, particularly in terms of gameplay mechanics and the overall user experience.

1. **Character Movement**: The player character's movement needed to feel smooth and responsive. I implemented a physics-based approach to jumping and a running animation to achieve this. The enemy's speed increases gradually to add a sense of progression and challenge.

2. **Obstacle Interaction**: The decision to include a fly and a snail as obstacles was made to provide variety in the gameplay. The fly moves in a different pattern compared to the snail, requiring the player to time their jumps.

3. **Graphics and Audio**: I chose to use custom graphics and sound effects to create a unique aesthetic for the game. This helps to differentiate it from other similar games and makes the experience more engaging.

4. **Testing**: Incorporating unit tests was a crucial decision to maintain the game's reliability. By writing tests for critical game functions, I ensured that the game remains stable as new features are added or existing ones are modified.

## Object-Oriented and Functional Programming

This game project showcases my skills in both Object-Oriented Programming (OOP) and Functional Programming (FP).

### Object-Oriented Programming

- **Classes and Objects**: The game uses classes to represent the player and the enemies (fly and snail). Each class encapsulates relevant data and methods, providing a clear structure and modular design.

- **Inheritance and Polymorphism**: The obstacles share a base class but have distinct behaviors (e.g., different movement patterns). This demonstrates my ability to use inheritance to create a hierarchy of classes and polymorphism to allow for flexible and interchangeable object behavior.

- **Encapsulation**: By encapsulating the properties and methods within classes, I ensured that each part of the game has a well-defined interface, promoting code reuse and maintainability.

### Functional Programming

- **Pure Functions**: Many functions within the game are designed to be pure functions, meaning they do not have side effects and return the same output given the same input. This is evident in the game logic and collision detection algorithms.

- **Immutability**: Where appropriate, I used try-except to prevent unintended side effects and to ensure that functions behave predictably.

## Conclusion

This project showcases my ability to integrate various aspects of game development, from coding and testing to design and user experience. By employing both Object-Oriented and Functional Programming techniques, I have created a robust, maintainable, and engaging game. Feel free to explore the code, play the game, and provide feedback. I hope you enjoy it as much as I enjoyed creating it!