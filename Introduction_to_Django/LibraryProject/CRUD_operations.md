# Create Operation

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(book)
# Output: 1984 by George Orwell (1949)



### `retrieve.md`
```markdown
# Retrieve Operation

```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949



### `update.md`
```markdown
# Update Operation

```python
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four



### `delete.md`
```markdown
# Delete Operation

```python
book.delete()
print(Book.objects.all())
# Output: <QuerySet []>
