iterator = iter(callable, sentinel)  # can create infinite iterator
# time example
with open("", "rt") as f:
    lines = iter(lambda: f.readline().strip(), "END")
    readings = [int(line) for line in lines]
