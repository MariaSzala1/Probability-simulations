import matplotlib.pyplot as plt
# I want to make a function that will calculate the probability
# of at least two people having the same birthday

def birthday_probability(people: int):
    # we assume that there are 365 days in a year
    days = 365
    probability_not_same = 1

    if people < 0:
        raise ValueError("Number of people cannot be negative")
    
    if people > 365:
        return 1.0
    
    if people < 2:
        return 0.0
    

    # First calculate the probability that everyone has a different birthday
    for i in range(people):
        probability_not_same *= days/365
        days -= 1

    # Then subtract that from 1, to get the probability of at least 2 people
    # having the same birthday
    p = 1 - probability_not_same

    return p


# Creates a plot to show the probability of at least two people having
# the same birthday for different groups of people
def birthday_plot():
    amount_people = []
    probabilities = []

    for i in range(1, 366):
        amount_people.append(i)
        probabilities.append(birthday_probability(i))

    plt.figure()
    plt.plot(amount_people, probabilities)
    plt.title("Probability of at least two people having the same birthday")
    plt.xlabel("Number of people")
    plt.ylabel("Probability")
    plt.xticks(range(0, 366, 25))
    plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    plt.axvline(x=23, color="red", linestyle="--") # highlights the 23 people mark
    plt.scatter(23, birthday_probability(23), color="red")
    plt.axvline(x=46, color="blue", linestyle="--") # highlights the 46 people mark
    plt.scatter(46, birthday_probability(46), color="blue")
    figure = plt.gcf()
    plt.show()
    return figure

# runs the examples below only if the file is run directly
if __name__ == "__main__":
    # printing rounded probabilities for easier interpretation
    print(round(birthday_probability(5), 2))
    print(round(birthday_probability(23), 2))
    print(round(birthday_probability(46), 2))
    print(round(birthday_probability(376), 2))
    print(round(birthday_probability(1), 2))
    # the plot itself
    birthday_plot()
