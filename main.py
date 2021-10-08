
import os
import shutil

if not os.path.isdir('exefile'):
    try:
        os.mkdir("exefile")
    except OSError as error:
        print(error)
else:
    pass

for filename in os.listdir():
    f_name, f_ext = os.path.splitext(filename)
    if f_name == 'main': 
        pass
    elif f_ext == ".exe":
        shutil.move(os.path.join(os.getcwd(), filename), os.path.join(os.getcwd(), "exefile", filename))

    else:
        pass
