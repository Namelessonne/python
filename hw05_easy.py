# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil

folders = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']
for folder in folders:
    os.mkdir(folder)

folders = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']
for folder in folders:
    os.rmdir(folder)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for root, dirs, files in os.walk(os.getcwd()):
    print(list(dirs))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

shutil.copy(__file__, __file__ +".dup1")
