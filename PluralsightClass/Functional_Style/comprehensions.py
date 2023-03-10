simple_list = [i * 2 for i in range(10)]
simple_dict = {i: i * 2 for i in range(10)}
simple_gen = (i for i in range(10))

multiple_input = [(x, y) for x in range(5) for y in range(5)]

values = [x / (x - y)
          for x in range(100)
          if x > 50
          for y in range(100)
          if x - y != 0
          ]

reference = [(x, y) for x in range(10) for y in range(x)]

vals = [[y * 3 for y in range(x)] for x in range(10)]
outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
        outer.append(inner)
