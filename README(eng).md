### Note Taking Program for GEEKBRAINS

This is a simple note-taking program developed by Artem Filosof for GEEKBRAINS. The program allows users to add, edit, delete, read, filter, and exit notes easily through the command line interface.

### Usage

To run the program, execute the `main()` function. The program accepts the following command line arguments:

- `--command`: Specify the action to perform (`add`, `edit`, `delete`, `read`, `filter`, `exit`).
- `--title`: Provide the title of the note.
- `--msg`: Enter the content of the note.
- `--note_id`: Specify the note ID for editing or deleting (positive number).

### Commands

- `add`: Add a new note with the given title and message.
- `edit`: Edit an existing note by providing the note ID, new title, and new message.
- `delete`: Delete a note by providing the note ID.
- `read`: Display all notes.
- `filter`: Filter notes by a specific date (in the format `YYYY-MM-DD`).
- `exit` or `quit`: Exit the program.

