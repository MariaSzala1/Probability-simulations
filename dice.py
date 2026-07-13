
def mean_of_dice_rolls(rolls: int, sides: int):
    # Calculates the mean of an n sided-dice rolled a set amount of times
    import random
    roll_results = []
    for i in range(rolls):
        roll = random.randint(1, sides)
        roll_results.append(roll)
    mean = (sum(roll_results)/rolls)

    return (f"The mean of rolling a {sides} sided dice {rolls} times is: {mean}")
        
print(mean_of_dice_rolls(rolls = 72, sides = 6))



