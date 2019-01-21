import random

class PerceptronTable:
    def __init__(self, perceptron):
        """

        :param perceptrons: dictionary[integer]
        """
        self.perceptron = perceptron

    @staticmethod
    def perceptron_table_generator(weights_num,perceptron_num,perceptron_table):
        """
        Generate a perceptron table with random weight initialized
        :param weights_num:
        :param perceptron_num:
        :param perceptron_table:
        :return:
        """
        for i in range(perceptron_num):
            weights = []
            for j in range(weights_num):
                weights.append(random.random())
            perceptron_table[i] = weights


