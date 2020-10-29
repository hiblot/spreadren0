import os
import os.path
import imdb
import shutil

listFilesBefore = []
listFilesAfter = []
ia = imdb.IMDb()

def listTargetRep():
    file = open('conf/rep.nhi', "r")
    line = file.readline()
    file.close()
    variaREP = line.strip()
    return variaREP

def datzETr(fileNametoTr,indexGil):

    # Etape 1 : on remplace toutes les fins de ligne
    root_ext = os.path.splitext(fileNametoTr)
    fileNametoTr = root_ext[0]
    extensionNewFileName = root_ext[1]
    listFilesAfter[indexGil] = fileNametoTr
    #print(listFilesAfter)
    # print("~~~~~~~~~~~~~~~ EO STEP 1 ~~~~~~~~~~~~~~~~~~~~~~~~")

    # Etape 2 : on remplace tous les . par des espaces
    fileNametoTr = fileNametoTr.replace('.', ' ')
    listFilesAfter[indexGil] = fileNametoTr
    #print(listFilesAfter)
    # print("~~~~~~~~~~~~~~~ EO STEP 2 ~~~~~~~~~~~~~~~~~~~~~~~~")

    #Etape 3 : Pour chaque titre de film on realise une recheche sur IMDB
    movieFind = ia.search_movie(fileNametoTr)
    if movieFind != 0:
        movieGet = ia.get_movie(movieFind[0].movieID)
        print(movieGet)

        #print(movieFind[0].movieID)
        genreTMP = movieGet['genres'][0]
        for genre in movieGet['genres']:
            #print("#### genre : " + genre)
            if genre == "Animation":
                genreTMP = genre
                break
            elif genre == "Fantasy":
                genreTMP = genre
            elif genre == "Sci-Fi":
                genreTMP = genre
            elif genre == "Mystery":
                genreTMP = genre

        listFilesAfter[indexGil] = genreTMP

        # On prend le nom du fichier de sortie
        newFileName = movieGet['title']
        newFileName = newFileName.replace(' ', '.')
        newFileName = newFileName.replace('-', '.')
        newFileName = newFileName.replace('_', '.')
        newFileName = newFileName + extensionNewFileName
        #print("newFileName : " + newFileName)
    return newFileName

    # print("~~~~~~~~~~~~~~~ EO STEP 3 ~~~~~~~~~~~~~~~~~~~~~~~~")


def get_dirToMove(genre):
    if(genre == "Action"):
        pathToMove="01.ACTION"
    elif(genre == "Adventure"):
        pathToMove="02.AVENTURE"
    elif(genre == "Animation"):
        pathToMove="03.ANIMATION"
    elif(genre == "Biography"):
        pathToMove="04.BIOGRAPHIE"
    elif(genre == "Comedy"):
        pathToMove="05.COMEDIE"
    elif(genre == "Crime"):
        pathToMove="06.CRIME"
    elif(genre == "Documentary"):
        pathToMove="07.DOCUMENTAIRE"
    elif(genre == "Drama"):
        pathToMove="08.DRAME"
    elif(genre == "Family"):
        pathToMove="09.FAMILLE"
    elif(genre == "Fantasy"):
        pathToMove="10.FANTASY"
    elif(genre == "Film Noir"):
        pathToMove="11.FILM_NOIR"
    elif(genre == "History"):
        pathToMove="12.HISTORIQUE"
    elif(genre == "Horror"):
        pathToMove="13.HORREUR"
    elif(genre == "Music"):
        pathToMove="14.MUSICAL"
    elif(genre == "Musical"):
        pathToMove="14.MUSICAL"
    elif(genre == "Mystery"):
        pathToMove="15.MYSTERE"
    elif(genre == "Romance"):
        pathToMove="16.ROMANCE"
    elif(genre == "Sci-Fi"):
        pathToMove="17.SCI-FI"
    elif(genre == "Short Film"):
        pathToMove="18.SHORT_CM"
    elif(genre == "Sport"):
        pathToMove="19.SPORT"
    elif(genre == "Superhero"):
        pathToMove="20.SUPER_HEROS"
    elif(genre == "Thriller"):
        pathToMove="21.THRILLER"
    elif(genre == "War"):
        pathToMove="22.GUERRE"
    elif(genre == "Western"):
        pathToMove="23.WESTERN"
    else:
        pathToMove="29.ERREUR_DE_CLASSEMENT"
    return pathToMove


def mainFunc():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("-- spreadren0  v1.0 -- Spread Files smoothly -- October 2020  -- 2020 HIBLOT.COM --")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    variaREP = listTargetRep()
    indexFile = 0
    indexFileMove = 0

    for root, directories, files in os.walk(variaREP):
        for file in files:
            print(file)
            listFilesBefore.append(file)
            listFilesAfter.append(file)
            newFileName = datzETr(listFilesAfter[indexFile], indexFile)

            # Une fois le type de Film recupere on deplace le fichier correspondant dans le bon dossier
            if os.path.exists((os.path.abspath(variaREP) + '/' + listFilesBefore[indexFile]).strip()):
                if listFilesAfter[indexFile] != listFilesBefore[indexFile]:
                    #print("## newFileName : " + newFileName)
                    oldPlace = (os.path.abspath(variaREP) + '/' + listFilesBefore[indexFile]).strip()
                    newPlace = (os.path.split(os.path.abspath(variaREP))[0] + '/'
                    #+ get_dirToMove(listFilesAfter[indexFile]) + '/' + listFilesBefore[indexFile]).strip()
                    + get_dirToMove(listFilesAfter[indexFile]) + '/' + newFileName).strip()
                    print("~~~~~ oldPlace : " + oldPlace)
                    print("~~~~~ newPlace : " + newPlace)
                    shutil.move(oldPlace, newPlace)
                    indexFileMove = indexFileMove + 1
            indexFile = indexFile + 1

    print ("spreadren0 Statement :  Finished : ", indexFileMove, " spreaded Files  / ", indexFile, " Files")
    print ("--()--")

mainFunc()

#Todo : Si le fichier est trouve mais qu'il a un titre original il faudrait prendre ce titre


