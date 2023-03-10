def image_height(height):
    return height or 900


def image_width(width=1200):
    return width


def image_size(h=10, w=20):
    return image_width(w) * image_height(h)


print(image_size())
