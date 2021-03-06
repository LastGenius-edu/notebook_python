'''
Sultanov Andriy
Lab 4 Year 1 Semester 2
'''
import datetime

# Store the next available id for all new notes in a global variable
last_id = 0


class Note:
    """
    Represent a note in the notebook. Match against ф
    string in searches and store tags for each note.

    Has attributes:
        memo - string representing the body of the note
        creation_date - date
        tags - list of strings representing tags

    Has methods:
        __str__ - returns a nicely formatted string
        __repr__ - returns a pythonish strict representation
        match - returns a boolean based on whether the word was found in the memo
    """

    def __init__(self, memo, tags=()):
        """
        (string, tuple) -> Note

        Initialize a note with memo and optional
        list of tags. Automatically set the note's
        creation date and a unique id.
        """

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def __str__(self):
        '''
        (Note) -> string

        Returns a nicely formatted string
        '''
        return f"\nNote created on {self.creation_date}." \
               f"\nTags: {', '.join(self.tags)}:\n{self.memo}"

    def __repr__(self):
        '''
        (Note) -> string

        Returns a pythonish strict representation of a Note
        '''
        return "Note({}, {}, {})".format(self.memo, self.creation_date, self.tags)

    def match(self, filtr):
        """
        (string) -> bool

        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.
        """
        return filtr in self.memo or filtr in self.tags


class Notebook:
    """
    Represent a collection of notes that can be tagged,
    modified, and searched.

    Has attributes:
        notes - list of Notes

    Has methods:
        __str__ - returns a nicely formatted string
        __repr__ - returns a pythonish strict representation
        new_note - creates a new Note given a memo
        _find_note - an internal function looking for a note with a given id
        modify_memo - changes the contents of a memo by an id
        modify_tags - changes the tags of a memo by an id
        search - returns a list with all the memos containing the word
    """

    def __init__(self):
        """
        (None) -> Notebook

        Initialize a notebook with an empty list.
        """
        self.notes = []

    def __str__(self):
        """
        (Notebook) -> string

        Returns a nicely formatted string of all the notes in the Notebook
        """
        result = "\nNotebook:\n"
        for note in self.notes:
            result += f"\nNote created on {note.creation_date}.\nTags: " \
                      f"{', '.join(note.tags)}\nMemo: {note.memo}"
        return result

    def new_note(self, memo, tags=()):
        """
        (string, list) -> None

        Create a new note and add it to the list.
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """
        (int) -> Note

        Locate the note with the given id.
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        """
        (int, string) -> None

        Find the note with the given id and change its
        memo to the given value.
        """
        try:
            self._find_note(note_id).memo = memo
        except AttributeError:
            print(f"Note with id {note_id} not found")

    def modify_tags(self, note_id, tags):
        """
        (int, list) -> None

        Find the note with the given id and change its
        tags to the given value.
        """
        try:
            self._find_note(note_id).tags = tags
        except AttributeError:
            print(f"Note with id {note_id} not found")

    def search(self, filtr):
        """
        Find all notes that match the given filter
        string.
        """
        return [note for note in self.notes if note.match(filtr)]


def main():
    '''
    Test function
    '''
    n1 = Note("hello first")
    n2 = Note("hello again")
    print(n1.id)
    print(n2.id)
    print(n1.match('hello'))
    print(n2.match('second'))

    n = Notebook()
    n.new_note("hello world")
    n.new_note("hello again")
    print(n.notes)

    print(n.notes[0].id)
    print(n.notes[1].id)
    print(n.notes[0].memo)
    print(n.notes[1].memo)
    print(n.search("hello"))
    print(n.search("world"))
    n.modify_memo(4, "hi world")
    print(n.notes[1].memo)

    print(n)

    print("\n\nObject of class Note: ", n1)
    print("\nIs n1 an instance of the class Note? ", isinstance(n1, Note))
    print("\nMethods of class Note:", dir(n1))


if __name__ == '__main__':
    main()
