import datetime

def date(fs, shell_gui, shell, args):
    # Получаем текущую дату и время
    current_datetime = datetime.datetime.now()

    # Форматируем дату и время, например, в формате 'ДД-ММ-ГГГГ ЧЧ:ММ:СС'
    formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    
    # Отображаем результат
    shell_gui.display_output(formatted_datetime)
