# I want to make a function that will calculate the probability
# of at least two people having the same birthday

def birthday_probability(people: int):
    # we assume that there are 365 days in a year
    days = 365
    probability_not_same = 1

    if people < 0:
        raise ValueError("Number of people cannot be negative")
    
    if people > 365:
        return f"The probability that at least 2 people out of {people} have the same birthday is 100%"
    
    if people < 2:
        return f"The probability that at least 2 people out of {people} have the same birthday is 0%"
    

    # First calculate the probability that everyone has a different birthday
    for i in range(people):
        probability_not_same *= days/365
        days -= 1

    # Then subtract that from 1, to get the probability of at least 2 people
    # having the same birthday
    p = (1 - probability_not_same) * 100
    rounded_p = round(p, 2)

    return f"The probability that at least 2 people out of {people} have the same birthday is {rounded_p}%"

print(birthday_probability(5))

print(birthday_probability(23))

print(birthday_probability(143))

print(birthday_probability(376))

print(birthday_probability(1))