from random import randint


class Dice:
    def __init__(self):
        pass

    def roll_two_dice(self, graphical=True):
        """
        Returns a tuple of two integers that simulates a random
        dice roll. The return values are between 1 and 6. The optional
        graphical parameter displays an ASCII art representation of
        the 2 die's random values displayed as a * symbol.
        """

        die_1 = self.get_random_die()  # Set random value between 1 - 6
        die_2 = self.get_random_die()  # Set random value between 1 - 6

        # -------------------
        # DIE MAP DESCRIPTION
        # -------------------
        # The die map holds the layout sequence for a dice roll (1 - 6).
        # Use the Dictionary's key to produce a map that
        # can be replaced with whatever symbol you want. (i.e. *)
        die_map = {1: [" ", " ", " ", " ", "*", " ", " ", " ", " "],
                   2: [" ", " ", "*", " ", " ", " ", "*", " ", " "],
                   3: ["*", " ", " ", " ", "*", " ", " ", " ", "*"],
                   4: ["*", " ", "*", " ", " ", " ", "*", " ", "*"],
                   5: ["*", " ", "*", " ", "*", " ", "*", " ", "*"],
                   6: ["*", " ", "*", "*", " ", "*", "*", " ", "*"]}

        # Prepare the ASCII print sequence for each die.
        left = die_map[die_1]
        right = die_map[die_2]

        if graphical is True:
            print(
                f"+-----------+    +-----------+\n" +
                f"|  {left[0]}  {left[1]}  {left[2]}  |    " +
                f"|  {right[0]}  {right[1]}  {right[2]}  |\n" +
                f"|  {left[3]}  {left[4]}  {left[5]}  |    " +
                f"|  {right[3]}  {right[4]}  {right[5]}  |\n" +
                f"|  {left[6]}  {left[7]}  {left[8]}  |    " +
                f"|  {right[6]}  {right[7]}  {right[8]}  |\n" +
                f"+-----------+    +-----------+"
                )

        return (die_1, die_2)

    def get_random_die(self):
        return randint(1, 6)
