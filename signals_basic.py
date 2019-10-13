import numpy as np
import matplotlib.pyplot as plt


class Signal:
    def __init__(self, min_value, max_value, length_dots):
        self.min_value = min_value
        self.max_value = max_value
        self.length_dots = length_dots

    def generate_signal(self):
        number_array = np.linspace(self.min_value, self.max_value, self.length_dots)
        x_volts = 10 * np.sin(number_array * (2 * np.pi))
        return number_array, x_volts

    def show_signal(self, number_array, x_volts, title):
        plt.subplot(3, 1, 1)
        plt.plot(number_array, x_volts)
        plt.title('сигнал' + ' ' + title)
        plt.ylabel('вольты')
        plt.xlabel('время')
        plt.show()

    def generate_random(self, volts_count):
        return np.random.normal(0, 1, volts_count)

