from django.urls import path, include
from . import views

# bind the extensions to the appropriate from views function
urlpatterns = [
    path('game/', views.start_game, name="game_start"),
    path('classic/', views.toggle_classic, name="toggle_classic"),
    path('lotr/', views.toggle_lotr, name="toggle_lotr"),
    path('pride/', views.toggle_pride, name="toggle_pride"),
    path('presidents/', views.toggle_presidents, name="toggle_presidents"),
    path('countries/', views.toggle_countries, name="toggle_countries"),
    path('star/', views.toggle_star, name="toggle_countries"),
    path('dune/', views.toggle_dune, name="toggle_dune"),
    path('addemail/', views.add_email, name="add_email"),
    path('resetemails/', views.reset_emails, name="reset_emails"),
    path('', views.home_start, name="home_start")
]
