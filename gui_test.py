import sys, string
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageQt, ImageDraw, ImageFont,  ImageQt
from random import*
import flickrapi
import urllib

#test runs


filters = {"angry","happy","love","work","finals"}
category = ["dog","cat","pizza","bird","christmas","car","school","egg"]
def searchCategory(name):
    for i in range(0, len(category), 1):
        if(category[i] == name):
            return name

def set_default(memeType): 
    if memeType == "angry":
        line1 = ["Seasme street didn't prepare me\n for any of this shit"]
        line2 = ["Fuck you Big Bird"]
        return line1, line2
    if memeType == "work":
        line1 = ["Whoever stole my stapler"]
        line2 = ["I will find you, and I will kill you"]
        return line1, line2
    if memeType == "love":
        line1 = ["When you finally tell him\her \n how you feel"]
        line2 = ["And he\she leaves you on read"]
        return line1, line2
    if  memeType == "happy":
        line1 = ["When you're finally feeling\n content with your life"]
        line2 = ["but then you remember your anxiety,\n depression,  and overall quality of \n life"]
        return line1, line2
    if memeType == "finals":
        line1 = ["Strippers making $100K\n a year"]
        line2 = ["& here I am struggling cuz I got\n morals. Where the pole at?"]
        return line1, line2

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

        
        flickr = flickrapi.FlickrAPI('98c9e8d1dbaeae46f08c5cccac21c21e', 'aea1eced4673a3f8', cache=True)
        if (memeType == ""):
            keyword = "dog"
        else:
            keyword = memeType 
        photos = flickr.walk(text=keyword,
                             tag_mode='all',
                             tags=keyword,
                             extras='url_c',
                             per_page=100,           
                             sort='relevance')
        urls = []
        for i, photo in enumerate(photos):
            #print (i)
            
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
            #image.show()
        else:
            #print("WE GOOD")
            print(urls[num])
            urllib.request.urlretrieve(urls[num], 'yourMeme.jpg')
            image = Image.open('yourMeme.jpg') 
            image = image.resize((600, 600), Image.ANTIALIAS)
            image.save('yourMeme.jpg')
            #image.show()
        

        # if self.dropDown.currentText() == "angry":
        #     line1 = ["Seasme street didn't prepare me\n for any of this shit"]
        #     line2 = ["Fuck you Big Bird"]
        # if self.dropDown.currentText() == "work":
        #     line1 = ["Whoever stole my stapler"]
        #     line2 = ["I will find you, and I will kill you"]
        # if self.dropDown.currentText() == "love":
        #     line1 = ["When you finally tell him\her \n how you feel"]
        #     line2 = ["And he\she leaves you on read"]

        # if self.dropDown.currentText() == "happy":
        #     line1 = ["When you're finally feeling\n content with your life"]
        #     line2 = ["but then you remember your anxiety,\n depression,  and overall quality of \n life"]
        # if self.dropDown.currentText() == "finals":
        #     line1 = ["Strippers making $100K\n a year"]
        #     line2= ["& here I am struggling cuz I got\n morals. Where the pole at?"]

        if (line1 == "" and line2 == ""):
            line1 , line2 = set_default(memeType)
        #     

        image = Image.open("yourMeme.jpg")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size=35)

        #starting position of the image
        (x, y) = (10, 70)
        message = line1[0]

        color = 'rgb(255,255,255)' 

        #draw the message on the background

        draw.text((x,y), message, fill=color, font=font)
        (x,y)= (10,400)
        name = line2[0]
        color = 'rgb(255,255,255)' #white color
        draw.text((x,y), name, fill=color, font=font)

        #save image and hope it work

        image.save("yourMeme.jpg")
        image.show()


app = QApplication(sys.argv)
box = Window()
sys.exit(app.exec_())
ff5
