import os
import os.path
import imdb

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
    listFilesAfter[indexGil] = fileNametoTr
    #print(listFilesAfter)
    # print("~~~~~~~~~~~~~~~ EO STEP 1 ~~~~~~~~~~~~~~~~~~~~~~~~")

    # Etape 2 : on remplace tous les . par des espaces
    fileNametoTr = fileNametoTr.replace('.',' ')
    listFilesAfter[indexGil] = fileNametoTr
    #print(listFilesAfter)
    # print("~~~~~~~~~~~~~~~ EO STEP 2 ~~~~~~~~~~~~~~~~~~~~~~~~")

    #Etape 3 : Pour chaque titre de film on realise une recheche sur IMDB
    #TODO tester le cas ou IMDB ne trouve pas
    movieFind = ia.search_movie(fileNametoTr)
    if movieFind != 0:
        movieGet = ia.get_movie(movieFind[0].movieID)
        print(movieGet)
        print(movieGet['genres'][0])
        listFilesAfter[indexGil] = movieGet['genres'][0]
    # print("~~~~~~~~~~~~~~~ EO STEP 3 ~~~~~~~~~~~~~~~~~~~~~~~~")


def get_dirToMove(genre):
    if(genre == "Action"):
        pathToMove="Sunday"
    elif(genre == "Adventure"):
        pathToMove="Monday"
    elif(genre == "Animation"):
        pathToMove="Tuesday"
    elif(genre == "Biography"):
        pathToMove="Wednesday"
    elif(genre == "Comedy"):
        pathToMove="Thursday"
    elif(genre == "Crime"):
        pathToMove="Friday"
    elif(genre == "Documentary"):
        pathToMove="Saturday"
    elif(genre == "Drama"):
        pathToMove="Monday"
    elif(genre == "Family"):
        pathToMove="Tuesday"
    elif(genre == "Fantasy"):
        pathToMove="Wednesday"
    elif(genre == "Film Noir"):
        pathToMove="Thursday"
    elif(genre == "History"):
        pathToMove="Friday"
    elif(genre == "Horror"):
        pathToMove="Saturday"
    elif(genre == "Music"):
        pathToMove="Monday"
    elif(genre == "Musical"):
        pathToMove="Tuesday"
    elif(genre == "Mystery"):
        pathToMove="Wednesday"
    elif(genre == "Romance"):
        pathToMove="Thursday"
    elif(genre == "Sci-Fi"):
        pathToMove="Friday"
    elif(genre == "Short Film"):
        pathToMove="Saturday"
    elif(genre == "Sport"):
        pathToMove="Monday"
    elif(genre == "Superhero"):
        pathToMove="Tuesday"
    elif(genre == "Thriller"):
        pathToMove="Wednesday"
    elif(genre == "War"):
        pathToMove="Thursday"
    elif(genre == "Western"):
        pathToMove="Friday"
    else:
        pathToMove="."
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
            datzETr(listFilesAfter[indexFile], indexFile)
            test = get_dirToMove(listFilesAfter[indexFile])
            print("test vaut : " + test );

            # Une fois le type de Film recupere on deplace le fichier correspondant dans le bon dossier
            if os.path.exists((os.path.abspath(variaREP) + '/' + listFilesBefore[indexFile]).strip()) == 0:
                print("on passe ici ")
                if listFilesAfter[indexFile] != listFilesBefore[indexFile]:



                    #os.rename(os.path.abspath(variaREP) + '/' + file, os.path.abspath(variaREP) + '/' + listFilesAfter[indexFile])
                    indexFileMove = indexFileMove + 1
            indexFile = indexFile + 1

    print ("spreadren0 Statement :  Finished : ", indexFileMove, " spreaded Files  / ", indexFile, " Files")
    print ("--()--")

mainFunc()



#Todo : Si le fichier est trouve mais qu'il a un titre original il faudrait prendre ce titre
