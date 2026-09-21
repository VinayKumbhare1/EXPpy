class Book:
    """Represents a book with essential metadata."""
    def __init__(self, isbn: str, title: str, author: str, year: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[ISBN: {self.isbn}] '{self.title}' by {self.author} ({self.year})"


class HashNode:
    """Node for a singly linked list to handle hash collisions via chaining."""
    def __init__(self, key: str, value: Book):
        self.key = key
        self.value = value
        self.next = None


class LibraryHashTable:
    """Hash Table using custom hashing and separate chaining."""
    def __init__(self, initial_capacity: int = 11):
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * self.capacity

    def _hash(self, key: str) -> int:
        """
        Custom hash function using polynomial rolling hash (base 31)
        to map string keys (ISBNs) to table indices.
        """
        hash_value = 0
        prime = 31
        for char in key:
            hash_value = (hash_value * prime + ord(char)) % self.capacity
        return hash_value

    def insert(self, book: Book) -> bool:
        """Inserts a book or updates it if the ISBN already exists."""
        key = book.isbn
        index = self._hash(key)
        current = self.table[index]

        # Check if key already exists (Update case)
        while current:
            if current.key == key:
                current.value = book
                return False  # Updated existing book
            current = current.next

        # Insert new node at the head of the chain (O(1) insertion)
        new_node = HashNode(key, book)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1
        return True  # Inserted new book

    def search(self, isbn: str) -> Book | None:
        """Searches for a book by its ISBN. Returns Book if found, else None."""
        index = self._hash(isbn)
        current = self.table[index]

        while current:
            if current.key == isbn:
                return current.value
            current = current.next

        return None

    def delete(self, isbn: str) -> bool:
        """Deletes a book by its ISBN. Returns True if successful, False otherwise."""
        index = self._hash(isbn)
        current = self.table[index]
        prev = None

        while current:
            if current.key == isbn:
                if prev is None:
                    # Remove head of the list
                    self.table[index] = current.next
                else:
                    # Bypass current node
                    prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next

        return False

    def display_all(self):
        """Prints all stored books along with their bucket indexes."""
        if self.size == 0:
            print("Library is currently empty.")
            return

        print("\n--- Current Library Index ---")
        for i, node in enumerate(self.table):
            if node:
                current = node
                chain = []
                while current:
                    chain.append(str(current.value))
                    current = current.next
                print(f"Bucket {i}: {' -> '.join(chain)}")
        print("-----------------------------\n")


# ==================== Demonstration ====================
if __name__ == "__main__":
    library = LibraryHashTable(initial_capacity=7)

    # 1. Insertion
    print("--- Adding Books ---")
    b1 = Book("978-0131103627", "The C Programming Language", "Kernighan & Ritchie", 1978)
    b2 = Book("978-0201633610", "Design Patterns", "Gamma et al.", 1994)
    b3 = Book("978-0132350884", "Clean Code", "Robert C. Martin", 2008)
    b4 = Book("978-0262033848", "Introduction to Algorithms", "Cormen et al.", 2009)

    for book in [b1, b2, b3, b4]:
        library.insert(book)
        print(f"Added: {book}")

    library.display_all()

    # 2. Search
    print("--- Searching for Books ---")
    target_isbn = "978-0132350884"
    found_book = library.search(target_isbn)
    if found_book:
        print(f"Found: {found_book}")
    else:
        print(f"Book with ISBN {target_isbn} not found.")

    # 3. Deletion
    print("\n--- Deleting a Book ---")
    delete_isbn = "978-0201633610"
    if library.delete(delete_isbn):
        print(f"Successfully deleted book with ISBN: {delete_isbn}")
    else:
        print(f"Failed to delete. ISBN {delete_isbn} not found.")

    library.display_all()
