# 🎲 Dice Game – Python OOP Project

## 📖 Description
This project is a command-line based dice game developed in Python using Object-Oriented Programming (OOP) principles.  
It supports multiple game modes with different winning conditions and demonstrates clean class design, inheritance, and automated testing.

This project was developed as a learning project during my second year of B.Tech.

---

## 🎮 Game Modes

### 🔹 Game A – Target Score
- Players roll dice to accumulate points.
- Reaching or exceeding the target score wins the game.
- Rolling a specific reset number resets the player’s score.

### 🔹 Game B – Sequence Match
- Players must roll a specific sequence of dice values to win.
- Extra values are allowed as long as the required sequence appears.

### 🔹 Game C – Target Sum
- Players win by rolling dice whose sum exactly matches a target value.

### 🔹 Game D – Max Score
- The game runs for a fixed number of rounds.
- The player with the highest score at the end wins.

---

## 🗂 Project Structure

```text
dice_game/
│
├── dice_game_main.py   # Main game logic
├── player.py           # Player class
├── scoreboard.py       # Scoreboard handling
├── tests.py            # Automated test cases
└── README.md           # Project documentation
