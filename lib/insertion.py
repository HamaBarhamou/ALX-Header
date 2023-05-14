import imp
import json
from datetime import datetime
#from lib.updateHeader import Update_Header
#from lib.newHeader import New_Header

MATRICE_LENGTH=77
MATRICE_WIDTH=11
FILENAME_X=3
FILENAME_Y=2
AUTHOR_X=5
AUTHOR_Y=6
CREATEDAT_X=7
CREATEDAT_Y=11
CREATEDBY_X=CREATEDAT_X
CREATEDBY_Y=34
UPDATEDAT_X=8
UPDATEDAT_Y=CREATEDAT_Y
UPDATEDBY_X=UPDATEDAT_X
UPDATEDBY_Y=CREATEDBY_Y

def New_Header(file,data,x,y):
    # your code 
    file_data=open_diagram(file)
    fichier = open(file, "w")
    for i in range(x):
        for j in range(y):
            fichier.write(data[i][j])
        fichier.write("\n")
    for x in range(len(file_data)):
        ligne=file_data[x]
        for loop in range(len(ligne)):
            fichier.write(ligne[loop])
    fichier.close()
    pass

def affiche(matrice):
    for x in range(MATRICE_WIDTH):
        for y in range(MATRICE_LENGTH):
            print(matrice[x][y],end="")
        print("")

def open_json(file):
    with open(file) as mon_fichier:
        user_config = json.load(mon_fichier)
    return(user_config) 

def open_diagram(file):
    diagram=[]
    try:
        file = open(file, "r")
        line = file.readline()
        line=list(line)
        diagram.append(line)

        while line:
            #print(line)
            line = file.readline()
            line=list(line)
            diagram.append(line)
        
        file.close()
        return(diagram)
    except:
         print("Oops! file not found:the value ",file," is incorrect in the user_config.json")
    
def Replaces(matrice,x,y,chaine):
    for loop in range(len(chaine)):
        matrice[x][y+loop]=chaine[loop]
    i=len(chaine)
    while(matrice[x][y+i]!=" "):
        matrice[x][y+i]=" "
        i=i+1
    return(matrice)

def open_MATRICE_WIDTH_diagram(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines[:MATRICE_WIDTH]]


def Existe_Header(file):
    user_config=open_json('user_config.json')
    user_name=user_config["user_name"]
    data = open_MATRICE_WIDTH_diagram(file)
    if len(data) < MATRICE_WIDTH:
        return False
    elif (len(data[0])-2) != MATRICE_LENGTH:
        return False
    elif file not in data[FILENAME_X][FILENAME_Y:MATRICE_LENGTH-2]:
        return False
    elif user_name not in data[AUTHOR_X][AUTHOR_Y:MATRICE_LENGTH-2]:
        return False
    elif "Created" in data[CREATEDBY_X][CREATEDBY_Y:MATRICE_LENGTH-2]:
        return False
    elif "Updated" in data[UPDATEDBY_X][UPDATEDBY_Y:MATRICE_LENGTH-2]:
        return False
    elif "Created" in data[CREATEDAT_X][CREATEDAT_Y:MATRICE_LENGTH-2]:
        return False
    elif "Updated" in data[UPDATEDAT_X][UPDATEDAT_Y:MATRICE_LENGTH-2]:
        return False
    return True


def Update_Header(file, user_name, user_email):
    data = open_diagram(file)
    create_date = data[CREATEDAT_X][CREATEDAT_Y:]
    updated_date = str(datetime.now())[:19]
    updated_by = f"{user_name}<{user_email}>"
    # Mettre à jour les informations de l'entête
    data[AUTHOR_X][AUTHOR_Y:AUTHOR_Y+len(user_name)] = user_name
    data[AUTHOR_X][AUTHOR_Y+len(user_name)+3:AUTHOR_Y+len(user_name)+3+len(user_email)] = user_email
    data[UPDATEDAT_X][UPDATEDAT_Y:] = updated_date
    data[UPDATEDBY_X][UPDATEDBY_Y:] = updated_by
    # Écrire les données mises à jour dans le fichier
    with open(file, 'w') as f:
        for row in data:
            f.write(''.join(row))


def Write_in_the_file(file,comment):
    user_config=open_json('user_config.json')
    diagram=open_diagram(user_config["diagram_choice"])
    user_name=user_config["user_name"]
    user_email='<'+user_config["user_email"]+'>'
    create_date=str(datetime.now())
    create_date=create_date[:19]
    diagram=Replaces(diagram,FILENAME_X,FILENAME_Y,file)
    diagram=Replaces(diagram,AUTHOR_X,AUTHOR_Y,user_name)
    diagram=Replaces(diagram,AUTHOR_X,AUTHOR_Y+len(user_name)+3,user_email)
    diagram=Replaces(diagram,CREATEDBY_X,CREATEDBY_Y,user_name)
    diagram=Replaces(diagram,UPDATEDBY_X,UPDATEDBY_Y,user_name)
    diagram=Replaces(diagram,CREATEDAT_X,CREATEDAT_Y,create_date)
    diagram=Replaces(diagram,UPDATEDAT_X,UPDATEDAT_Y,create_date)
   
    for loop in range(MATRICE_WIDTH):
        diagram[loop][0]=comment[0]
        diagram[loop][MATRICE_LENGTH-1]=comment[1]
    
    rep = Existe_Header(file)
    if(rep == True):
        #Update_Header(file, user_name, user_email)
        pass
    else:
        New_Header(file,diagram,MATRICE_WIDTH,MATRICE_LENGTH)
        
        