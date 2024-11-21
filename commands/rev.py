import os
def rev(fs, shell_gui, shell, args):
    if not args:
        shell_gui.display_output("Укажите файл для реверсирования.")
        return

    file_path = args[0]
    normalized_file_path = os.path.normpath(file_path)

    try:
        # Получаем полный путь к файлу относительно текущей директории
        full_path = os.path.join(shell.current_dir, normalized_file_path)
        file_content = fs.read_file(full_path)
        
        # Реверсируем каждую строку
        reversed_content = "\n".join(line[::-1] for line in file_content.splitlines())
        shell_gui.display_output(reversed_content)
    except FileNotFoundError:
        shell_gui.display_output(f"Ошибка: Файл '{file_path}' не найден.")
    except IsADirectoryError:
        shell_gui.display_output(f"Ошибка: '{file_path}' является директорией.")
    except Exception as e:
        shell_gui.display_output(f"Ошибка при реверсировании файла: {e}")
