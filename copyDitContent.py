from distutils.dir_util import copy_tree

#Created by Omri Ziner
#24/12/2020
# copy subdirectory example

fromDirectory = "/tmp/CONTENT/"
toDirectory = "/tmp/RAWDATA/"

copy_tree(fromDirectory, toDirectory)
