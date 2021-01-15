from PIL import Image

# Created by L.D. Moon AKA BathThief
# Image -must- be black and white pixels. Pure white pixels will be printed as blocks.


def main():
    # To change the image input change the address of the image below.
    # I tested with BMP but it should work with PNG and JPG.
    img = Image.open("export.bmp")
    pixels = img.load()
    print(img)
    for y in range(img.height):
        row = '\''
        for x in range(img.width):
            if pixels[x, y] == (255, 255, 255):
                row += '██'
            else:
                row += '  '
        row += '\''
        print(row)


if __name__ == '__main__':
    main()
    input()




