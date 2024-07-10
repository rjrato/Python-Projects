# Turtle Crossing Game

A simple game where a turtle crosses a busy road, avoiding cars and reaching the other side safely, implemented in Python using the Turtle module.

## Overview

This Python program recreates a classic arcade-style game where the player controls a turtle trying to cross a road filled with moving cars. The goal is to safely navigate the turtle across the road without colliding with any cars.

## Features

- **Turtle Movement**: 
  - Use 'Up' and 'Down' arrow keys to move the turtle up and down on the screen.
  - The turtle must avoid oncoming traffic by timing movements between gaps in the cars.

- **Car Generation and Movement**: 
  - Cars appear from the left side of the screen and move towards the right.
  - Multiple cars of varying speeds are generated as the game progresses.

- **Collision Detection**: 
  - Detects collisions between the turtle and cars, ending the game if they collide.
  - Upon collision, the game displays a game over message.

- **Level Progression**: 
  - Each time the turtle successfully crosses the road to the finish line, the level increases.
  - With each level, cars move faster, making the game more challenging.

## Installation

Ensure Python is installed on your system. Clone the repository and run the following command:

```bash
python turtle_crossing_game.py
```

## Dependencies
- Python 3.x
- Turtle graphics library (included in standard Python installations)