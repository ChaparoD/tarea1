from django.urls import path
from . import views


#inculde le agrega el /
urlpatterns =[
path("", views.index, name="index"),
path("home", views.home, name="home"),  
path("breakingbad/<int:id>", views.breakingbad, name ="breakingbad"),
path("bettercallsaul/<int:id>", views.bettercallsaul, name ="bettercallsaul"),
path("episode/<int:ide>", views.episode, name ="episode"),
path("character/<int:eid>/<str:chr>", views.character, name ="character"),
path("character/<int:cid>/breakingbad/<int:sid>", views.configbb, name ="config"),
path("character/<int:cid>/bettercallsaul/<int:sid>", views.configbcs, name ="config"),
]
