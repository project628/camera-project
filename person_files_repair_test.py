import os

labels_path = r'C:\Users\eeproj\Desktop\Project\train_part_person_extra\labels'

for filename in os.listdir(labels_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(labels_path, filename)

        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                parts = line.split()
                if int(parts[0]) != 1:
                    parts[0] = '1'
                file.write(' '.join(parts) + '\n')
