import binarizer as bin
import cv2 as cv
import stringUtils
import json

bible = 'Muenchen'
binar = bin.Binarizer(bible)

#binar.binarize()

"""img = cv.imread('threshed.png')
cropped = cv.imread('cropped.png')
binar.calimero(img, cropped)"""

with open('groundTruthDictionary.json') as groundTruth:
    dictionary = json.load(groundTruth)

# Problemi patologici su pag14, cattiva segmentazione su pag31



#for numPage in range(14, 33):

numPage = 33

binar.linesCropping('GenesisPages/old/Muenchen/Gut-0{x}.jpg'.format(x=numPage),
                    numPage,
                    '_P{x}_C0'.format(x=(numPage - 14)),
                    '_P{x}_C1'.format(x=(numPage - 14)),
                    dictionary)
