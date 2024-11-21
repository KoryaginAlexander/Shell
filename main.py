import configparser
from shell_gui import ShellGUI

def main():
    config = configparser.ConfigParser()
    config.read("config.ini")  # Указываем путь к конфигурационному файлу
    
    # Читаем необходимые параметры из ini-файла
    username = config.get("settings", "username", fallback=None)
    fs = config.get("settings", "fs", fallback=None)
    log = config.get("settings", "log", fallback=None)
    config_script = config.get("settings", "config", fallback=None)

    # Проверяем, что обязательные параметры указаны
    if not username or not fs or not log:
        raise ValueError("Параметры 'username', 'fs' и 'log' обязательны в конфигурационном файле!")

    # Инициализируем ShellGUI
    shell_gui = ShellGUI(username, fs, log, config_script)
    if config_script:
        with open(config_script, 'r') as script:
            for line in script:
                shell_gui.command_entry.insert(len(f"{shell_gui.shell.username}@shell: {shell_gui.shell.current_dir} $ "), line.strip())
                shell_gui.execute_command()
    shell_gui.run()

if __name__ == "__main__":
    main()
