import json


def open_json(file):
    with open('user_config.json') as mon_fichier:
        user_config = json.load(mon_fichier)
    return(user_config) 

def open_diagram(file):
    diagram=[]
    try:
        file = open(file, "r")
        line = file.readline()
        diagram.append(line)

        while line:
            print(line)
            line = file.readline()
            diagram.append(line)
        
        file.close()
        return(diagram)
    except:
         print("Oops! file not found:the value ",file," is incorrect in the user_config.json")
    

def Write_in_the_file(file,comment):
    user_config=open_json(file)
    diagram=open_diagram(user_config["diagram_choice"])
    

