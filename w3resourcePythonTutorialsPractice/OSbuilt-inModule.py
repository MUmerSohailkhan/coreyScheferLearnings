import os


# getting current working directory
a=os.getcwd()
print(a)
#-----------------------------------


#creating new directory at given path
foldername='songs'
pathAndFolderName=a+f'\\{foldername}'
# print(newPathFolder)
os.mkdir(pathAndFolderName)
#-----------------------------------


#changing the current working directory
os.chdir(pathAndFolderName)
print(os.getcwd())
#------------------------------------

#changing the current working directory
os.chdir('..')
os.chdir('..')
os.chdir('..')
print(os.getcwd())
#--------------------------------------

#removing directory
os.rmdir(pathAndFolderName)
#--------------------------------------

# listing all files in w3resource
print(os.listdir(a))



