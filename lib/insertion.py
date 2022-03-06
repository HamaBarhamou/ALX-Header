import json

def Write_in_the_file(file,comment):
    #load user_confi.json file and diagram in memory
    with open('user_config.json') as mon_fichier:
        user_config = json.load(mon_fichier)

    #print(user_config["user_name"])
    