from django.urls import path

from .views import HomePageView, AboutView, ContactFormView, ProjectsListView

# URL configuration for the portfolio app view.
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("projects/", ProjectsListView.as_view(), name="projects"),
    path('contact/', ContactFormView.as_view(), name="contact")
]