from os import listdir
from os.path import isfile, join, splitext
files = [f for f in listdir("./") if isfile(join("./", f))]

themes= [] #list the themes 
for file in files:
    split_file = splitext(file)
    if split_file[1] == '.json':
        themes.append(split_file[0])
