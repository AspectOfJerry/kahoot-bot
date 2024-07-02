import pyautogui
import keyboard
import time
from cc import cc

"""
https://pyautogui.readthedocs.io/en/latest/mouse.html

0,0       X increases -->
+---------------------------+
|                           | Y increases
|                           |     |
|   1920 x 1080 screen      |     |
|                           |     V
|                           |
|                           |
+---------------------------+ 1919, 1079
"""

# full: normalized coordinates when the answer buttons take up the whole screen without the question
# low: normalized coordinates when the answer buttons are at the bottom of the screen with the question at the top
DISPLAY_MODE = "full"
NUM_TABS = 20  # Has to be two times the number of iterations in join.py!!!

# Increase this value (seconds) if the script is going too fast (performance issues)
pyautogui.PAUSE = 0.04  # Generally, 0.04 to 0.06 works


class Constants:
    def __init__(self, top_left, top_right, bottom_left, bottom_right, left_center, right_center):
        self.TOP_LEFT = top_left
        self.TOP_RIGHT = top_right
        self.BOTTOM_LEFT = bottom_left
        self.BOTTOM_RIGHT = bottom_right
        self.LEFT_CENTER = left_center
        self.RIGHT_CENTER = right_center


MOUSE_POS = Constants(
    top_left=(0.25, 0.40) if DISPLAY_MODE == "full" else (0.25, 0.75),
    top_right=(0.75, 0.40) if DISPLAY_MODE == "full" else (0.75, 0.75),
    bottom_left=(0.25, 0.80) if DISPLAY_MODE == "full" else (0.25, 0.90),
    bottom_right=(0.75, 0.80) if DISPLAY_MODE == "full" else (0.75, 0.90),
    left_center=(0.2, 0.55) if DISPLAY_MODE == "full" else (0.2, 0.83),
    right_center=(0.75, 0.55) if DISPLAY_MODE == "full" else (0.75, 0.83)
)


def mov_norm(x_normalized, y_normalized):
    screen_width, screen_height = pyautogui.size()
    tx = screen_width * x_normalized
    ty = screen_height * y_normalized
    pyautogui.moveTo(tx, ty)


def mov_click_norm(x_normalized, y_normalized):
    screen_width, screen_height = pyautogui.size()
    tx = screen_width * x_normalized
    ty = screen_height * y_normalized
    pyautogui.click(x=tx, y=ty)


def answer_pos(pos, iterations):
    local_start_time = time.time()
    for _ in range(iterations):
        print(cc("GREEN", "> clicking at " + str(pos)))
        mov_click_norm(*pos)

        print(cc("FUCHSIA", "MOV >>"))
        pyautogui.shortcut("ctrl", "tab")

    print(cc("CYAN", "Round elapsed time: " + str(round(time.time() - local_start_time, 2)) + "s"))


print(cc("CYAN", "Focus on the browser window, starting in 2 seconds..."))
print(cc("RED", "Press Q to quit"))
print(cc("RED", "Avoid pressing arrow keys due to some conflicts"))
print(cc("GRAY", "Here are the hotkeys:"
                 "\nQ: Quit ❌"
                 "\n1: Top left ↖️"
                 "\n2/down arrow: Top right ↗️"
                 "\n3: Bottom left ↙️"
                 "\n4/left arrow: Bottom right ↘️"
                 "\n5: Left center ⬅️"
                 "\n6/right arrow: Right center ➡️"))

pyautogui.sleep(2)
global_start_time = time.time()

print(cc("GREEN", "Ready!"))

keyboard.on_press_key("1", lambda _: answer_pos(MOUSE_POS.TOP_LEFT, NUM_TABS))
keyboard.on_press_key("2", lambda _: answer_pos(MOUSE_POS.TOP_RIGHT, NUM_TABS))
keyboard.on_press_key("3", lambda _: answer_pos(MOUSE_POS.BOTTOM_LEFT, NUM_TABS))
keyboard.on_press_key("4", lambda _: answer_pos(MOUSE_POS.BOTTOM_RIGHT, NUM_TABS))
keyboard.on_press_key("5", lambda _: answer_pos(MOUSE_POS.LEFT_CENTER, NUM_TABS))
keyboard.on_press_key("6", lambda _: answer_pos(MOUSE_POS.RIGHT_CENTER, NUM_TABS))

keyboard.wait("q")
keyboard.unhook_all()
print(cc("CYAN", "Global elapsed time: " + str(round(time.time() - global_start_time, 2)) + "s"))
print(cc("RED", "Quitting..."))
