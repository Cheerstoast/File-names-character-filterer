import glob
import os

# Get valid directory
while 1:
  inputdirectory = input('Enter folder directory: ')
  if os.path.isdir(inputdirectory):
    if inputdirectory[-1] == '/':
      inputdirectory = inputdirectory[:-1]
    break
  else:
    print('\nSorry, that is not a valid directory.\n')
# Directories list contains directories of all files and subfolders within the specified folder.
# These could contain chinese characters.
directories = glob.glob(inputdirectory.split('/')[-1] + '/**',recursive = True)
input = []
output = []
for directory in directories:
  if os.path.isfile(directory):
    input.append(directory)
    toappend = ""
    for ch in directory:
      if ch.isascii():
        toappend = toappend + ch
    output.append(toappend)
# Rename all files and folders recursively
# try:
for i in input:
  os.renames(i, output[input.index(i)])
# except:
#   input("\e[0;32mError: one or more files or folders doesn't contain any non-chinese characters. Abort.")
print('\033[H\033[J\001\033[0;92m\002Success!\n\001\033[0m\002')
