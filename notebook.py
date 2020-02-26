'''
Sultanov Andriy
Lab 4 Year 1 Semester 2
'''
import datetime


class Note:
    '''
    Note class

    Has attributes:
        memo - string representing the body of the note
        creation_date - date
        tags - list of strings representing tags

    Has methods:
        __str__ - returns a nicely formatted string
        __repr__ - returns a pythonish strict representation
        match - returns a boolean based on whether the word was found in the memo
    '''

    def __init__(self, memo, creation_date, tags):
        '''
        (Note, string, date, list) -> Note

        Initializes a Note class.
        '''
        self.memo = memo
        self.creation_date = creation_date
        self.tags = tags


    def __str__(self):
        '''
        (Note) -> string

        Returns a nicely formatted string
        '''
        return "\nNote created on {}.\nTags: {}:\n{}".format(self.creation_date, ", ".join(self.tags), self.memo)


    def __repr__(self):
        '''
        (Note) -> string

        Returns a pythonish strict representation
        '''
        return "Note({},{},{})".format(self.memo, self.creation_date, self.tags)


    def match(self, search_filter):
        '''
        (Note, string) -> bool

        Returns a boolean based on whether the word was found in the memo
        '''
        return search_filter in self.memo


class Notebook:
    '''
    Notebook class

    Has attributes:
        notes - list of Notes

    Has methods:
        __str__ - returns a nicely formatted string
        __repr__ - returns a pythonish strict representation
        match - returns a boolean based on whether the word was found in the memo
    '''

    def __init__(self, notes=[]):
        '''
        (Notebook, list) -> Notebook

        Initializes a Notebook class.
        '''
        self.notes = notes


    def __str__(self):
        '''


         
        '''
        result = ""
        for note in self.notes:
            result += "\nNote created on {}.\nTags: {}:\n{}".format(note.creation_date, ", ".join(note.tags), note.memo)
        return result


    def search(self, tag_filter):
        return list(filter(lambda x: tag_filter in x.tags, [note for note in self.notes]))


    def new_note(self, memo, tags=""):
        self.notes.append(Note(memo, datetime.datetime.now(), tags))


    def modify_memo(self, note_id, memo):
        self.notes[note_id].memo = memo


    def modify_tags(self, note_id, tags):
        self.notes[note_id].tags = tags



def main():
    notebook1 = Notebook()
    notebook1.new_note("memo1 test text",["test", "troll"])
    notebook1.new_note("memo2 test text", ["test", "ucu"])
    print(notebook1.notes)
    print(notebook1.search('test'))
    print(notebook1.search('ucu'))
    notebook1.modify_memo(0, 'CHANGED THE TEXT')
    notebook1.modify_tags(0, ['changed', 'the', 'tags'])
    print(notebook1.notes)


if __name__ == '__main__':
    main()