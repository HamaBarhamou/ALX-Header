from re import L
from lib.language import what_language
from lib.delimiters import languageDemiliters
from lib.insertion import Write_in_the_file

def file_type(file):
    #determine the type of file
    file_decom=file.split('.')
    if(len(file_decom)!=2):
        print("unsupported format")
        quit()
    ext=file_decom[1]
    #print(what_language(ext))
    key=what_language(ext)
    if(key in languageDemiliters):
        comment=languageDemiliters[key]
        Write_in_the_file(file,comment)
    else:
        print("language not supported")
    
        
    
    
    

    
