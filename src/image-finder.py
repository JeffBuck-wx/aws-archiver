#!/usr/bin/env python
import os


SEARCH_DIRS = ['Pictures', 'Desktop', 'Downloads']\
IMAGE_EXT_PATTERN = "([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)"

def main():
    user = 'jbuck'
    userDir = os.path.join('C:\\', 'Users', user)
    print(userDir)    

    for i in os.listdir(userDir):
        thisPath = os.path.join(userDir, i)
        if os.path.isdir(thisPath) and i in SEARCH_DIRS:
            # dir to search for images
            pass


if __name__ == '__main__':
    main()
