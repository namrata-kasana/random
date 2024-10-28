
import random

def how_high_can_you_go():
    total_score = 0
    while True:
        dice_roll = random.randint(1, 6)
        try:
            choice = int(input("Standing enter 1, sitting down enter 0: "))
            if choice not in (0, 1):
                raise ValueError("Invalid input. Please enter 0 or 1.")
                break
        except ValueError as e:
            print(f"Error: {e}")
        if dice_roll == 6:
            # DOUBT : Quetion does  not mention what to print when 6 is rolled hence have printed below line.
            print("You rolled a 6. Game over!")
            return
        if choice == 0:
            print(total_score)
            return
        total_score += dice_roll
        print(dice_roll, total_score)

how_high_can_you_go()