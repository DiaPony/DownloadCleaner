import os
import shutil

downloads_path = 'C:/Users/fe199/Downloads'

dest_dirs ={
    'Bilder': 'C:/Aufräumer/Bilder',
    'Dokumente': 'C:/Aufräumer/Dokumente',
    'Videos' : 'C:/Aufräumer/Videos',
    'Rest' : 'C:/Aufräumer/Rest'
}

file_types = {
    'Bilder': {'.jpg', '.png'},
    'Dokumente': ['.pdf', '.docx'],
    'Videos': ['.mp4', '.mov']
}

for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    if os.path.isfile(file_path):
        _, file_extension = os.path.splitext(filename)
        moved = False
        for type, extensions in file_types.items():
            if file_extension in extensions:
                dest_path = os.path.join(dest_dirs[type], filename)
                shutil.move(file_path, dest_path)
                print(f'Verschoben: {filename} -> {dest_dirs[type]}')
                moved = True
                break
        if not moved:
            dest_path = os.path.join(dest_dirs['Rest'], filename)
            shutil.move(file_path, dest_path)
            print(f'Verschoben: {filename} -> {dest_dirs["Rest"]}')

print('Fertig mit dem Verschieben von Dateien.')