from django.urls import path 
from . import views

urlpatterns = [
    path("",views.intro),
    path("about",views.about),
    path("work",views.work),
    path("clients",views.clients),
    path("letstotalk",views.letstalk)
    

]
