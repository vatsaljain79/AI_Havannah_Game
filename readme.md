
# Havannah Game Playing AI

## Overview

This project implements an AI agent capable of playing the two-player board game **Havannah**. The AI is designed to make decisions within a limited time frame, considering the state of the game board and the opponent's actions. The project also supports human vs human, human vs AI, and AI vs random agent gameplay.

## Game Rules: Havannah

Havannah is played on a hexagonal grid where players take turns placing their pieces, aiming to form one of the following structures to win:

1. **Bridge**: A continuous path connecting two corners of the board.
2. **Fork**: A path connecting three different edges of the board.
3. **Ring**: A closed loop of pieces surrounding empty or occupied spaces.


![image](https://github.com/user-attachments/assets/03bc4878-537d-4275-ae80-eee16b5ab1bc)

The game ends when a player successfully completes one of these structures or if their time budget is exhausted.

## Features

- **AI Agent**: The AI uses a search-based algorithm to evaluate board states and make optimal moves.
- **Multiple Game Modes**:
  - AI vs Human
  - Human vs Human
  - AI vs Random Agent
- **Board Size**: Configurable board dimensions (4 to 10).
- **Time Bound**: Each player operates within a specified time budget to make decisions.

## Installation

### Requirements

- Python 3.10+
- NumPy
- Tkinter (for GUI rendering)

### Setup Using Conda

1. Clone the repository:
    ```bash
    git clone https://github.com/vatsaljain79/AI_Havannah_Game
    cd AI_Havannah_Game-main
    ```
2. Set up the environment using conda:
    ```bash
    conda create -n havannah_env python=3.10 numpy tk
    conda activate havannah_env
    ```

### Running on WSL

To run the project on **Windows Subsystem for Linux (WSL)**, install the required packages and execute the code as usual:

1. Install dependencies:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip python3-tk
    pip3 install numpy
    ```
2. Run the game:
    ```bash
    cd AI_Havannah_Game-main
    python3 game.py <player1> <player2> --time <time> --dim <dim>
    ```

## Game Execution

To start a game, use the following command:

```bash
python3 game.py <player1> <player2> --time <time> --dim <dim>
```

- `<player1>` and `<player2>`: Can be `ai`, `human`, or `random`.
- `--time`: Specify the time budget for each player (in seconds).
- `--dim`: (Optional) Specify the board size (4 to 10). Default is 4.

### Example Commands

- **AI vs Human** (4x4 board, 10-minute game):
    ```bash
    python3 game.py ai human --dim 4 --time 600
    ```
- **Human vs Human** (5x5 board, 10-minute game):
    ```bash
    python3 game.py human human --dim 5 --time 600
    ```
- **AI vs Random Agent** (6x6 board, 1000-second game):
    ```bash
    python3 game.py ai random --dim 6 --time 1000
    ```

## Project Structure

```bash
AI_Havannah_Game-main/
├── game.py             # Game engine (runs game loop, renders GUI, manages input/output)
├── helper.py           # Helper functions for traversing the board, checking win conditions, etc.
├── players/
│   ├── ai.py           # AI agent implementation
│   ├── ai2.py          # 2nd AI agent implementation
│   ├── random.py       # Random agent implementation
│   ├── human.py        # Human player input handler
├── initial_states      # Sample board layouts (optional)
└── README.md           # Instructions and project overview
```

## AI Implementation Details

The AI agent is implemented in `ai.py` and uses a search-based algorithm to determine the best move. The AI takes into account factors such as remaining time and board state, aiming to complete one of the three winning conditions as quickly as possible.

### Key Components

- **Monte Carlo Tree Search (MCTS)**: A strategy that balances exploration and exploitation by running simulations to evaluate potential moves, helping the AI make more informed decisions.
- **Move Selection**: The AI uses a state evaluation function to score possible moves and select the most optimal one.
- **Time Management**: The AI ensures it never runs out of time by continuously monitoring the remaining time with the `fetch_remaining_time` function and always making a move within the time limit, prioritizing optimal choices.

## How to Play

1. **Start the Game**: Follow the commands in the "Game Execution" section to start a game with your desired settings.
2. **GUI Interaction**: If using the graphical interface, you can click on hexagonal cells to place your pieces.
3. **Command Line Interaction**: In "server" mode (no GUI), input the row and column numbers in the terminal.
