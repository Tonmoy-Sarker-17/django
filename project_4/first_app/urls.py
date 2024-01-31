from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.index,name='home'),
    # path('about/<int:id>/', views.about,name='about'),
    # path('about/page/<int:id>/', views.about,name='about'),
    path('about/', views.about,name='about'),

]
