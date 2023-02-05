from django.contrib import admin
from django.urls import path
from Portfolio_app import views
urlpatterns = [
    path('',views.home, name="home"),
    path('fb',views.home,name='feedback'),
    # path('aboutme',views.aboutme,name='aboutme'),
    # path('project',views.project,name='project'),
    # path('certificate',views.certificate,name='certificate'),
    # path('feedback',views.feedback,name='feedback'),
    # path('fb',views.fb,name='fb')
]