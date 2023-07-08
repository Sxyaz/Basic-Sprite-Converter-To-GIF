from PIL import Image

image1 = Image.open("first.jpg") #The first image must be RGBA, and this image using for background.
image2 = Image.open("second.png") #The second image too,must be RGBA, and the scale must be same with first image.
image3 = Image.open("third.png")
#image4 = Image.open("fourth.png")
image1.save("Result.gif", save_all = True, append_images=[image2, image3, image4], duration = 200, loop = 0)

#You can add more "image" variables, and then just put it in here "append_images=[]".
#append_images=[image2, image3, image4, image5] like that.
#High Duration -> Low Speed, Low Duration -> High Speed