# LED display
import time
import datetime

# bug in ~2 layout
per_line = {
    '1': ['#', '#', '#', '#', '#'],
    '2': ["###", "  #", "###", "#  ", "###"],
    '3': ["###", "  #", "###", " #", "###"],
    '4': ["#  #", "#  #", "####", "   #", "   #"],
    '5': ["###", "#  ", "###", "  #", "###"],
    '6': ["####", "#   ", "####", "#  #", "####"],
    '7': ["###", "  #", "  #", "  #", "  #"],
    '8': ["####", "#  #", "####", "#  #", "####"],
    '9': ["####", "#  #", "####", "   #", "   #"],
    '0': ["####", "#  #", "#  #", "#  #", "####"],
    ':': ["   ", " # ", '   ', " #  ", '   ']
}


def display():
    kill = False
    start_time = time.time()
    while not kill:
        time_string = datetime.datetime.now().strftime('%H:%M')
        display_string = _time_builder(time_string)
        print(display_string)
        time.sleep(1 * 60)
        end_time = time.time()
        if (end_time - start_time) >= 60 * 5:
            kill = True


def _time_builder(input_string):
    display_string = ''
    line_number = 0
    while line_number <= 4:
        for char in input_string:
            number_segments = per_line[char]
            display_string += number_segments[line_number]
            display_string += '  '
        display_string += '\n'
        line_number += 1
    return display_string


display()
