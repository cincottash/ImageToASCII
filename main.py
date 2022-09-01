from os.path import exists
import subprocess as sp
from PIL import Image
from math import sqrt

def main():
    #dark to bright
    asciiText = '@%#*+=-:. '
   
    #asciiText = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\\\"^`'. "
    imag = Image.open("test.png")

    #Convert the image te RGB if it is a .gif for example
    imag = imag.convert ('RGB')

    commandList = ['rm', 'out.txt']

    if not exists('out'):
        print('Found existing output file: out.txt, removing file')
        sp.run(commandList)

    with open('out.txt', 'w') as outFile:
        for px in range(imag.size[0]):
            outFile.write('\n')
            for py in range(imag.size[1]):
                #Get RGB
                pixelRGB = imag.getpixel((px, py))
                R,G,B = pixelRGB 

                #0 is dark, 255 is bright
                brightness = sum([R,G,B])/3
                #print(brightness)

                #normalize between 0 and the length of the chars
                normal = int(brightness/255 * len(asciiText))   
                outFile.write(asciiText[normal])



if __name__ == '__main__':
    main()
