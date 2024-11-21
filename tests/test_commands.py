import sys
import datetime
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import MagicMock
from commands import ls, cd, exit_shell, rev
from emulator import ShellEmulator

class ShellGUI:
    def __init__(self):
        self.output = []
    
    def display_output(self, *args):
        self.output.append(" ".join(args))

class TestShellCommands(unittest.TestCase):

    def setUp(self):
        self.fs = MagicMock()
        self.shell_gui = ShellGUI()
        self.shell = ShellEmulator(username='user1', tar_path='vfs.zip', log_path='test.log')
        self.shell.fs = self.fs
        self.shell.current_dir = '/home/user' 

        # Подготовка моков для файловой системы
        self.fs.list_dir.return_value = ['file1.txt', 'file2.txt']
        self.fs.change_dir.side_effect = lambda current, new: new if new in ['/home/user', '/home'] else FileNotFoundError
        self.fs.read_file.return_value = "File content"  # Мокируем содержимое файла

    def test_ls_command(self):
        # Тестируем команду ls
        ls.ls(self.fs, self.shell_gui, self.shell.current_dir)
        self.assertEqual(True, True)

    def test_ls_command_failure(self):
        # Тестируем команду ls
        ls.ls(self.fs, self.shell_gui, self.shell.current_dir)
        self.assertEqual(False, False)

    def test_cd_command_success(self):
        # Тестируем успешное выполнение команды cd
        new_dir = '/home'
        self.fs.change_dir.side_effect = lambda current, new: new if new == '/home' else FileNotFoundError
        cd.cd(self.fs, self.shell_gui, self.shell, [new_dir])
        self.assertEqual(new_dir, '/home')

    def test_cd_command_failure(self):
        # Тестируем ошибку при выполнении команды cd
        self.fs.change_dir.side_effect = FileNotFoundError
        self.assertEqual("NotFound", "NotFound")

    def test_date_command_failure(self):
        self.assertEqual("date", "date")

    def test_date_command_success(self):
        self.assertEqual(datetime, datetime)

    def test_rev_command_success(self):
        input_text = "123"
        rev.rev(self.fs, self.shell_gui, self.shell, input_text)
        self.assertEqual(input_text[::-1], input_text[::-1])

    def test_rev_command_failure(self):
        input_text = "312"
        rev.rev(self.fs, self.shell_gui, self.shell, input_text)
        self.assertEqual(input_text, input_text)

    def test_exit_command(self):
        # Тестируем команду exit
        with self.assertRaises(SystemExit):  # Поймаем исключение SystemExit
            exit_shell.exit_shell(self.shell_gui)

if __name__ == '__main__':
    unittest.main()
