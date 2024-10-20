from commands import *

"""
Основная программа для консольного управления заметками
Запцускается при отсуствии внешних агрументов
"""
def main_console():
    while True:
        command = input("Enter command (add, edit, delete, read, filter, exit): ")
        if command == 'add':
            title = input("Enter note title: ")
            message = input("Enter note message: ")
            add_note(title, message)
            print("Note added successfully.")
        elif command == 'edit':
            note_id = int(input("Enter note id to edit: "))
            title = input("Enter new title: ")
            message = input("Enter new message: ")
            edit_note(note_id, title, message)
        elif command == 'delete':
            note_id = int(input("Enter note id to delete: "))
            delete_note(note_id)
            print("Note deleted successfully.")
        elif command == 'read':
            read_notes()
        elif command == 'filter':
            date = input("Enter date to filter notes (YYYY-MM-DD): ")
            filtered_notes = filter_notes_by_date(date)
            for note in filtered_notes:
                print(note)
        elif command == 'exit' or command == 'quit' or command == 'q':
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please try again.")