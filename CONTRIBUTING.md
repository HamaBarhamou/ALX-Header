# <center>Open source project made by a beginner for beginners</center>

# Contribute to ALX-Header

:+1::tada: First of all, thank you for taking the time to contribute to ALX-Header! :tada::+1 : </br>
If you want to start with open source, this project is for you.


## General Guidelines

This page explains at a very low level how to contribute to ALX-Header. 
Make sure you know [Working with remote repositories] (https://git-scm.com/book/fr/v2/Les-bases-de-Git-Travailler-avec-des-d%C3%A9p%C3%B4ts-distants).

## Submit a useful issue

Submitting useful, effective and relevant problem reports can help improve ALX-Header for everyone.

Add to these report submissions error/traceback messages and requested environment/dependency information, be sure to include a detailed step-by-step description of what triggered the problem. Otherwise, we probably won't be able to find and fix it, and your issue will have to be closed after a week (7 days). Thank you!


## Setting up a development environment

### Forking and cloning the repo

First, navigate to the [ALX-Header](https://github.com/HamaBarhamou/ALX-Header) in your web browser and press the "Fork" button to make a personal copy of the repository on your own Github account.
Then, click the "Clone or Download" button on your repository, copy the link and run the following on the command line to clone the repository:

```bash
$ git clone <LINK-TO-YOUR-REPO>
```

Finally, set the upstream remote to the official ALX-Header repository with:

```bash
$ git remote add upstream https://github.com/HamaBarhamou/ALX-Header
```
[Read more here ](https://www.neonscience.org/resources/learning-hub/tutorials/git-setup-remote)

### Run ALX-Header

To run ALX-Header directly from your clone
```bash
$ cd ALX-Header
$ ./ALX-Header.sh file_name.sh # file_name.c or file_name.py ....

```

## Internal organization of code lines

**lib:** Is a python library. It is in this folder that we will define all the functions we will need.</br></br>
**ALX-Header.sh:** Is the entry point of the program. This bash script takes a **file** as argument and executes in the linux environment the python script **main.py** passing it the **file** as argument. </br></br>

**main.py:** Is the entry point to the python code. It just tramsmit the argument `file` recover to function `file_type` of the library **lib** in the file **fileType.py**</br></br>

`file_type`: This function determines at first the programming language of **fichier** and then call the function `Write_in_the_file(file,comment)` the programming language is supported by the project. </br></br>

`Write_in_the_file(file,comment)`: is a function in the file insertion.py. It takes as parameters two arguments, the file: `file` et `comment`: a two-dimensional array that contains the characters for commenting in the file. It loads in memory the user_config.json file and the diagram of your choice (the diagram_ALX file is loaded by default) respectively in the `user_config` and `diagram`.

**the writing of this document is in progress...**