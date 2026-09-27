class Publication:
    def __init__(self, name: str):
        self.name = name


class Book(Publication):
    def __init__(self, name: str, author: str, page_count: int):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        """Prints all details of the magazine."""
        print(f"Magazine Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

if __name__ == "__main__":
    # Creating instances of Book and Magazine
    book = Book("The Hobbit", "J.R.R. Tolkien", 310)
    magazine = Magazine("National Geographic", "Nathan Lump")

    # Printing information using the print_information method
    print("--- Book Info ---")
    book.print_information()
    
    print("\n--- Magazine Info ---")
    magazine.print_information()