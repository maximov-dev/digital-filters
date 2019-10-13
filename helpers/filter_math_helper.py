import math


class FilterMath:

    @staticmethod
    def avg(value_array):
        return sum(value_array) / len(value_array)

    @staticmethod
    def median(value_array):
        length = len(value_array)
        length_half = math.floor(length / 2)
        value_array = sorted(value_array)

        if length % 2:
            return value_array[length_half]
        else:
            return (value_array[length_half] + value_array[length_half])/2
