# An investor starts with a certain amount of money. Each period, the investment
# either gains or loses value. The simulation ends when the investment reaches
# the target value, or falls to zero. We are interested in the probability
# of reaching the target value.
import random
import matplotlib.pyplot as plt
initial_investment = 1000
target_value = 2500
p_gain = 0.55
amount = 250 # the amount of money gained or lost each period

def investment_sim(initial_investment: int, target_value: int, p_gain: float, amount: int):
    current_value = initial_investment 
    while current_value > 0 and current_value < target_value:
        # we are going to generate a random number between 0 and 1
        # if the number is smaller than p_gain, then we increase the current value.
        # if its bigger than p_gain, then we decrease the current value.
        p = random.random()
        if p < p_gain:
            current_value += amount
        else:
            current_value -= amount

        if current_value >= target_value:
            return 1
        
        elif current_value <= 0:
            return 0
        
# now we are going to create a function that will perform the simulation
# a set number of times (in this case 10000) and will tell us the probability of reaching
# the target value

amount_simulations = 10000

def run_simulation(amount_simulations: int, initial_investment: int):
    results = []
    for i in range(amount_simulations):
        results.append(investment_sim(initial_investment, target_value, p_gain, amount))
    
    target_reached = sum(results)
    
    probability = target_reached/amount_simulations

    return probability

# now we are going to create a plot that will show the probability of reaching the 
# target value for different initial investments
initial_invest = [] # empty list for all initial investments
probs = [] #empty list for the probabilities from simulations

for n in range(500, 2000, 100):
    initial_invest.append(n)
    probs.append(run_simulation(amount_simulations, n))

plt.plot(initial_invest, probs)
plt.title("Probabilities of reaching the target for different initial amounts")
plt.xlabel("Initial investment (in Euro)")
plt.ylabel("Probability of reaching the target")
plt.show()





    



    
