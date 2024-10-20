import datetime
import json

from main import notes


class Note:
    def __init__(self, title, message):
        self.id = len(notes) + 2
        self.title = title
        self.message = message
        self.timestamp = datetime.datetime.now().isoformat()


def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)


def add_note(title, message):
    note = Note(title, message)
    notes.append(vars(note))
    save_notes()