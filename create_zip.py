import zipfile
import os

def create_test_zip(zip_path):
    base_dir = "test_dir"
    os.makedirs(os.path.join(base_dir, "home", "user"), exist_ok=True)
    
    # Create files in the directory
    with open(os.path.join(base_dir, "home", "user", "file1.txt"), 'w') as f:
        f.write("Content of file1.txt")
        
    with open(os.path.join(base_dir, "home", "user", "file2.txt"), 'w') as f:
        f.write("Content of file2.txt")
    
    # Create a zip file
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Add the file to the zip, preserving directory structure
                arcname = os.path.relpath(file_path, start=base_dir)
                zipf.write(file_path, arcname=arcname)

if __name__ == "__main__":
    create_test_zip("vfs.zip")
