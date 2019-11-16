from os import walk
import os
f = []
i = 1
for (dirpath, dirnames, filenames) in walk("trainparent"):
    for dirs in dirnames:
    	os.rename("trainparent"+os.sep+str(dirs), "trainparent"+os.sep+str(i))
    i = i + 1
    break