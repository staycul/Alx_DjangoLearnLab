# Django Admin Setup for Book Model

1. Registered the `Book` model in `bookshelf/admin.py` using `@admin.register(Book)`.
2. Customized the admin interface with:
   - `list_display` → shows `title`, `author`, `publication_year`
   - `search_fields` → allows searching by `title` and `author`
   - `list_filter` → adds filter for `publication_year`
3. Created a superuser with `python manage.py createsuperuser`.
4. Verified in the Django Admin interface at http://127.0.0.1:8000/admin/
