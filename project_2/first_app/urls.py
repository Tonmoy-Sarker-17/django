
from django.urls import path
# from first_app.views import home
# from first_app import views
from . import views
#  dot (.) indicates the current folder i am in

urlpatterns = [
    path('',views.home),
]
