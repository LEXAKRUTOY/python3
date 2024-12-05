import os
from datetime import datetime

def file_stats(filepath):
    if not os.path.isfile(filepath):
        with open("example.txt", "w") as txt:
            txt.write("Hello_World!")
            return txt
    
    file = {
        "Размер файла: " : os.stat(filepath).st_size,
        "Последнее изменение: " : datetime.fromtimestamp(os.path.getmtime(filepath)).strftime("%m/%d/%y %H:%M:%S"),
        "Имя файла" : os.path.splitext(filepath)[0],
        "Расширение" : os.path.splitext(filepath)[1]
    }
    return file
print(file_stats("example.txt"))