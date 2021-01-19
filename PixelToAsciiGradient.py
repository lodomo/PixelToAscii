from PIL import Image

# Created by L.D. Moon AKA BathThief

# ██ 80-100 White
# ▓▓ 60-80
# ▒▒ 40-60
# ░░ 20-40
#    0-20%


def grey_percentage(rgb_value):
    red = rgb_value[0]
    green = rgb_value[1]
    blue = rgb_value[2]
    grey = (0.3 * red) + (0.59 * green) + (0.11 * blue)
    return grey


def make_art():
    img = Image.open("import.png")
    pixels = img.load()
    output = []
    for y in range(img.height):
        row = '\''
        for x in range(img.width):
            grey_scale = grey_percentage(pixels[x, y])
            if grey_scale > 204:
                row += '██'
            elif grey_scale > 153:
                row += '▓▓'
            elif grey_scale > 102:
                row += '▒▒'
            elif grey_scale > 51:
                row += '░░'
            else:
                row += '  '
        row += '\','
        print(row)


if __name__ == '__main__':
    make_art()
    input()


