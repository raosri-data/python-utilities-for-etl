import os, shutil
def organize(path):
    for f in os.listdir(path):
        ext=f.split('.')[-1]
        folder=os.path.join(path, ext)
        os.makedirs(folder, exist_ok=True)
        shutil.move(os.path.join(path,f), os.path.join(folder,f))

# usage commented to avoid unintended moves
# organize('/path/to/dir')
