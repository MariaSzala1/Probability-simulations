# An investor starts with a certain amount of money. Each period, the investment
# either gains or loses value. The simulation ends when the investment reaches
# the target value, or falls to zero. We are interested in the probability
# of reaching the target value.
import random
import matplotlib.pyplot as plt

def investment_sim(initial_investment: int, target_value: int, p_gain: float, 
                   gain_amount: int):
    current_value = initial_investment 

    if current_value >= target_value:
        return 1
    
    if current_value <= 0:
        return 0
    
    while current_value > 0 and current_value < target_value:
        # we are going to generate a random number between 0 and 1
        # if the number is smaller than p_gain, then we increase the current value.
        # if its bigger than p_gain, then we decrease the current value.
        p = random.random()
        if p < p_gain:
            current_value += gain_amount
        else:
            current_value -= gain_amount

        if current_value >= target_value:
            return 1
        
        elif current_value <= 0:
            return 0
        
# now we are going to create a function that will perform the simulation
# a set number of times and will tell us the probability of reaching the 
# target value

def run_simulation(amount_simulations: int, initial_investment: int, 
                   target_value:int, p_gain:float, gain_amount:int):
    results = []
    for i in range(amount_simulations):
        results.append(investment_sim(initial_investment, target_value, p_gain, gain_amount))
    
    target_reached = sum(results)
    
    probability = target_reached/amount_simulations

    return probability

# Creates a plot that will show the probability of reaching the target value 
# for different initial investments
def investment_plot(amount_simulations:int, lower: int, upper: int, jump: int,
                    target_value:int, p_gain:float, gain_amount:int):
    initial_invest = [] # empty list for all initial investments
    probs = [] #empty list for the probabilities from simulations

    for n in range(lower, upper, jump):
        initial_invest.append(n)
        probs.append(run_simulation(amount_simulations, n, target_value,
                                    p_gain, gain_amount))

    plt.figure()
    plt.plot(initial_invest, probs)
    plt.title("Probabilities of reaching the target for different initial amounts")
    plt.xlabel("Initial investment (in Euro)")
    plt.ylabel("Probability of reaching the target")
    figure = plt.gcf()
    plt.show()
    return figure

# runs the example below only when this file is run directly
if __name__ == "__main__":
    print(run_simulation(10000, 1000, 2500, 0.55, 250))
    investment_plot(10000, 500, 2000, 100, 2500, 0.55, 250)


    



    
