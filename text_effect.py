from time import sleep


# Time in seconds to pause between senetences (0.04 works well)
DEFAULT_PAUSE_LENGTH = 0.07

# A smaller number makes text print faster (0.003 works well)
DEFAULT_SLOW_TEXT_SPEED = 0.003


class TextEffect:
    def __init__(self):
        self.pause_length = DEFAULT_PAUSE_LENGTH
        self.slow_text_speed = DEFAULT_SLOW_TEXT_SPEED

    def clear_screen(self):
        print("\n" * 500)

    def print_slowly(self, text, pause_sentences=True):
        """
        Creates a classic scroll effect on the text as
        it prints to the screen
        """
        for c in text:
            if c is "\n":
                if pause_sentences is True:
                    self._pause()

            print(c, sep='', end='', flush=True)
            sleep(self.slow_text_speed)

    def _pause(self):
        sleep(self.pause_length)
