

#ERROR CHECKING
#if the URL type is "None" in this case we
#need a back up image, and we will use this
#using conditionals
#SAMPLE CODE
'''
if(url[i] == "None"):
    then use backupImage
else:
    use input image
'''

import flickrapi
import urllib
from PIL import Image
from random import*



# Flickr api access key 
flickr=flickrapi.FlickrAPI('98c9e8d1dbaeae46f08c5cccac21c21e', 'aea1eced4673a3f8', cache=True)

enter = input("Enter meme image:")
keyword = enter

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,           
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):
    print (i)
    
    url = photo.get('url_c')
    if(url != None):
        urls.append(url)
    
    # get 50 urls
    if i >= 100:
        break

print (urls)
print(len(urls))
print("number of URLS above")
num = randint(1,len(urls)-2)


# Download image from the url and save it to '00001.jpg'


#do for loop that gets rid of all "None" URLs
#if all are none then use backup image
print("THE RANDOM NUMBER IS "+ str(num))
if(urls[num] == None):
    image = Image.open('none.jpg')
    image = image.resize((600,600), Image.ANTIALIAS)
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




'''
import flickrapi
import urllib
from PIL import Image

flickr=flickrapi.FlickrAPI('98c9e8d1dbaeae46f08c5cccac21c21e', 'aea1eced4673a3f8', cache=True)

keyword = 'dog'

photos = flickr.walk(text=keyword, tag_mode='all', tags=keyword, extras='url_c', per_page=100, sort='relevance')



urls = []

for i, photo in enumerate(photos):
    print(i)

    url = photo.get('url_c')
    urls.append(url)

    if i > 5:
        break
print(urls)

urllib.request.urlretrieve(urls[1], '00003.jpg')

# Resize the image and overwrite it
image = Image.open('00003.jpg') 
image = image.resize((256, 256), Image.ANTIALIAS)
image.save('00003.jpg')
image.show()
'''
