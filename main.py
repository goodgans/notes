# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.Например:

from commands import *
from main_console import main_console

notes = []

import argparse


def main():
    load_notes()
    parser = argparse.ArgumentParser(description='Note Taking Program for GEEKBRAINS by Artem Filosof')
    parser.add_argument('--command', choices=['add', 'edit', 'delete', 'read', 'filter', 'exit'],
                        help='Enter command (add, edit, delete, read, filter, exit)')
    parser.add_argument('--title', type=str, help='Note title (Text)')
    parser.add_argument('--msg', type=str, help='Note message (Text)')
    parser.add_argument('--note_id', type=str, help='Note id message to edit or delete(Positive Number)')
    args = parser.parse_args()

    if args.command == '':
        print("=================")
    if args.command == 'add':
        add_note(args.title, args.msg)
        print("Note added successfully.")
    elif args.command == 'edit':
        # проверка на пустой аргумент
        if args.note_id == None:
            note_id = int(input("Enter note id to edit: "))
        else:
            note_id = int(args.note_id)
        if args.title == None:
            title = input("Enter new title: ")
        else:
            title = args.title
        if args.msg == None:
            message = input("Enter new message: ")
        else:
            message = args.msg
        edit_note(note_id, title, message)
    elif args.command == 'delete':
        note_id = int(input("Enter note id to delete: "))
        delete_note(note_id)
        print("Note deleted successfully.")
    elif args.command == 'read':
        read_notes()
    elif args.command == 'filter':
        date = input("Enter date to filter notes (YYYY-MM-DD): ")
        filtered_notes = filter_notes_by_date(date)
        for note in filtered_notes:
            print(note)
    elif args.command == 'exit' or args.command == 'quit' or args.command == 'q':
        print("Exiting program.")
    else:
        print("Command line arguments not recognized.")
        main_console()




if __name__ == "__main__":
    main()
