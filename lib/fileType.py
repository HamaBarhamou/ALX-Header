from re import L
from lib.language import what_language
from lib.delimiters import languageDemiliters

def file_type(file):
    #determine the type of file
    file_decom=file.split('.')
    if(len(file_decom)!=2):
        print("unsupported format")
        quit()
    ext=file_decom[1]
    #print(what_language(ext))
    comment=languageDemiliters[what_language(ext)]
    #Write_in_the_file(file,comment)
    

    
