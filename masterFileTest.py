#master file TEST
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,  QLineEdit, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot 
import PIL
from PIL import Image, ImageDraw, ImageFont,  ImageQt
from random import*
import flickrapi
import urllib

'''
creat drop down men that selects
meme genre for lines
and create drop down for meme
genre for image then user
clicks generate meme


'''


class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Meme Generator'
        self.left = 400
        self.top = 400
        self.width = 320
        self.height = 200
        self.initUI()
 
    def initUI(self):
        


        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
     
        button = QPushButton('Generate Meme', self)
        button.setToolTip('This is an example button')
        button.move(100,70)


        
        button.clicked.connect(self.on_click)
 
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        '''
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

        image.save("endme.jpg")
        image.show()
        '''
        
        category = ["dog","cat","pizza","bird","christmas","car","school","egg"]
        randCatg = randint(0,len(category))
        flickr=flickrapi.FlickrAPI('98c9e8d1dbaeae46f08c5cccac21c21e', 'aea1eced4673a3f8', cache=True)
        keyword = category[randCatg]

        photos = flickr.walk(text=keyword,
                             tag_mode='all',
                             tags=keyword,
                             extras='url_c',
                             per_page=100,           
                             sort='relevance')

        urls = []
        
        for i, photo in enumerate(photos):
           # print (i)
            
            url = photo.get('url_c')
            if(url != None):
                urls.append(url)
            
            # get 50 urls
            if i >= 100:
                break
        num = randint(1,len(urls)-2)
        if(urls[num] == None):
            image = Image.open('none.jpg')
            image = image.resize((1000,1000), Image.ANTIALIAS)
            image.save('yourMeme.jpg')
            image.show()
        else:
            #print("WE GOOD")
            print(urls[num])
            urllib.request.urlretrieve(urls[num], 'yourMeme.jpg')
            image = Image.open('yourMeme.jpg') 
            image = image.resize((600, 600), Image.ANTIALIAS)
            image.save('yourMeme.jpg')
            image.show()




        
        line1 = ["Seasme street didn't prepare me\n for any of this shit"]
        line2 = ["Fuck you Big Bird"]


        image = Image.open("yourMeme.jpg")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size=30)

        #starting position of the image
        (x, y) = (10, 70)
        message = line1[0]
        color = 'rgb(255,255,255)' #black color

        #draw the message on the background

        draw.text((x,y), message, fill=color, font=font)
        (x,y)= (10,400)
        name = line2[0]
        color = 'rgb(255,255,255)' #white color
        draw.text((x,y), name, fill=color, font=font)

        #save image and hope it work

        image.save("yourMeme.jpg")
        image.show()














      
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
