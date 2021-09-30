import glob
from PIL import Image
import os
from pyzbar.pyzbar import decode

i=0
myDataPrevious = ''

path = 'D:/Programming/Python/pythonProject1/Barcodes'
for filename in glob.glob(os.path.join(path, '*.png')):
            with Image.open(filename) as img:
                for barcode in decode(img):
                        myData = barcode.data.decode('utf-8')


            text = path + '/' + myData + '_' +str(i) +'.png'
            os.rename(filename, text)
            if (myData!=myDataPrevious and myDataPrevious!=''):
                i=0
            else:
                i=i+1
            myDataPrevious = myData


