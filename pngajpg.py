from PIL import Image
im = Image.open('logo1.png')
im.save('ejemplo1.jpg', quality=95)

print("SU IMAGEN HA SIDO CONVERTIDA A JPG")