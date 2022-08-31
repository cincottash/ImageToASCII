from setup import *
from PIL import Image
from math import sqrt

def main():
    #dark to bright
    asciiText = '@%#*+=-:. '
    
    imag = Image.open("test.png")

    #Convert the image te RGB if it is a .gif for example
    imag = imag.convert ('RGB')

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
