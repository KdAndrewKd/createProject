import os
from datetime import datetime

while True:

    nameFolder = input("Enter name progect: ")

    if os.path.exists(nameFolder):
        print("Folder exist. Enter ather name.") 
    else:
        os.mkdir(nameFolder) 
        os.system(f'python -m venv {nameFolder}/venv')
        
        listFiles = ("README.txt", ".gitignore", "help.txt", "info.txt", "main.py")

        for nameFile in listFiles:
            contentFile = ""
            with open(f'{nameFolder}/{nameFile}', "w", encoding="utf-8")as createFile:

                if nameFile == ".gitignore":
                    contentFile="/venv/ \n.idea \n.vscode"

                elif nameFile == "main.py":
                    contentFile="# source venv/bin/activate"

                elif nameFile == "info.txt":
                    curentTime = datetime.now()
                    curentTime = str(curentTime).split(".")
                    contentFile=f"{curentTime[0]} - Start progect"

                createFile.write(contentFile)

        print(f"Project {nameFolder} was created.")
        
        exit()
