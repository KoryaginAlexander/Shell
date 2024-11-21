def ls(fs, shell_gui, current_dir):
    try:
        files = fs.list_dir(current_dir)
        
        if not files:
            shell_gui.display_output("Директория пуста.")
            return

        for file in files:
            shell_gui.display_output(file)
            
    
    except FileNotFoundError:
        shell_gui.display_output(f"Ошибка: Директория '{current_dir}' не найдена.")
    except NotADirectoryError:
        shell_gui.display_output(f"Ошибка: '{current_dir}' не является директорией.")
    except Exception as e:
        shell_gui.display_output(f"Ошибка: {e}")
