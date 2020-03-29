import os

path = os.getcwd()

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' or '.jpeg' in file:
            files.append(file)

for f in files:
    print(f)