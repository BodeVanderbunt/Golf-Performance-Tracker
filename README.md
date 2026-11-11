# Golf Performance Tracker

A command-line Python application for recording golf rounds and tracking performance statistics over time.

## Overview

Golf Performance Tracker lets golfers log each round they play, including score, fairways hit, greens in regulation (GIR), and putts. It calculates key performance statistics so players can spot strengths and weaknesses in their game. All data is saved to a local JSON file, so rounds are kept between sessions.

## Features

- **Add rounds** with course name, score, fairways hit, greens in regulation, and putts
- **View all rounds** in a clear, numbered list
- **Performance statistics**, including:
  - Rounds played
  - Average score and best round
  - Average putts
  - Average fairways hit and fairway percentage
  - Average GIR and GIR percentage
- **Persistent storage**: rounds are saved to and loaded from a JSON file automatically
- **Input validation**: rejects non-numeric input and values outside realistic ranges (for example, more than 18 greens in regulation)
- **Reset all data** with a confirmation prompt to prevent accidental deletion

## Technologies Used

- Python 3
- `json` module for data storage

No external libraries are required.

## Getting Started

### Prerequisites

- [Python 3](https://www.python.org/downloads/) installed on your computer

### Installation and Usage

1. Download or clone this repository:
   ```
   git clone https://github.com/[your-username]/golf-performance-tracker.git
   ```
2. Go to the project folder:
   ```
   cd golf-performance-tracker
   ```
3. Run the program:
   ```
   python golf_tracker.py
   ```
   On Mac or Linux, you may need to use `python3` instead of `python`.

A `rounds.json` file is created automatically the first time you add a round.

### EXAMPLE

--- GOLF PERFORMANCE TRACKER ---
1. Add Round
2. View Rounds
3. View Statistics
4. Reset All Data
5. Exit

Choose an option: 3
Rounds Played: 2
Average Score: 77.50
Best Round: Payne's Valley - 76
Average Putts: 31.50
% Fairways Hit: 69.44%
GIR %: 50.00%

## Planned Features

- [ ] Add a date to each round
- [ ] Edit or delete individual rounds
- [ ] Track course par and show score relative to par
- [ ] Unit tests with `pytest`
- [ ] Charts of scoring trends with `matplotlib`
- [ ] Web-based version using Flask and SQLite

## Author
- GitHub: @BodeVanderbunt https://github.com/BodeVanderbunt)
- LinkedIn: https://www.linkedin.com/in/bodevanderbunt/
