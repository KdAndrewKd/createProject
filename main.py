#!/usr/bin/python3.11
import os
from datetime import datetime


def translator(name):

    dic = {'Ь':'', 'ь':'', 'Ъ':'', 'ъ':'', 'А':'A', 'а':'a', 'Б':'B', 'б':'b', 'В':'V', 'в':'v',
        'Г':'G', 'г':'g', 'Д':'D', 'д':'d', 'Е':'E', 'е':'e', 'Ё':'E', 'ё':'e', 'Ж':'Zh', 'ж':'zh',
        'З':'Z', 'з':'z', 'И':'I', 'и':'i', 'Й':'I', 'й':'i', 'К':'K', 'к':'k', 'Л':'L', 'л':'l',
        'М':'M', 'м':'m', 'Н':'N', 'н':'n', 'О':'O', 'о':'o', 'П':'P', 'п':'p', 'Р':'R', 'р':'r', 
        'С':'S', 'с':'s', 'Т':'T', 'т':'t', 'У':'U', 'у':'u', 'Ф':'F', 'ф':'f', 'Х':'Kh', 'х':'kh',
        'Ц':'Tc', 'ц':'tc', 'Ч':'Ch', 'ч':'ch', 'Ш':'Sh', 'ш':'sh', 'Щ':'Shch', 'щ':'shch', 'Ы':'Y',
        'ы':'y', 'Э':'E', 'э':'e', 'Ю':'Iu', 'ю':'iu', 'Я':'Ia', 'я':'ia'}
        
    alphabet = ['Ь', 'ь', 'Ъ', 'ъ', 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё',
                'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
                'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч',
                'Ш', 'ш', 'Щ', 'щ', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']


    if name == "exit":
        exit()
    result = str()
    
    len_st = len(name)
    for i in range(0,len_st):
        if name[i] in alphabet:
            simb = dic[name[i]]
        else:
            simb = name[i]
        result = result + simb
    
    return result.replace(" ", "_")



nameFolder = input("Enter name progect: ")
nameFolder = translator(nameFolder)


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

            # elif nameFile == "main.py":
            #     contentFile="# source venv/bin/activate"

            elif nameFile == "info.txt":
                curentTime = datetime.now()
                curentTime = str(curentTime).split(".")
                contentFile=f"{curentTime[0]} - Start progect"

            createFile.write(contentFile)

    print(f"Project {nameFolder} was created.")

    # /usr/share/code/code --unity-launch %F
    os.system(f'/usr/share/code/code {nameFolder}')


    exit()
