import os
import shutil

# print(os.getcwd())
# print(os.listdir())

# with open('output.txt', 'w') as f:
#     f.write("Sample text file")


# shutil.move('output.txt', '../exceptionHandling/')

for folder, subfolder, files in os.walk(os.getcwd()):
    print(f'Currently looking at {folder}' )
    print("\n")
    print("Sub folders are: ")
    for sub_fold in subfolder:
        print(f'Subfolder: {sub_fold}')

    print("\n")
    print("the files are :")
    for f in files:
        print(f)