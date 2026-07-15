
def mean_of_dice_rolls(rolls: int, sides: int):
    # Calculates the mean of an n sided-dice rolled a set amount of times
    import random
    roll_results = []
    for i in range(rolls):
        roll = random.randint(1, sides)
        roll_results.append(roll)
    mean = (sum(roll_results)/rolls)

    return mean
        
print(mean_of_dice_rolls(rolls = 72, sides = 6))

# create a plot to show the mean of rolling a dice with 6 sides a set amount of times
import matplotlib.pyplot as plt
number_rolls = []
mean_results = []

for i in range(1,1000):
    number_rolls.append(i)
    mean_results.append(round(mean_of_dice_rolls(i, 6), 2))


plt.plot(number_rolls, mean_results)
plt.title("Mean of rolling a 6 sided dice")
plt.xlabel("Number of rolls")
plt.ylabel("Mean")
plt.axhline(y=3.5, color="red", linestyle="--") # highlights the theoretical mean
plt.show()


