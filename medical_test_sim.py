# In this project I will make a function that will check how reliable
# a positive medical test result is
import numpy as np
import matplotlib.pyplot as plt

# calculates the amount of people that have a disease in a population
# (where people that don't have it is healthy = population - sick)
def disease(population: int, prob_disease: float):
    
    disease_list = []

    # simulating who is sick and who is healthy
    for i in range(population):
        sick = np.random.binomial(1, prob_disease)
        disease_list.append(sick)

    result_sick = 0
    result_healthy = 0

    # counting the amount of sick and healthy people
    for i in disease_list:
        if i == 1:
            result_sick += 1

    return result_sick
    
# simulates the true and false positive and negative results
def correctness_test(population: int, prob_disease: float, 
                     correct_positive: float, correct_negative: float):
    
    # simulating the actual amount of sick and healthy people
    result_sick = disease(population, prob_disease)
    result_healthy = population - result_sick

    # simulating the test results for sick people
    true_positive = np.random.binomial(result_sick, correct_positive)
    false_negative = result_sick - true_positive # tested healthy, were sick

    # simulating the test results for healthy people
    true_negative = np.random.binomial(result_healthy, correct_negative)
    false_positive = result_healthy - true_negative # tested sick, were healthy

    return true_positive, true_negative, false_positive, false_negative

# calculates how reliable positive and negative results are
def reliability_test(population: int, prob_disease: float, 
                     correct_positive: float, correct_negative: float):
    
    # get the results of the correctness test
    true_positive, true_negative, false_positive, false_negative = (
        correctness_test(population, prob_disease, correct_positive, correct_negative))
    
    total_positive = true_positive + false_positive
    total_negative = true_negative + false_negative
    
    # given that someone tested positive, how likely are they to actually be sick

    if total_positive == 0: # handling the case when there are no sick people
        positive_reliability = None

    else:
        positive_reliability = round(true_positive / total_positive, 2)

    # given that someone tested negative, how likely are they to actually be healthy

    if total_negative == 0: # handling the case when no one is healthy
        negative_reliability = None

    else:
        negative_reliability = round(true_negative / total_negative, 2)

    return positive_reliability, negative_reliability

# creates a plot that compares the test reliability with the disease probability
def plot(population: int, correct_positive: float, correct_negative: float):
    # we'd like to make this plot for many disease probabilities,
    # here I'm going to take ones from 0.05 to 0.6
    dis_probabilities = np.linspace(0.05, 0.6, 55)

    positive_reliabilities = []
    negative_reliabilities = []
    
    for i in dis_probabilities:
        positive_reliability, negative_reliability  = reliability_test(population, i, correct_positive, correct_negative)
        positive_reliabilities.append(positive_reliability)
        negative_reliabilities.append(negative_reliability)

    # Create separate plots for positive and negative probabilities
    plt.figure()
    plt.plot(dis_probabilities, positive_reliabilities, label = "Reliability of a positive test")
    plt.plot(dis_probabilities, negative_reliabilities, label = "Reliability of a negative test", color = "red")
    plt.title("Test reliability for different disease probabilities")
    plt.xlabel("Disease probabilities")
    plt.ylabel("Test reliability")
    figure = plt.gcf()
    plt.legend()
    plt.show()

    return figure


# runs the examples below only if the file is run directly
if __name__ == "__main__":
    print(disease(1000, 0.4))
    print(correctness_test(1000, 0.4, 0.9, 0.95))
    print(reliability_test(1000, 0.4, 0.9, 0.95))
    plot(1000, 0.9, 0.95)

    

