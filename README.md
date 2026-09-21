# Library Book Indexing System Using Hash Tables

A Python-based data structure project that implements a **Library Book Indexing System** using a custom Hash Table with separate chaining. This project provides efficient storage, fast retrieval, updates, and deletion of book records based on their unique ISBN identifiers.

---

## 📌 Project Overview

In a large library system, retrieving book details quickly is essential. This implementation utilizes a **Custom Hash Table** rather than built-in dictionary primitives to demonstrate fundamental computer science concepts:
- **Fast Lookups:** $O(1)$ average time complexity for operations using unique ISBNs.
- **Custom Hashing:** Implements polynomial rolling hash function (base 31) to convert string ISBNs to table bucket indices.
- **Collision Handling:** Uses **Separate Chaining** with singly-linked lists to resolve hash collisions gracefully.

---

## 🚀 Features

- **Insertion:** Add new book records (`ISBN`, `Title`, `Author`, `Publication Year`). Updates record if ISBN already exists.
- **Lookup / Search:** Retrieve complete book details by searching with an ISBN.
- **Deletion:** Remove book records safely from the index by ISBN.
- **Index Visualization:** Display all hash buckets and linked list chains to inspect collision distributions.

---

## 📁 Project Structure

```text
.
├── library_hash_table.py   # Main implementation file
└── README.md               # Project documentation
