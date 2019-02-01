import binarizer as bin
import utils
import stringUtils
import os

import json
import cv2 as cv

bible = 'Muenchen'
binar = bin.Binarizer(bible)

with open('JsonUtils/groundTruthDictionary.json') as groundTruth:
    dictionary = json.load(groundTruth)

with open('JsonUtils/angles.json') as aj:
    angles = json.load(aj)

# Variabile a True significa che e` possibile vedere le pagine singolarmente, altrimenti provvede a salvare le frequent
# words nella apposita cartella (richiede qualche minuto)
"""
inspector = False

if inspector:

    for numPage in range(14, 21):
        binar.linesCropping('GenesisPages/old/Muenchen/Gut-0{x}.jpg'.format(x=numPage),
                            numPage,
                            '_P{x}_C0'.format(x=(numPage - 14)),
                            '_P{x}_C1'.format(x=(numPage - 14)),
                            dictionary,
                            angles,
                            None,
                            None,
                            None
                            )


else:
    with open('JsonUtils/10mostFrequentWords.json') as fq:
        frequentWords = json.load(fq)

    # Dizionario delle posizioni assolute rispetto alla pagina di ciascuna parola, per creare successivamente le
    # annotazioni. La chiave piu` esterna rappresenta il numero di pagina che ha come valore un altro dizionario.
    # Quest`ultimo ha come chiavi le parole frequenti e come valore una lista di tuple. Ciascuna di esse rappresenta
    # la posizione all`interno della pagina. Es: "et": [(p1, p2, p3, p4), (p5, p6, p7, p8)...] (i punti sono presi
    # partendo dall`alto, da sinista a destra.

    inPagePositions = dict()

    for frequentWord in frequentWords:

        with open('JsonUtils/{frequentWord}Positions.json'.format(frequentWord=frequentWord)) as dfw:
            wordPositions = json.load(dfw)

        print()
        print(frequentWord)

        for numPage in range(14, 34):

            print("Page: " + str(numPage))

            if numPage not in inPagePositions.keys():
                inPagePositions[numPage] = dict()

            binar.linesCropping('GenesisPages/old/Muenchen/Gut-0{x}.jpg'.format(x=numPage),
                                numPage,
                                '_P{x}_C0'.format(x=(numPage - 14)),
                                '_P{x}_C1'.format(x=(numPage - 14)),
                                dictionary,
                                angles,
                                wordPositions,
                                frequentWord,
                                inPagePositions
                                )

    with open('inPagePositions.json', 'w') as pp:
        json.dump(inPagePositions, pp)

"""

numImage = 1
for numPage in range(14, 29):
    numImage = utils.splitColumns('GenesisPages/old/MuenchenRotated/Gut-{x}.png'.format(x=numPage), numPage, numImage)

for file in os.listdir("train2019/"):
    os.rename("train2019/{file}".format(file=file), "train2019/{file}".format(file=file.zfill(9)))

annotationId = 0
for x in range(14, 29, 1):
    if x % 2 == 0:
        cutWidthLeft = 450
        cutWidthRight = 450
    else:
        cutWidthLeft = 470
        cutWidthRight = 430
    annotationId = utils.setAnnotations(nPage=x, cutWidthLeft=cutWidthLeft, cutWidthRight=cutWidthRight, cutHeight=250,
                                        annotationId=annotationId)

