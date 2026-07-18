# Probability simulations
This is a collection of small Python projects created while practicing programming and probability. The main idea is to understand the logic behind common probability questions better, while practicing programming.

## Current Projects

### 1. Dice roll simulation
Lets you pick the number of sides of a die, as well as the number of rolls you want to make. It shows how the mean of the observed rolls approaches the theoretical mean as the number of rolls increases. I also created a plot for a six sided die showing that the observed mean gradually approaches 3.5.

### 2. Birthday paradox
Lets you pick the number of people in a group and calculates the probability that at least two of them have the same birthday. Interestingly, we find that with only 23 people, this probability is already about 50%, and it increases to roughly 95% with 46 people. To illustrate this rapid increase, I created a plot showing how the probability changes as the number of people grows. The plot also highlights the probabilities of groups of 23 and 46 people.

### 3. Investment payoff
Lets you choose the initial value of an investment and calculates the probability that it reaches the target value before falling to zero. During each period, the investment can either gain or lose a fixed amount, based on the chosen probability of gain. I repeated the simulation 10 000 times for different initial amounts, and created a plot showing how the probability of reaching the target value changes as the initial investment increases.

### 4. Medical test simulator
Lets you choose the size of a population, the probability of having the disease, and how often the test correctly identifies sick and healthy people. It simulates the amount of true positives, true negatives, false positives, and false negatives. Based on these results, it calculates how likely someone is to actually be sick after testing positive, and how likely they are to be healthy after testing negative. It shows that the reliability of a test doesn't only depend on how accurate the test is, but also on how common the disease is. 
