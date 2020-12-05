import datetime

# store the next available id for all new notes
last_id = 0


class Note:
    """
    Represents a note in the notebook. Match against a string in searched and
    store tags for each note
    """

    def __init__(self, memo, tags=''):
        """
        Initialize a note with memo and optional space separated tags.
        Automatically set the note's creation data and id
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """
        Determine if this note matches the filter text. Returns True if yes,
        False otherwise.

        Search is case sensitive and matches both memo text and tags.
        """
        return filter in self.memo or filter in self.tags


class Notebook:
    """
    Represents a collection of notes that can be tagged, modified and searched.
    """

    def __init__(self):
        """Initializes a notebook with an empty list."""
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        Creates a new note and appends it to the list.
        """

        note = Note(memo=memo, tags=tags)
        self.notes.append(note)
        return note

    def modify_memo(self, note_id, memo):
        """
        Find a new with the given id and change its memo to the given value.
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
        return note

    def modify_tags(self, note_id, tags):
        """
        Find a note with the given id and changes its tags to the given value.
        """
        note = self._find_note(note_id)
        if note:
            note.tags = tags
        return note

    def search(self, filter):
        """
        Find and return all the notes that match the given filter string.
        """
        results = [note for note in self.notes if note.match(filter)]
        return results

    def _find_note(self, note_id):
        """Locate a note with a given id"""

        notes = [note for note in self.notes if str(note.id) == str(note_id)]

        if notes:
            note = notes[0]
            return note
        return
