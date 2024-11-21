from commands import ls, cd, exit_shell, cat, rev, date
from filesystem import VirtualFileSystem
from log_handler import LogHandler

class ShellEmulator:
    def __init__(self, username, tar_path, log_path):
        self.username = username
        self.history = []

        self.current_dir = '/'

        self.logger = LogHandler(log_path, username)

        self.fs = VirtualFileSystem(tar_path)

    
    def execute_command(self, command, shell_gui):
        self.logger.log(command)
        self.history.append(command)

        parts = command.split()
        if not parts:
            return

        cmd = parts[0]
        args = parts[1:]

        if cmd == 'ls':
            ls.ls(self.fs, shell_gui, self.current_dir)
        elif cmd == "cat":
            cat.cat(self.fs, shell_gui, self, args)
        elif cmd == "rev":
            rev.rev(self.fs, shell_gui, self, args)
        elif cmd == "date":
            date.date(self.fs, shell_gui, self, args)
        elif cmd == 'cd':
            try:
                new_dir = cd.cd(self.fs, shell_gui, self, args)
                if new_dir is not None:
                    self.current_dir = new_dir
            except FileNotFoundError:
                shell_gui.display_output(f"Ошибка: Директория '{args[0]}' не найдена.")
            except NotADirectoryError:
                shell_gui.display_output(f"Ошибка: '{args[0]}' не является директорией.")
            except Exception as e:
                shell_gui.display_output(f"Ошибка при смене директории: {e}")
        elif cmd == 'exit':
            exit_shell.exit_shell(shell_gui)
        else:
            shell_gui.display_output("Команда не найдена")
    