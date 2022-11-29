import os
import sys
import shutil
import getpass
import platform
import json
import asyncio


def isLinux() -> bool:
    try:
        platform.linux_distribution()
        return True
    except:
        return False


def getFromAndToDirs():
    if not isLinux():
        if len(sys.argv) > 1:
            toDir = sys.argv[1]
            if len(sys.argv) > 2:
                fromDir = sys.argv[2]
            else:
                inp = input(
                    "Enter a directory to organize files to (leave empty for downloads folder): ")
                fromDir = f"C:\\Users\\{getpass.getuser()}\\Downloads"

            if toDir == "" or fromDir == "":
                fromDir, toDir = getFromAndToDirs()
        else:
            inp = input(
                "Enter a directory to get files from (leave empty for downloads folder): ")
            if inp == "":
                toDir = f"C:\\Users\\{getpass.getuser()}\\Downloads"
            inp = input(
                "Enter a directory to organize files to (leave empty for downloads folder): ")
            if inp == "":
                fromDir = f"C:\\Users\\{getpass.getuser()}\\Downloads"

            if toDir == "" or fromDir == "":
                fromDir, toDir = getFromAndToDirs()
    else:
        if len(sys.argv) > 1:
            toDir = sys.argv[1]
            if len(sys.argv) > 2:
                fromDir = sys.argv[2]
            else:
                inp = input(
                    "Enter a directory to organize files to: ")
                fromDir = f"C:\\Users\\{getpass.getuser()}\\Downloads"

            if toDir == "" or fromDir == "":
                fromDir, toDir = getFromAndToDirs()
        else:
            inp = input("Enter a directory to get files from: ")
            toDir = f"C:\\Users\\{getpass.getuser()}\\Downloads"
            inp = input("Enter a directory to organize files to: ")
            fromDir = f"C:\\Users\\{getpass.getuser()}\\Downloads"

            if toDir == "" or fromDir == "":
                fromDir, toDir = getFromAndToDirs()

    return fromDir, toDir


async def sort(filePath, sortKey, fromDir, toDir):
    fileName, ext = os.path.splitext(filePath)
    if ext != "":
        for fol in sortKey:
            if ext.lower() in [i.lower() for i in sortKey[fol]]:
                if not os.path.exists(os.path.join(fromDir, fol)):
                    os.mkdir(os.path.join(fromDir, fol))

                print(filePath)
                shutil.move(os.path.join(fromDir, filePath),
                            os.path.join(toDir, fol, filePath))


fromDir, toDir = getFromAndToDirs()

files = [i for i in os.listdir(fromDir) if i != "desktop.ini"]

sortKey = json.load(open("./config.json", "rb"))

asyncio.run(sort(files[0], sortKey, fromDir, toDir))
for file in files:
    fileName, ext = os.path.splitext(file)
