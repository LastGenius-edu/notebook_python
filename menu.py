'''
Sultanov Andriy
Lab 4 Year 1 Semester 2

Menu module.
CLI representation of the Notebook base on Notebook and Note classes
'''
import sys

from notebook import Notebook


def display_menu():
    """
    (None) -> None

    Displaus the choices the function
    """
    print("""
    Notebook Menu
    1. Show all Notes
    2. Search Notes
    3. Add Note
    4. Modify Note
    5. Quit
    """)


def quit_program():
    """
    (None) -> None

    Ends the program
    """
    print("Thank you for using your notebook today.")
    sys.exit(0)


class Menu:
    """
    Display a menu and respond to choices when run.
    """

    def __init__(self):
        """
        (None) -> None

        Initializes a Notebook, memorizes the functions in a dict
        """
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": quit_program
            }


    def run(self):
        """
        (None) -> None

        Display the menu and respond to choices.
        """
        while True:
            display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid choice".format(choice))


    def show_notes(self, notes=None):
        """
        (list) -> None

        Prints the list of notes
        """
        if not notes:
            notes = self.notebook.notes
            if not notes:
                print("Notebook is empty")
        for note in notes:
            print("\n{}: {}\n{}".format(note.id, note.tags, note.memo))


    def search_notes(self):
        """
        (None) -> None

        Searches the notes and displays the found list
        """
        filtr = input("Search for: ")
        notes = self.notebook.search(filtr)
        self.show_notes(notes)


    def add_note(self):
        """
        (None) -> None

        Adds a note to the notebook
        """
        memo = input("Enter a memo: ")
        tags = input("Enter tags divided by commas: ").split(",")
        self.notebook.new_note(memo, tags)
        print("\nYour note has been added.")


    def modify_note(self):
        """
        (None) -> None

        Modifies a note given an id
        """
        id_num = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id_num, memo)
        if tags:
            self.notebook.modify_tags(id_num, tags)


if __name__ == "__main__":
    Menu().run()
