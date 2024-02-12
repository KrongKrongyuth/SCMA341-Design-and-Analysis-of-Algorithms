"""
This file for longest substring search algorithm
"""

class Competition():
    def __init__(self, text_1, text_2):
        self.text_1 = text_1
        self.text_2 = text_2

    def tao_algorithm(self):
        """
        Algorithm from tao
        """

    def kantong_algorithm(self):
        """
        Algorithm from kantong
        """

    def tonkaow_algorithm(self):
        """
        Algorithm from tonkaow
        """

    def ton_algorithm(self):
        """
        Algorithm from ton
        """
        import numpy as np
        possible_result, i = [], 0
        while i < len(self.text_1):
            j, k, word = 0, 0, ""
            while j + k < len(self.text_2):
                if (text_1[i+k] == text_2[j+k]):
                    word += text_2[j+k]
                    k += 1
                j += 1
            if k != 0: possible_result.append([word, k])
            i += 1
        result = possible_result[np.argmax(np.array(possible_result)[:,1])]
        print(f"\nLongest substring is \"{result[0]}\" with \"{result[1]}\" letters.\n")
        return result

if __name__ == "__main__":
    text_1 = "parachute"
    text_2 = "shuttle"
    com = Competition(text_1 = text_1, text_2 = text_2)
    com.ton_algorithm()     # How to run your function.
