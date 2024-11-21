import os
import zipfile
import tempfile

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.mount_point = self.temp_dir.name 
        self._extract_zip(zip_path)
    
    def _extract_zip(self, zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(self.mount_point)

    def list_dir(self, current_dir):
        current_dir = current_dir.lstrip("/")
        path = os.path.join(self.mount_point, current_dir) 
        
        if os.path.isdir(path):
            return os.listdir(path)
        else:
            raise NotADirectoryError(f"{path} is not a directory")

    def read_file(self, file_path):
        # Преобразуем путь в абсолютный относительно mount_point
        absolute_path = os.path.normpath(os.path.join(self.mount_point, file_path))
        if os.path.isfile(absolute_path):
            with open(absolute_path, 'r') as file:
                return file.read()
        elif os.path.isdir(absolute_path):
            raise IsADirectoryError(f"'{file_path}' является директорией.")
        else:
            raise FileNotFoundError(f"Файл '{file_path}' не найден.")


    def change_dir(self, current_dir, new_dir):
        current_dir = current_dir.lstrip("/")
        new_dir = new_dir.lstrip("/")
        new_path = os.path.normpath(os.path.join(self.mount_point, current_dir, new_dir))
        if os.path.isdir(new_path):
            return os.path.relpath(new_path, self.mount_point)
        else:
            raise FileNotFoundError(f"Directory {new_dir} not found")

