from PIL import Image

im1 = Image.open('a.jpg') #The first image must be RGBA, and this image using for background.
im2 = Image.open('b.png') #The second image too,must be RGBA, and the scale must be same with first image.
im3 = Image.open('c.png')
im1.save("out.gif", save_all=True, append_images=[im2, im3], duration=100, loop=0)

#You can add more "im" variables, and then just put it in here "append_images=[]".
#append_images=[im2, im3, im4, im5] like that.