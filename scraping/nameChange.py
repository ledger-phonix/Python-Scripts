import os
files = os.listdir('pics')
i = 1
for file in files:   
    if file.endswith('.jpg'):
        print(file)
        os.rename(f'pics/{file}',f'pics/pexel{i}.jpg')
        i = i + 1



