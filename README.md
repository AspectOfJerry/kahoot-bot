# Kahoot flooder bot

This is a simple kahoot flooder bot written in python. It uses PyAutoGUI to simulate mouse and keyboard events.

There are two scripts in this repository:

Remember to focus on the browser window where the kahoot game is after starting the script. You will have 3 seconds to do so.

<br>

- `join.py` - This script will is used to join the kahoot game.
- Please change the variables below. The comments are self-explanatory.

```python
KAHOOT_URL = "https://kahoot.it/"
GAME_PIN = "0000000"  # Replace with the game pin
NUM_ITER = 10  # Number of bots is two times the number of iterations because they join in pairs

pyautogui.PAUSE = 0.1  # Increase this value (seconds) if the script is going too fast (performance issues)
```

Note: The amount of bots that join the game is two times the `NUM_ITER` variable because they join in pairs.

<br>

- `answer.py` - This script will answer the questions. Run it after the bots have joined the game, waiting for the game to start.
- Please change the variables below. The comments are self-explanatory.

```python
# full: normalized coordinates when the answer buttons take up the whole screen without the question
# low: normalized coordinates when the answer buttons are at the bottom of the screen with the question at the top
DISPLAY_MODE = "full"
NUM_TABS = 20  # Has to be two times the number of iterations in join.py!!!

pyautogui.PAUSE = 0.04  # Increase this value (seconds) if the script is going too fast (performance issues)
```

Note: The amount of tabs that the script has to switch has to be two times the `NUM_ITER` variable from `join.py` because they join in pairs.

Here are the hotkeys for the answer script:

- Q: Quit ❌
- 1: Top left ↖️
- 2/down arrow: Top right ↗️
- 3: Bottom left ↙️
- 4/left arrow: Bottom right ↘️
- 5: Left center ⬅️
- 6/right arrow: Right center ➡️
