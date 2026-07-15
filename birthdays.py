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

# printing rounded probabilities for an easier interpretation

print(round(birthday_probability(5), 2))

print(round(birthday_probability(23), 2))

print(round(birthday_probability(46), 2))

print(round(birthday_probability(376), 2))

print(round(birthday_probability(1), 2))

# now we are going to create a plot to show the probability of at least two
# people having the same birthday for different numbers of people
import matplotlib.pyplot as plt
amount_people = []
probabilities = []

for i in range(1, 366):
    amount_people.append(i)
    probabilities.append(birthday_probability(i))


plt.plot(amount_people, probabilities)
plt.title("Probability of at least two people having the same birthday")
plt.xlabel("Number of people")
plt.ylabel("Probability")
plt.xticks(range(0, 366, 25))
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.axvline(x=23, color="red", linestyle="--") # highlights the 23 people mark
plt.scatter(23, birthday_probability(23), color="red")
plt.axvline(x=46, color="blue", linestyle="--") # highlights the 46 people mark
plt.scatter(46, birthday_probability(46), color="blue")
plt.show()