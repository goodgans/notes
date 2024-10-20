import json
import datetime


def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file,indent=4)

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        print("Notes file not found.")

def add_note(title, message):
    note = {
        'id': len(notes) + 1,
        'title': title,
        'message': message,
        'timestamp': datetime.datetime.now().isoformat()
    }
    notes.append(note)
    save_notes()

def edit_note(note_id, title, message):
    for note in notes:
        if note['id'] == note_id:
            note['title'] = title
            note['message'] = message
            note['timestamp'] = datetime.datetime.now().isoformat()
            save_notes()
            return
    print("Note not found.")

def delete_note(note_id):
    global notes
    notes = [note for note in notes if note['id'] != note_id]
    save_notes()

def filter_notes_by_date(date):
    filtered_notes = [note for note in notes if date in note['timestamp']]
    return filtered_notes

def read_notes():
    for note in notes:
        print(note)
