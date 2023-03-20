from os import listdir
import os
from os.path import isfile, join, splitext
import shutil
files = [f for f in listdir("./") if isfile(join("./", f))]

themes= [] #list the themes 
for file in files:
    split_file = splitext(file)
    if split_file[1] == '.json':
        themes.append(split_file[0])


#get rid of bl themes
for theme in themes:
    if theme.find("bl") != -1:
        index = themes.index(theme)
        themes.pop(index)

print(themes)
#set up building
try:
    os.mkdir("build")
except:
    print()
os.chdir("build")
os.system("git clone --recursive https://github.com/UpsilonNumworks/Upsilon.git")
os.chdir("Upsilon")
os.system("git checkout upsilon-dev") #building the dev branch as we are crazy


for theme in themes:
    print(f"building theme: {theme}")
    os.system("make cleanall")
    os.system(f"make PLATFORM=simulator THEME_NAME={theme} THEME_REPO=https://github.com/hugo-b-r/Upsilon-Themes.git -j8 > ../{theme}_log.txt")
    shutil.move('./output/release/simulator/linux/epsilon.bin', f'../{theme}.bin')
