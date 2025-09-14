"""
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="list_books"),   # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
]
"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Registration (still custom)
    path("register/", views.register_view, name="register"),

    # Login using Django's built-in class-based view
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),

    # Logout using Django's built-in class-based view
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]


