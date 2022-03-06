import sys
from lib.fileType import file_type

#from fileType import file_type
if len(sys.argv) !=2 :
    print("Non-conforming argument.")
    print("Exemple: ./ALX-Header.sh file_path")
else:
    file=sys.argv[1]
    file_type(file)
