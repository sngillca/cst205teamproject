import sys, string
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageQt, ImageDraw, ImageFont,  ImageQt
from random import*
import flickrapi
import urllib
import random

#Natalia Gill - Partner: Christopher Jimenez
#CST 205 Final Project: Meme Generator
#12/17/18
#ABSTRACT: Using the Flickr API and
#built-in or user entered filters/lines a
#user can generate a meme of their choice


#built-in filters
filters = {"angry","happy","love","work","finals"}


#create the GUI
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.pictureLabel = QLabel("Enter meme image, then select type for lines. ", self)
        self.label1 = QLabel("Image for meme: ", self)
        self.label2 = QLabel("Text for Line 1:", self)
        self.label3 = QLabel("Text for Line 2:", self)

        self.textLin1 = QLineEdit()
        self.dropDown = QComboBox()
        self.searchButton = QPushButton("Generate Meme",self)
        self.dropDown.addItems(filters)
        self.textLin2 = QLineEdit()
        self.textLin3 = QLineEdit()

        #Horzontal layouts
        #For user enetered lines
        layout = QHBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.textLin1)
        layout.addWidget(self.searchButton)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.label2)
        layout2.addWidget(self.textLin2)

        layout3 = QHBoxLayout()
        layout3.addWidget(self.label3)
        layout3.addWidget(self.textLin3)

        #Vertical layout
        boxLay = QVBoxLayout()
        boxLay.addLayout(layout)
        boxLay.addWidget(self.dropDown)
        boxLay.addLayout(layout2)
        boxLay.addLayout(layout3)
        boxLay.addWidget(self.pictureLabel)

        self.setLayout(boxLay)
        self.searchButton.clicked.connect(self.update_ui)
        self.setWindowTitle("Meme Generator")
        self.show()



    @pyqtSlot()
    def update_ui(self):
        count = 0
        memeType = self.textLin1.text()
        line1 = self.textLin2.text()
        line2 = self.textLin3.text()

        #ACCESS FLICKR API
        flickr = flickrapi.FlickrAPI('98c9e8d1dbaeae46f08c5cccac21c21e', 'aea1eced4673a3f8', cache=True)
        #IF USER SEARCHES FOR IMAGE, AND IT DOES NOT EXIST IN FLICKR API
        #SET DEFAULT IMAGE TO DOG
        if (memeType == ""):
            keyword = "dog"
        #IF IMAGE DOES EXIST IN FLICKR API, USE THAT IMAGE FOR BACKGROUND
        else:
            keyword = memeType 
        photos = flickr.walk(text=keyword,
                             tag_mode='all',
                             tags=keyword,
                             extras='url_c',
                             per_page=100,           
                             sort='relevance')
        urls = []
        #GATHER ALL IMAGES WITH THAT KEYWORD
        for i, photo in enumerate(photos):
            #print (i)

            #SOME URLS FOR SOME REASON WERE NULL SO
            #I ADDED A CONDITIONAL TO ONLY ADD
            #THE NOT NULL URLS
            url = photo.get('url_c')
            if(url != None):
                urls.append(url)
            
            # get 50 urls
            
            if i >= 100:
                break
        num = randint(1,len(urls)-2)

        #THIS IS A DEFAULT IMAGE WE WERE TESTING WITH
        #SAVED ON DESKTOP TITLED 'none.jpg'
        if(urls[num] == None):
            image = Image.open('none.jpg')
            image = image.resize((1000,1000), Image.ANTIALIAS)
            image.save('yourMeme.jpg')
            #image.show()

        #WE KNOW FOR THE MOST THAT WE'RE BEING
        #RETURNED URLS THAT DO WORK THIS IS WHERE
        #WE USE urllib
        else:
            print(urls[num])
            urllib.request.urlretrieve(urls[num], 'yourMeme.jpg')
            image = Image.open('yourMeme.jpg') 
            image = image.resize((700, 700), Image.ANTIALIAS)
            image.save('yourMeme.jpg')
            #image.show()


        #Use Image.Draw to write lines for meme
        #save to wherever Python is downloaded as
        #yourMeme.jpg
        image = Image.open("yourMeme.jpg")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size=35)

        #starting position of the image
        (x, y) = (10, 70)

        #built-in lines if user doesn't
        #select line filter - chosen from dropdown
        if(line1 != ""):
            message = line1
        else:
            if self.dropDown.currentText() == "angry":
                message = "Seasme street didn't prepare me\n for any of this shit"
            if self.dropDown.currentText() == "work":
                message = "Whoever stole my stapler"
            if self.dropDown.currentText() == "love":
                message = "When you finally tell him \n how you feel"
            if self.dropDown.currentText() == "happy":
                message = "When you're finally feeling\n content with your life"
            if self.dropDown.currentText() == "finals":
                message = "Strippers making $100K\n a year"
                
                
                

        color = 'rgb(255,255,255)' #white color

        #draw the message on the background
        #built-in lines if user doesn't
        #select line filter - chosen from dropdown
        draw.text((x,y), message, fill=color, font=font)
        (x,y)= (10,400)
        if(line2 != ""):
            message = line2
        else:
            if self.dropDown.currentText() == "angry":
                message = "Fuck you Big Bird"
            if self.dropDown.currentText() == "work":
                message = "I will find you, and I will kill you"
            if self.dropDown.currentText() == "love":
                message = "And he leaves you on read"
            if self.dropDown.currentText() == "happy":
                message = "but then you remember your anxiety,\n depression,  and overall quality of \n life"
            if self.dropDown.currentText() == "finals":
                message = "& here I am struggling cuz I got\n morals. Where the pole at?"
                
              

            
            
        color = 'rgb(255,255,255)' #white color
        draw.text((x,y), message, fill=color, font=font)

        image.save("yourMeme.jpg")
        image.show()


app = QApplication(sys.argv)
box = Window()
sys.exit(app.exec_())

