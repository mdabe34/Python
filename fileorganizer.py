import os
import shutil

def organize_files():

    base_dir = "MyFiles"
    docs_dir = os.path.join(base_dir, "Docs")
    images_dir = os.path.join(base_dir, "Images")
    videos_dir = os.path.join(base_dir, "Videos")

    try: 
        os.mkdir(base_dir)
        os.mkdir(docs_dir)
        os.mkdir(images_dir)
        os.mkdir(videos_dir)
        print("Directories created successfully!")
    except FileExistsError:
        print("Directories already exist.")

   
    file_mappings = {
        ".txt": docs_dir,
        ".jpg": images_dir,
        ".mp4": videos_dir
    }

    for filename in os.listdir():
        if os.path.isfile(filename):  # Check if it's a file
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in file_mappings:
                dest_dir = file_mappings[file_ext]
                try:
                    shutil.move(filename, dest_dir)
                    print(f"Moved '{filename}' to '{dest_dir}'")
                except shutil.Error:
                    print(f"Error moving '{filename}'")

if __name__ == "__main__":
    organize_files()
