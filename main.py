import sys

if len(sys.argv) !=2 :
    print("Argument non conforme.")
    print("Exemple: ./ALX-Header.sh file_name")
else:
    file=sys.argv[1]
    print(file)