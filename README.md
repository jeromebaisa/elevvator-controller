# Elevator Controller Simulator

## About the Project
This is a simple Python program that simulates a three-floor elevator. The elevator moves between floors based on the buttons pressed.

## What It Does
- Moves between Floors 1, 2, and 3.
- Opens and closes the elevator doors.
- Slows down before reaching a floor.
- Ignores button presses while moving.
- Allows people to call the elevator using hallway buttons.

## How to Run
Make sure Python 3 is installed.

Open the terminal in the project folder and type:

```bash
python3 elevator.py
```

You can also run it using:

```bash
make run
```

Enter commands one at a time to control the elevator. Press Control + D to exit.

## How to Test
Run this command:

```bash
make test
```

This checks whether the elevator produces the correct outputs.

GitHub Actions also runs the tests automatically when changes are pushed to GitHub or a pull request is made.

## Project Files
- elevator.py - Main Python program.
- Makefile - Commands for running and testing.
- tests/ - Test files.
- .github/workflows/test.yml - Runs tests on GitHub.