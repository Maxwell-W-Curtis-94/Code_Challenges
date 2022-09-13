def better_than_average(class_points, your_points):
    return True if sum(class_points) / len(class_points) < your_points else False


if __name__ == '__main__':
    print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
    print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))
