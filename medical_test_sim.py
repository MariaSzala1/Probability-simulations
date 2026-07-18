# In this project I will make a function that will check how reliable
# a positive medical test result is
import numpy as np

# calculates the amount of people that have a disease in a population
# (where people that don't have it is healthy = population - sick)
def disease(population: int, prob_disease: float):
    
    disease_list = []

    # simulating who was tested positive ad negative for the disease
    for i in range(population):
        sick = np.random.binomial(1, prob_disease)
        disease_list.append(sick)

    result_sick = 0
    result_healthy = 0

    # counting the amount of sick and healthy people
    for i in disease_list:
        if i == 1:
            result_sick += 1

        if i == 0:
            result_healthy += 1

    return result_sick
    
# checks whether the test result was correct
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


    

