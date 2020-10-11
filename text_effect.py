from time import sleep


DEFAULT_PAUSE_LENGTH = 0.0          # Time in seconds to pause between senetences (1 works well)
DEFAULT_SLOW_TEXT_SPEED = 0.001     # A smaller number makes text print faster (0.01 works well)

class TextEffect:
    def __init__(self):
        self.pause_length = DEFAULT_PAUSE_LENGTH
        self.slow_text_speed = DEFAULT_SLOW_TEXT_SPEED

    def clear_screen(self):
        print("\n" * 500)

    def print_slowly(self, text, pause_sentences=True):
        """Creates a classic scroll effect on the text as it prints to the screen"""
        for c in text:
            if c == "\n":
                if pause_sentences == True:
                    self._pause()

            print(c, sep='', end='', flush=True)
            sleep(self.slow_text_speed)

    def _pause(self):
        sleep(self.pause_length)