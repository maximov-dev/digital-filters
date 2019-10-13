from filter import Filter
from helpers.filter_math_helper import FilterMath
from signals_basic import Signal

FILTER_WINDOW = 30

MIN_ARRAY_VALUE = 1
MAX_ARRAY_VALUE = 100
LENGTH_ARRAY = 10000

if __name__ == '__main__':
    signal_base = Signal(MIN_ARRAY_VALUE, MAX_ARRAY_VALUE, LENGTH_ARRAY)
    number_array, x_volts = signal_base.generate_signal()
    signal_base.show_signal(number_array, x_volts, 'исходный')
    print(len(number_array))

    x_volts = signal_base.generate_random(len(x_volts)) + x_volts
    signal_base.show_signal(number_array, x_volts, 'с шумом')
    print(len(x_volts))

    filter_signal1 = Filter(FILTER_WINDOW, FilterMath.avg)
    x_volts = filter_signal1.filter(x_volts) #ФИЛЬТР СКОЛЬЗЯЩЕГО СРЕДНЕГО

    #filter_signal1 = Filter(FILTER_WINDOW, FilterMath.median)
    #x_volts = filter_signal1.filter(x_volts) #МЕДИАННЫЙ ФИЛЬТР

    print(len(x_volts))
    signal_base.show_signal(number_array, x_volts, 'пропущенный через фильтр')
    #x_volts = [filter_signal1.filter(point) for point in x_volts]
