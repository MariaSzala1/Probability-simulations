import matplotlib.pyplot as plt
import random

def mean_of_dice_rolls(rolls: int, sides: int):
    # Calculates the mean of an n sided-dice rolled a set amount of times
    roll_results = []
    for i in range(rolls):
        roll = random.randint(1, sides)
        roll_results.append(roll)
    mean = (sum(roll_results)/rolls)

    return mean

# create a plot to show the mean of rolling a dice with n sides a set amount of times

def plot_dice(sides: int):
    number_rolls = []
    mean_results = []
    theoretical_mean = sum(range(sides + 1)) / sides

    for i in range(1,1001):
        number_rolls.append(i)
        mean_results.append(mean_of_dice_rolls(i, sides))

    plt.figure()
    plt.plot(number_rolls, mean_results)
    plt.title(f"Mean of rolling a {sides} sided dice")
    plt.xlabel("Number of rolls")
    plt.ylabel("Mean")
    plt.axhline(y=theoretical_mean, color="red", linestyle="--") # highlights the theoretical mean
    figure = plt.gcf()
    plt.show()

    return figure

# Runs examples above only when this file is run directly
if __name__ == "__main__":
    print(mean_of_dice_rolls(rolls = 8, sides =6))
    print(mean_of_dice_rolls(rolls = 164, sides =6))
    plot_dice(6)

