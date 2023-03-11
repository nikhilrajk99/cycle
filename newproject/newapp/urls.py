from . import views
from django.urls import path
app_name='newapp'


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('news',views.news,name='news'),
    path('cycle',views.cycle,name='cycle')
]