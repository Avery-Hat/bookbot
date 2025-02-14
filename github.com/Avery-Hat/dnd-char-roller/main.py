# made to create a random stats for a DnD Character in 5e
# this uses 6 D6 dice and drops the lowest number

# notes: 
# maybe give it a seed to work with for consistency
# making lowest and highest total scores from 100 runs printed
import random

def main():

    def roll_dice(num_dice):
        rolls = [random.randint(1, 6) for _ in range(num_dice)]
        rolls.sort()  
        print("Rolls:", rolls)  # Show all rolls (sorted)
        return sum(rolls[1:])  # Drop the lowest roll and sum the rest

    results = [roll_dice(4) for _ in range(6)]  # Roll 6 times
    print("Results number 1:", results)  # Display the final results for all 6

    results2 = [roll_dice(4) for _ in range(6)]  # Roll 6 times
    print("Results number 2:", results2)  # Display the final results for all 6

main()