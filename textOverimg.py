from PIL import Image, ImageDraw, ImageFont

image = Image.open("pic.jpg")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=15)

#starting position of the image
(x, y) = (50, 50)
message = "Happy Birthday!"
color = 'rgb(0,0,0)' #black color

#draw the message on the background

draw.text((x,y), message, fill=color, font=font)
(x,y)= (150,150)
name = 'Vinay'
color = 'rgb(255,255,255)' #white color
draw.text((x,y), name, fill=color, font=font)

#save image and hope it work

image.save("hoptethisfuckingworks.jpg")
