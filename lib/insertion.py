import json
from datetime import datetime

MATRICE_LENGTH=80
MATRICE_WIDTH=11
FILENAME_X=3
FILENAME_Y=5
AUTHOR_X=5
AUTHOR_Y=9
CREATEDAT_X=7
CREATEDAT_Y=14
CREATEDBY_X=CREATEDAT_X
CREATEDBY_Y=37
UPDATEDAT_X=8
UPDATEDAT_Y=CREATEDAT_Y
UPDATEDBY_X=UPDATEDAT_X
UPDATEDBY_Y=CREATEDBY_Y

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

def Existe_Header(file):
    data=open_diagram(file)
    print(len(data))
    print(MATRICE_WIDTH)
    if(len(data)<MATRICE_WIDTH):
        return 0
    else:
        if(len(data[MATRICE_WIDTH-1])!=len(data[0])):
            return 0
            
        print(data[MATRICE_WIDTH-1])

def Update_Header(file):
    pass

def New_Header(file):
    pass

def Write_in_the_file(file,comment):
    user_config=open_json('user_config.json')
    diagram=open_diagram(user_config["diagram_choice"])
    #replace the user information in the matrix
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
    
    if(len(comment[0])==1):
        for loop in range(MATRICE_WIDTH):
            diagram[loop][0]=comment[0]
            diagram[loop][MATRICE_LENGTH-1]=comment[1]
    else:
        pass
    
    affiche(diagram)
    
    if(Existe_Header(file)):
        Update_Header(file)
    else:
        New_Header(file)
        