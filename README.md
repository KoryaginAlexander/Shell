
# Shell Emulator
![Интерфейс](https://i.imgur.com/AuX8p4Z.png)
## Описание

Этот проект реализует эмулятор оболочки, который поддерживает основные команды, такие как изменение директорий, отображение файлов, изменение прав владения файлами и другие, используя виртуальную файловую систему, извлечённую из архива tar.

## Версия Python

Для работы с проектом требуется Python 3.10 или новее. Рекомендуется создать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows
```

## Необходимые библиотеки

Убедитесь, что у вас установлены следующие библиотеки, необходимые для тестирования:

- `exceptiongroup==1.2.2`
- `iniconfig==2.0.0`
- `packaging==24.1`
- `pluggy==1.5.0`
- `pytest==8.3.3`
- `tomli==2.0.2`

Вы можете установить библиотеки с помощью pip после активации виртуального окружения:

```bash
pip install -r requirements.txt
```

## Настройка

Чтобы настроить вашу виртуальную файловую систему (VFS), вы можете либо создать свой собственный архив tar, либо использовать предоставленный скрипт. Вот два варианта:

### Вариант 1: Создание архива tar с помощью скрипта

Запустите следующую команду, чтобы создать файл `vfs.zip`:

```bash
python create_zip.py
```


Это создаст структуру директорий с двумя файлами (`file1.txt` и `file2.txt`) и упакует её в `vfs.zip`.

## Запуск эмулятора

Рекомендуется сначала запустить эмулятор оболочки напрямую из командной строки, а затем с использованием стартового скрипта.


Сделайте config.ini

```ini
[settings]
username = user1
fs = vfs.zip
log = log.csv
config=
```

### Вариант 1: Запуск без скрипта

Оставьте config= в config.ini пустым

### Вариант 2: Использование стартового скрипта

Вот пример того, как может выглядеть ваш скрипт `start.sh`:

```bash
ls
cd test_dir/home/user
ls
```

Впишите его в ini

```ini
config=start.sh
```

Запускайте эмулятор:

```bash
python main.py
```

## Использование

После запуска эмулятора оболочки вы можете использовать такие команды, как:

- `ls` - Отобразить файлы в текущей директории.
- `cd <директория>` - Перейти в указанную директорию.
- `cat ` -  Просмотр файла
- `date` - Текущая дата
- `rev` - Перевернуть содержимое файла
- `exit` - Выйти из эмулятора оболочки.

## Тесты

Для тестирования функций используется фреймворк pytest
Тестируются:
- test_ls_command
- test_ls_command_failure
- test_cd_command_success
- test_cd_command_failure
- test_date_command_failure
- test_date_command_success
- test_rev_command_success
- test_rev_command_failure
- test_exit_command
![Тесты](https://i.imgur.com/n0gHO0K.png)