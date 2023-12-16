import random

min_value = 1
max_value = 6
roll_again = "y"
while roll_again == "y":
    print("Rolling the dices...")
    value1 = random.randint(min_value, max_value)
    value2 = random.randint(min_value, max_value)
    print(f'Rolled {value1} & {value2}')
    roll_again = input("\nWant to roll again? (y/n): ")
    roll_again = roll_again.lower()

print("Have a good day.")
