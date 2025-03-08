import os
import shutil

source_directory = r"C:\Users\User\Desktop\BSIT3RD"

categories = {
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.html','.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Audio': ['.mp3', '.wav', '.aac'],
}

for category in categories:
    category_path = os.path.join(source_directory, category)
    os.makedirs(category_path, exist_ok=True)

def sort_files():
    file_moved = False  
    for file in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file)

        if os.path.isfile(file_path):  
            moved = False
            for category, extensions in categories.items():
                if file.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(source_directory, category, file))
                    print(f"Moved: {file} --> {category}")
                    moved = True
                    file_moved = True
                    break

            if not moved:  
                misc_folder = os.path.join(source_directory, 'Miscellaneous')
                os.makedirs(misc_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(misc_folder, file))
                print(f"Moved: {file} --> Miscellaneous")
                file_moved = True

    if file_moved:
        print("\nFile organization completed successfully!")
    else:
        print("\nNo files found to organize.")

if __name__ == "__main__":
    sort_files()
