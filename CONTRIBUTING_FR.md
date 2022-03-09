# Projet open source fait par un débutant pour les debutants

Si vous desirer debuter dans l'open source, se projet est fait pour vous. 

Comment contribuer ?

## 1 Pour commencer

commencer a fait fork du projet et ensuite cloner votre fork dans votre git locale.
ajouter le depot du projet comme depot distant dans votre projet en locale. 
A chaque fois que vous vouler apporter des modification assurer vous d'obtenir les dernier mise a jour du depot original avant de continuer vos modification.
Apres avoir finit votre contribution et pousser votre travail sur la version fork du projet dans votre referentielle git, fait un pull request pour pousser faire une demande d'extraction de votre contribution.

## Les point de contribution

### Communauté

- Repondre au questions des questions des nouveaux utilisateur 

### ESTHETIQUE
- Correction de faute d'orthographe 
- prosition d'une meilleur redaction fichier ![README.md]
- proposition d'une meilleur redaction du fichier ![CONTRIBUTING.md]

### LE CODE

**lib:** Est une un bibliotheque python. C'est dans ce dossier que nous allons definir tout les fonction dont nous aurons besoins.</br></br>

**ALX-Header.sh:** Est le point d'entrée du programme. Ce script bash prend un **fichier** comme argument et execute dans l'environement linux le script python **main.py**  en lui passant le **fichier** comme argument. </br></br>

**main.py:** Est le point d'entrée au code python. Il se contente de tramsmettre l'argument **file** recuperer a la fonction  **file_type** de la bibliotheque **lib** dans le fichier **fileType.py**</br></br>

**file_type:** Cette fonction determine en un premiers temps le language de programmation de **fichier** et ensuite appelle la fonction **Write_in_the_file(file,comment)** le language de programmtion est prix en charge par le projet. </br></br>

