import os


def readAllFiles(path):
    d = os.listdir(path)
    files = []
    for f in d:
        files.append(path + f)
    return files


def readFile(file):
    f = open(file, "r", encoding='utf-8')
    content = f.read().split('\n')
    return content[0],  content[1]


def readDataFile(name):
    f = open("input-files/" + name, "r")
    content = f.read().split('\n')
    return content[0], content[1]
