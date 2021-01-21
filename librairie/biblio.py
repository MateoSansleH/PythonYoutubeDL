from ping3 import ping, verbose_ping
import moviepy.editor
import os

def bonjour():
    print("#####################################")
    print("#  Python Youtube Downloader V.1.2  #")
    print("#  by Mateo DUCHÊNE - 01.01.2021    #")
    print("#####################################")

def internetconnection(host):
    test_ping = ping(host)
    if test_ping == None or test_ping == False:
        print("Erreur : Ping non resolu veuillez verifier votre connexion internet ...")
        return 1
    else:
        print("ping ... "+ host +" : " + str(test_ping) + " ms")
        print("Check ... internet connection OK!")
        return 0


#####################################################
# - Remplace les espace d'une chaine par des plus - #
#####################################################
def spacetoplus(var):
    rslt = ""
    i = 0
    while i < len(var):
        a = var[i]
        if var[i] == " ":
            a = "+"
        rslt = rslt + a
        i = i + 1
    return rslt

def replacespace(var, remplace):
    rslt = ""
    i = 0
    while i < len(var):
        a = var[i]
        if var[i] == " ":
            a = remplace
        rslt = rslt + a
        i = i + 1
    return rslt

#####################################################
# - Fonction renvoyant: 0, 1 , 2                    #
#   prend une chaine en entrée                      #
#   0 = Non                                         #
#   1 = Oui                                         #
#   2 = erreur -> ni oui ni non                     #
#####################################################
def ouiounon(var):
    liste_oui = ["OUI", "Oui", "oui", "O", "o", "YES", "Yes", "yes", "Y", "y", "1"]
    liste_non = ["NON", "Non", "non", "N", "n", "NO", "No", "no", "0"]
    flag_oui = 0
    flag_non = 0

    for i in liste_oui:
        if i == var:
            flag_oui = 1

    for i in liste_non:
        if i == var:
            flag_non = 1

    if flag_oui == 1 and flag_non == 0:
        rslt = 1
    elif flag_oui == 0 and flag_non == 1:
        rslt = 0
    else :
        rslt = 2
        
    return rslt

##########################################################################################
#  fonction qui permet de stopper une boucle                                             #
#  a la demande de l'arret du programme et converti une demande en oui ou non en 1 ou 0  #
##########################################################################################
def quitprgm():
    erreur = 1
    while erreur != 0:
        print("Voulez-vous quitter le programme ?")
        choix = input(">>> ")
        rslt = ouiounon(choix)
        if rslt == 0 or rslt == 1:
            erreur = 0 
        elif rslt == 2:
            print("error : wrong command")
        else:
            print("ERREUR !!!")
    return rslt 

def demande():
    rslt = input(">>> ")
    return rslt

def choixde1a5():
    error = 0
    liste_choix = ["0", "1", "2", "3", "4", "5",]
    flag_exist = 0
    while error == 0:
        var = demande()
        for i in liste_choix:
            if var == i:
             flag_exist = 1
        if flag_exist == 1:
            error = 1
        else:
            error = 0
            print("Erreur : Veilllez entre un nombre entre 1 et 5")
    return (int(var) - 1)

def splitaudiovideo(cheminsource, cheminsortie):
    video = moviepy.editor.VideoFileClip(str(cheminsource))
    audio = video.audio
    audio.write_audiofile(str(cheminsortie))
    audio.close()
    video.close()
    os.system("del output\\tmp /q")

def cleantitle(titre):
    liste_terme = ["/", "#", '"', "'",]
    rslt = ""
    flag = 0
    for i in titre:
        for y in liste_terme:
            if i == y:
                flag = 1
        if flag == 1 :
            rslt = rslt + ""
            flag = 0
        else:
            rslt = rslt + i
    return rslt
