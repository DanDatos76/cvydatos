from PIL import Image

 
#import Tkinter, tkFileDialog, re

im = Image.open('casos2.jpg')
im.save('logo1.png')

print("SU IMAGEN HA SIDO CONVERTIDA A PNG")